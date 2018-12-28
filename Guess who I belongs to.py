
version = "Guess who I belongs to ?"
#Definit le nom de la version

#______________________________Imports (EXPORT)__________________________

 #Importation des modules
from tkinter import *
from PIL import Image, ImageTk
import winsound
import time

import fct_Home
import fct_Messages
import fct_Calculatrice
import fct_Galerie
import fct_Persos

#__________________________________Fenetres_____________________________
root = Tk()

root.title(version) #Definit la version
root["bg"]="black" #Change la couleur du Canvas
root.attributes('-fullscreen',True) #Sert a mettre le jeu en plein ecran
root.overrideredirect(True) #Enleve la barre qui permet de fermer le programme en haut
w,h = root.winfo_screenwidth(),root.winfo_screenheight() #recupere la taille de l'ecran et la stocke dans des variables

#____________________________Fonction deverrouillage________________________

def ClicDev(event):
        # Gestion de l'evenement Clic gauche
        global clic_deverrouillage
        # position du pointeur de la souris
        X = event.x
        Y = event.y
        # coordonnees de l'objet fleche
        [xmin,ymin] = Candev.coords(Fleche)
        # Si le clique est dans les coordonnees fleche
        if X-72<=xmin<=X:
            clic_deverrouillage = True
            #clic_deverrouillage est confirmer
        #sinon
        else :
            clic_deverrouillage = False
            #clic_deverrouillage est refuser

def Drag(event):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    #Si clic_deverrouillage est confirmer
    if clic_deverrouillage == True:
        # limite de l'objet dans le canvas
        if X<38 : X=38
        if X>328: X=328
        if Y<38 : Y=38
        if Y>38 : Y=38
        # mise a jour de la position de l'objet (drag)
        Candev.coords(Fleche,X-38,Y-38)

def deverrouiller():
    global n
    n=200
    if n==200:
        n=2
        #Supprime les canvas du deverrouillage
        can3.destroy()
        Candev.destroy()
        #change le bureau par l'image avec les caracteristique des personnes
        can1.itemconfig(canFond,image= Fond)
        #met l'ecran du telphone avec les applications
        can2.place(x=745,y=154)
        #met a jour l'heure en haut de l'ecran
        can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")

# check les coordonnees de la souris quand relachement de la fleche
def win(event):
    X = event.x
    [xmin,ymin] = Candev.coords(Fleche)
    #Si c'est dans les coordonnees de la zone ou la fleche doit etre et que clic_deverrouiller est confirmer
    if 315<=event.x and clic_deverrouillage ==True:
            #lance la fonction deverrouiller
            deverrouiller()


#met de base clic_deverrouillage en off
clic_deverrouillage = False
#____________________________Fonction positions____________________________

def Clique(evt):  #la variable evt a recupere l'information lors du clic de la souris
    global root, can2, can3, canMenu, n, total, p
    abscisse=str(evt.x) #Permet de recuperer les coordonnees sous forme de texte afin de les affichees plus tard
    ordonnee=str(evt.y)
#    can2.create_text(evt.x,evt.y,text="coord : X"+abscisse+" Y"+ordonnee) (Permet d'afficher les coordonnes lors du clique pour nous aider a faire les zones cliquables)

#_________________________Position_Menu__________________________________
#n est une variable qui verifie sur quelle application nous nous trouvons qui empeche de fonctionner des zones cliquables
    if n==1: #n==1 fait que ces zones cliquables ne marchent que sur le menu

        if 807<=evt.x<=1122 and 442<=evt.y<=542 : #Indique les coordonees de la zone du bouton jouer (c'est pareil pour tout le reste de Clique())
            n=200
            canMenu.delete()#Supprime le canvas du menu
            can1.place(x=0,y=0)#Place le Canvas de l'arriere du jeu (Ou il y a le telephone et plus tard les informations des peronnages)
            can3.place(x=745,y=154) #place l'ecran du telephone
            Candev.place(x=785,y=815) #place le canvas ou on fait glisser la fleche pour deverouiller le telephone
            can3.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure") #affiche l'heure

        if 799<=evt.x<=1122 and 687<=evt.y<=783 :
            root.destroy() #le bouton Quitter (detruit la fenetre)
