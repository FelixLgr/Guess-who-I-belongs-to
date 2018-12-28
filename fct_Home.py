from tkinter import *
from PIL import Image, ImageTk
import winsound
import time

def retour(n,can2,total,Screen,HomePage):
    n=2 #change la variable n
    total="" #remet a zero le total de la calculette
    can2.itemconfig(Screen,image=HomePage) #change limage du telephone
    can2.delete("artiste")#supprime le texte artiste
    can2.delete("titre")#supprime le texte titre
    can2.delete("affichage")#supprime le texte affichage
    can2.delete("heure")#supprime le texte heure
    can2.delete("Point")#supprime le texte point (si Pong est dans le programme principale)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")#met a jour l'heure
    return(n,total)#retourne dans le programme principale le n qui a changer et le total

def mail(n,can2,Screen,Mails):
    n=5
    can2.itemconfig(Screen,image=Mails)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)#retourne dans le programme principale le n qui a changer

def facebook(n,can2,Screen,Facebook):
    n=8
    can2.itemconfig(Screen,image=Facebook)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def twitter(n,can2,Screen,Twitter):
    n=10
    can2.itemconfig(Screen,image=Twitter)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")

def tinder(n,can2,Screen,Tinder):
    n=9
    can2.itemconfig(Screen,image=Tinder)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def appstore(n,can2,Screen,AppStore):
    n=6
    can2.itemconfig(Screen,image=AppStore)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def chrome(n,can2,Screen,Chrome):
    n=7
    can2.itemconfig(Screen,image=Chrome)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def horloge(n,can2,Screen,Horloge):
    n=11
    can2.itemconfig(Screen,image=Horloge)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def calculatrice(n,can2,Screen,Calculatrice_Home):
    n=3
    can2.itemconfig(Screen,image=Calculatrice_Home)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def message(n,can2,Screen,Messages_Home):
    n=4
    can2.itemconfig(Screen,image=Messages_Home)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def musique(n,can2,Screen,Musiques):
    n=12
    can2.itemconfig(Screen,image=Musiques)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def photo(n,can2,Screen,Photo_Home):
    n=13
    can2.itemconfig(Screen,image=Photo_Home)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def appareilphoto(n,can2,Screen,AppareilPhoto):
    n=14
    can2.itemconfig(Screen,image=AppareilPhoto)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def reglages(n,can2,Screen,Reglages):
    n=16
    can2.itemconfig(Screen,image=Reglages)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def telephone(n,can2,Screen,Telephone):
    n=33
    can2.itemconfig(Screen,image=Telephone)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def contact(n,can2,Screen,Contact):
    n=18
    can2.itemconfig(Screen,image=Contact)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='white',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def calendrier(n,can2,Screen,Calendrier):
    n=19
    can2.itemconfig(Screen,image=Calendrier)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)

def note(n,can2,Screen,BlocNotes):
    n=32
    can2.itemconfig(Screen,image=BlocNotes)
    can2.create_text(205,8,font=("arial",11,"bold"),fill='black',text=time.strftime('%H:%M',time.localtime()),anchor=NW,tag="heure")
    return(n)