#_________________________Position_Home_________________________________
    if n!=1:
        if 925<=evt.x<=1008 and 932<=evt.y<=1000 :
            n,total=fct_Home.retour(n,can2,total,Screen,HomePage)#permet de revenir a l'ecran d'acceuil du telephone
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC) #Arrette la musique quand on sort l'application de la musique

    if n==2:
        #Lance les fonctions stockees dans un programme externe et qui permet de lancer les applications
        if 29<=evt.x<=104 and 50<=evt.y<=125 :
            n=fct_Home.mail(n,can2,Screen,Mails) #le n=fct_... permet de recuperer le n du return n qu'il y a dans la fonction et qui change le global n
        if 132<=evt.x<=207 and 50<=evt.y<=125 :
            n=fct_Home.note(n,can2,Screen,BlocNotes)
        if 227<=evt.x<=302 and 50<=evt.y<=125 :
            n=fct_Home.appareilphoto(n,can2,Screen,AppareilPhoto)
        if 330<=evt.x<=405 and 50<=evt.y<=125 :
            n=fct_Home.photo(n,can2,Screen,Photo_Home)


        if 29<=evt.x<=104 and 150<=evt.y<=225 :
            n=fct_Home.facebook(n,can2,Screen,Facebook)
        if 132<=evt.x<=207 and 150<=evt.y<=225 :
            n=fct_Home.twitter(n,can2,Screen,Twitter)
        if 227<=evt.x<=302 and 150<=evt.y<=225 :
            n=fct_Home.tinder(n,can2,Screen,Tinder)
        if 330<=evt.x<=405 and 150<=evt.y<=225 :
            n=fct_Home.appstore(n,can2,Screen,AppStore)


        if 29<=evt.x<=104 and 250<=evt.y<=325 :
            n=fct_Home.chrome(n,can2,Screen,Chrome)
        if 132<=evt.x<=207 and 250<=evt.y<=325 :
            n=fct_Home.calendrier(n,can2,Screen,Calendrier)
        if 227<=evt.x<=302 and 250<=evt.y<=325 :
            n=fct_Home.horloge(n,can2,Screen,Horloge)
        if 330<=evt.x<=405 and 250<=evt.y<=325 :
            n=fct_Home.calculatrice(n,can2,Screen,Calculatrice_Home)


        if 29<=evt.x<=104 and 350<=evt.y<=425 :
            n=fct_Home.reglages(n,can2,Screen,Reglages)

        if 330<=evt.x<=405 and 550<=evt.y<=625 :
            root.destroy()


        if 29<=evt.x<=104 and 661<=evt.y<=736 :
            n=fct_Home.message(n,can2,Screen,Messages_Home)
        if 132<=evt.x<=207 and 661<=evt.y<=736 :
            n=fct_Home.contact(n,can2,Screen,Contact)
        if 227<=evt.x<=302 and 661<=evt.y<=736 :
            n=fct_Home.telephone(n,can2,Screen,Telephone)
        if 330<=evt.x<=405 and 661<=evt.y<=736 :
            n=fct_Home.musique(n,can2,Screen,Musiques)

#__________________________Fonctions positions Fin__________________________
    if n==42: #Ecran de victoire

        if 830<=evt.x<=1093 and 787<=evt.y<=859 :
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC)
            root.destroy()

    if n==43: #ecran GameOver

        if 830<=evt.x<=1093 and 787<=evt.y<=859 :
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC)
            root.destroy()

#__________________________Fonctions positions Musiques_____________________
    if n==12: #Application musique

        if 0<=evt.x<=440 and 130<=evt.y<=205 :
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC) #Enleve la musique pour pouvoir en lancer une autre
            can2.delete("artiste")#supprime l'ancien texte qui affiche l'artiste si il est deja afficher
            can2.delete("titre")#supprime l'ancien texte qui affiche le titre si il est deja afficher
            can2.create_text(20,720,font=("arial",11),fill='black',text="Mozart",anchor=NW,tag="artiste")#cree le texte avec afficher l'artiste
            can2.create_text(20,690,font=("arial",18),fill='black',text="Petite Musique de Nuit",anchor=NW,tag="titre")#cree le texte avec afficher le titre
            winsound.PlaySound("Musiques\Petite Musique de Nuit.wav", winsound.SND_ASYNC)#lance la musique du dossier Musique et fait quon peux continuer a utiliser le programme quand la musique tourne

        if 0<=evt.x<=440 and 205<=evt.y<=280 :
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC)
            can2.delete("artiste")
            can2.delete("titre")
            can2.create_text(20,720,font=("arial",11),fill='black',text="Schumann",anchor=NW,tag="artiste")
            can2.create_text(20,690,font=("arial",18),fill='black',text="Des pays lointains",anchor=NW,tag="titre")
            winsound.PlaySound("Musiques\Des pays lointains.wav", winsound.SND_ASYNC)

        if 0<=evt.x<=440 and 280<=evt.y<=355 :
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC)
            can2.delete("artiste")
            can2.delete("titre")
            can2.create_text(20,720,font=("arial",11),fill='black',text="Beethoven",anchor=NW,tag="artiste")
            can2.create_text(20,690,font=("arial",18),fill='black',text="Ode a la joie",anchor=NW,tag="titre")
            winsound.PlaySound("Musiques\Ode a la joie.wav", winsound.SND_ASYNC)

        if 0<=evt.x<=440 and 355<=evt.y<=430 :
            winsound.PlaySound("Musiques\StopSound.wav", winsound.SND_ASYNC)
            can2.delete("artiste")
            can2.delete("titre")
            can2.create_text(20,720,font=("arial",11),fill='black',text="Richard Wagner",anchor=NW,tag="artiste")
            can2.create_text(20,690,font=("arial",18),fill='black',text="La chevauchee des Walkyries",anchor=NW,tag="titre")
            winsound.PlaySound("Musiques\La chevauchee des Walkyries.wav", winsound.SND_ASYNC)


#_______________________Fonction positions Messages________________________
    if n==4: #Application messages

        if 0<=evt.x<=440 and 130<=evt.y<=205 :
            n=fct_Messages.Luke(n,can2,Screen,Messages_Luke)

        if 0<=evt.x<=440 and 205<=evt.y<=280 :
            n=fct_Messages.Maman(n,can2,Screen,Messages_Maman)

        if 0<=evt.x<=440 and 280<=evt.y<=355 :
            n=fct_Messages.Papa(n,can2,Screen,Messages_Papa)

        if 0<=evt.x<=440 and 355<=evt.y<=430 :
            n=fct_Messages.Patrice(n,can2,Screen,Messages_Patrice)

        if 0<=evt.x<=440 and 430<=evt.y<=505 :
            n=fct_Messages.Cusmar(n,can2,Screen,Messages_Cusmar)

        if 0<=evt.x<=440 and 505<=evt.y<=580 :
            n=fct_Messages.Alex(n,can2,Screen,Messages_Alex)

    if n==5:
        if 7<=evt.x<=27 and 44<=evt.y<=63 :
            n=fct_Messages.BackMessages(n,can2,Screen,Messages_Home)


#___________________________Positions Personnages_________________________

    if 605<=evt.x<=630 and 275<=evt.y<=300 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 578<=evt.x<=597 and 275<=evt.y<=300 :
        fct_Persos.RefuserJawad(can1,Cacher)
        p+=1#p est un compteur qui compte le nombre de personnage qu'on a cacher
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose) #Si tous les personnages sont caches game over

    if 605<=evt.x<=630 and 500<=evt.y<=525 :
        n=fct_Persos.AccepterWin(n,can1,can2,canWin)

    if 578<=evt.x<=597 and 500<=evt.y<=525 :
        fct_Persos.RefuserPeter(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 605<=evt.x<=630 and 745<=evt.y<=760 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 578<=evt.x<=597 and 745<=evt.y<=760 :
        fct_Persos.RefuserPatrick(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 605<=evt.x<=630 and 975<=evt.y<=1000 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 578<=evt.x<=597 and 975<=evt.y<=1000 :
        fct_Persos.RefuserJean(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1285<=evt.x<=1310 and 275<=evt.y<=300 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1322<=evt.x<=1342 and 275<=evt.y<=300 :
        fct_Persos.RefuserLionel(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1285<=evt.x<=1310 and 500<=evt.y<=525 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1322<=evt.x<=1342 and 500<=evt.y<=525 :
        fct_Persos.RefuserBrandon(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1285<=evt.x<=1310 and 745<=evt.y<=760 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1322<=evt.x<=1342 and 745<=evt.y<=760 :
        fct_Persos.RefuserNicolas(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1285<=evt.x<=1310 and 975<=evt.y<=1000 :
        n=fct_Persos.AccepterLose(n,can1,can2,canLose)

    if 1322<=evt.x<=1342 and 975<=evt.y<=1000 :
        fct_Persos.RefuserFrancois(can1,Cacher)
        p+=1
        if p==8:
            n=fct_Persos.AccepterLose(n,can1,can2,canLose)

#_______________________Fonction positions Calculatrice_______________________
    if n==3: #applications calculatrice

        if 133<=evt.x<=209 and 613<=evt.y<=664 :
            total=fct_Calculatrice.zero(n,can2,total,Screen)

        if 35<=evt.x<=112 and 540<=evt.y<=590 :
            total=fct_Calculatrice.un(n,can2,total,Screen)

        if 133<=evt.x<=209 and 540<=evt.y<=590 :
            total=fct_Calculatrice.deux(n,can2,total,Screen)

        if 231<=evt.x<=308 and 540<=evt.y<=590 :
            total=fct_Calculatrice.trois(n,can2,total,Screen)

        if 35<=evt.x<=112 and 466<=evt.y<=517 :
            total=fct_Calculatrice.quatre(n,can2,total,Screen)

        if 133<=evt.x<=209 and 466<=evt.y<=517 :
            total=fct_Calculatrice.cinq(n,can2,total,Screen)

        if 231<=evt.x<=308 and 466<=evt.y<=517 :
            total=fct_Calculatrice.six(n,can2,total,Screen)

        if 35<=evt.x<=112 and 390<=evt.y<=441 :
            total=fct_Calculatrice.sept(n,can2,total,Screen)

        if 133<=evt.x<=209 and 390<=evt.y<=441 :
            total=fct_Calculatrice.huit(n,can2,total,Screen)

        if 231<=evt.x<=308 and 390<=evt.y<=441 :
            total=fct_Calculatrice.neuf(n,can2,total,Screen)

        if 329<=evt.x<=404 and 540<=evt.y<=590 :
            total=fct_Calculatrice.plus(n,can2,total,Screen)

        if 329<=evt.x<=404 and 613<=evt.y<=664 :
            total=fct_Calculatrice.moins(n,can2,total,Screen)

        if 329<=evt.x<=404 and 466<=evt.y<=517 :
            total=fct_Calculatrice.multiplier(n,can2,total,Screen)

        if 329<=evt.x<=404 and 390<=evt.y<=441 :
            total=fct_Calculatrice.diviser(n,can2,total,Screen)

        if 231<=evt.x<=308 and 613<=evt.y<=664 :
            total=fct_Calculatrice.egal(n,can2,total,Calculatrice_Secret,Screen)

        if 35<=evt.x<=112 and 613<=evt.y<=664 :
            total=fct_Calculatrice.annuler(n,can2,total,Screen)

#_______________________Fonction positions galerie___________________________
    if n==13: #application galerie

        if 354<=evt.x<=388 and 716<=evt.y<=743 :
            n=fct_Galerie.Fav(n,can2,Screen,Photo_Fav)

        if 9<=evt.x<=103 and 110<=evt.y<=204 :
            n=fct_Galerie.FeuxArtifice(n,can2,Screen,Photo_FeuxArtifice)

        if 117<=evt.x<=210 and 110<=evt.y<=204 :
            n=fct_Galerie.DarkVador(n,can2,Screen,Photo_DarkVador)

        if 229<=evt.x<=326 and 110<=evt.y<=204 :
            n=fct_Galerie.Selfie(n,can2,Screen,Photo_Selfie)

        if 339<=evt.x<=430 and 110<=evt.y<=204 :
            n=fct_Galerie.Insecte(n,can2,Screen,Photo_Insecte)

        if 9<=evt.x<=103 and 214<=evt.y<=308 :
            n=fct_Galerie.Code(n,can2,Screen,Photo_Code)

        if 117<=evt.x<=210 and 214<=evt.y<=308 :
            n=fct_Galerie.Chat(n,can2,Screen,Photo_Chat)

        if 229<=evt.x<=326 and 214<=evt.y<=308 :
            n=fct_Galerie.Nourriture(n,can2,Screen,Photo_Nourriture)

    if n==17: #photo retour
        if 25<=evt.x<=36 and 721<=evt.y<=739 :
            n=fct_Home.photo(n,can2,Screen,Photo_Home)

    if n==23: #photo favoris
        if 9<=evt.x<=103 and 110<=evt.y<=204 :
            n=fct_Galerie.Code(n,can2,Screen,Photo_Code)

        if 39<=evt.x<=83 and 707<=evt.y<=753 :
            n=fct_Home.photo(n,can2,Screen,Photo_Home)


#_______________________Fonction positions contacts, telephone_________________

    if n==33:#Application telephone
        if 198<=evt.x<=243 and 705<=evt.y<=755 :
            n=fct_Home.contact(n,can2,Screen,Contact)

    if n==18: #Application contact
        if 25<=evt.x<=75 and 705<=evt.y<=755 :
            n=fct_Home.message(n,can2,Screen,Messages_Home)
        if 368<=evt.x<=416 and 705<=evt.y<=755 :
            n=fct_Home.telephone(n,can2,Screen,Telephone)

    if n==14: #AppareilPhoto
        if 368<=evt.x<=416 and 705<=evt.y<=755 :
            n=fct_Home.photo(n,can2,Screen,Photo_Home)

#_________________________________Variables______________________________

total="" #Affichage calculatrice
n=1 #pour rendre dispo certain clique sur certain canvas
titre="" #Variable avec le titre de la musique jouee
artiste="" #Variable avec le nom de l'artiste de la musique jouee
p=0 #Compteur de personnes caches

#__________________________________Images_______________________________
#importation des images en png et stock dans des variables

Gagner = ImageTk.PhotoImage(file="screen\Gagner.png")
GameOver = ImageTk.PhotoImage(file="screen\GameOver.png")
Cacher = ImageTk.PhotoImage(file="screen\Cacher.png")
Fond = ImageTk.PhotoImage(file="screen\Fond.png")
FondClear = ImageTk.PhotoImage(file="screen\FondClear.png")
Menu = ImageTk.PhotoImage(file="screen\Menu.png")
HomePage = ImageTk.PhotoImage(file="screen\HomePage.png")
Horloge = ImageTk.PhotoImage(file="screen\Horloge.png")
Calculatrice_Home = ImageTk.PhotoImage(file="screen\Calculatrice_Home.png")
Calculatrice_Secret = ImageTk.PhotoImage(file="screen\Calculatrice_Secret.png")
Mails = ImageTk.PhotoImage(file="screen\Mails.png")
AppStore = ImageTk.PhotoImage(file="screen\AppStore.png")
Chrome = ImageTk.PhotoImage(file="screen\Chrome.png")
Facebook = ImageTk.PhotoImage(file="screen\Facebook.png")
Tinder = ImageTk.PhotoImage(file="screen\Tinder.png")
Twitter = ImageTk.PhotoImage(file="screen\Twitter.png")
Photo_Home = ImageTk.PhotoImage(file="screen\Photo_Home.png")
AppareilPhoto = ImageTk.PhotoImage(file="screen\AppareilPhoto.png")
BlocNotes = ImageTk.PhotoImage(file="screen\BlocNotes.png")
Telephone = ImageTk.PhotoImage(file="screen\Telephone.png")
Horloge = ImageTk.PhotoImage(file="screen\Horloge.png")
Contact = ImageTk.PhotoImage(file="screen\Contact.png")
Reglages = ImageTk.PhotoImage(file="screen\Reglages.png")
Calendrier = ImageTk.PhotoImage(file="screen\Calendrier.png")

#__________________________Images_deverou_______________________________

ImgFleche = ImageTk.PhotoImage(file="screen\Fleche.png")
ImgWallpaper = ImageTk.PhotoImage(file="screen\Wallpaper.png")
ImgBarreDev = ImageTk.PhotoImage(file="screen\BarreDev.png")

#__________________________Images_galerie________________________________

Photo_FeuxArtifice = ImageTk.PhotoImage(file="screen\Photo_FeuxArtifice.png")
Photo_DarkVador = ImageTk.PhotoImage(file="screen\Photo_DarkVador.png")
Photo_Selfie = ImageTk.PhotoImage(file="screen\Photo_Selfie.png")
Photo_Insecte = ImageTk.PhotoImage(file="screen\Photo_Insecte.png")
Photo_Code = ImageTk.PhotoImage(file="screen\Photo_Code.png")
Photo_Chat = ImageTk.PhotoImage(file="screen\Photo_Chat.png")
Photo_Nourriture = ImageTk.PhotoImage(file="screen\Photo_Nourriture.png")
Photo_Fav = ImageTk.PhotoImage(file="screen\Photo_Fav.png")

#__________________________Images_Messages_____________________________

Messages_Home = ImageTk.PhotoImage(file="screen\Messages_Home.png")
Messages_Luke = ImageTk.PhotoImage(file="screen\Messages_Luke.png")
Messages_Maman = ImageTk.PhotoImage(file="screen\Messages_Maman.png")
Messages_Papa = ImageTk.PhotoImage(file="screen\Messages_Papa.png")
Messages_Patrice = ImageTk.PhotoImage(file="screen\Messages_Patrice.png")
Messages_Cusmar = ImageTk.PhotoImage(file="screen\Messages_Cusmar.png")
Messages_Alex = ImageTk.PhotoImage(file="screen\Messages_Alex.png")

#________________________Images_Musiques________________________________

Musiques = ImageTk.PhotoImage(file="screen\Musiques.png")
Musiques_Play = ImageTk.PhotoImage(file="screen\Musiques_Play.png")
Musiques_Pause = ImageTk.PhotoImage(file="screen\Musiques_Pause.png")

#_________________________Images_Pong__________________________________
Ballon = ImageTk.PhotoImage(file="screen\Ballon.png")
Barre = ImageTk.PhotoImage(file="screen\Barre.png")
FondPong = ImageTk.PhotoImage(file="screen\FondPong.png")


#creation des canvas , placement du canvaset definition des images de fond
canMenu=Canvas(root,width=w,height=h,highlightthickness=0) #highlightthickness = contour
canMenu.place(x=0,y=0)

can1=Canvas(root,width=w,height=h,highlightthickness=0)
can2=Canvas(root,width=440,height=759,highlightthickness=0)
canWin=Canvas(root,width=1920,height=1080,highlightthickness=0)
canWin.create_image(0,0, anchor = NW, image= Gagner)
canLose=Canvas(root,width=1920,height=1080,highlightthickness=0)
canLose.create_image(0,0, anchor = NW, image= GameOver)
can2["bg"]="black"

#canvas de deverrouillage
can3=Canvas(root,width=440,height=759,highlightthickness=0)
Candev=Canvas(root,width=365,height=75,highlightthickness=0)
can3["bg"]="black"

#placement des image du deverouillage dans les canvas
Wallpaper=can3.create_image(220,380,image= ImgWallpaper)
BarreDev=Candev.create_image(0,0, anchor = NW,image= ImgBarreDev)
Fleche = Candev.create_image(0,0, anchor = NW, image= ImgFleche)

MenuPr=canMenu.create_image(960,540,image = Menu)
canFond=can1.create_image(960,540,image = FondClear)
Screen=can2.create_image(220,380,image= HomePage)

root.bind('<ButtonPress-1>',Clique) #evenement clic gauche
Candev.bind('<Button-1>',ClicDev) # evevement clic gauche (maintien)
Candev.bind('<B1-Motion>',Drag) # evenement bouton gauche enfonce + deplacement du curseur (hold down)
Candev.bind('<ButtonRelease-1>',win) # evevement clic gauche (relachement)


root.mainloop() #lance le programme
