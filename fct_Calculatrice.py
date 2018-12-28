from tkinter import *
from PIL import Image, ImageTk
import winsound
import time

def limite(n,can2,Screen,total): #Limite l'affichage de la calculatrice a 9
    if len(total)>9:
        total="ERROR" #change l'affichage de la calculatrice car trop de caracteres
        clear(n,can2,Screen,total)
        total=""
    else:
        clear(n,can2,Screen,total)

def clear(n,can2,Screen,total): #Supprime l'affichage et le remet avec le nouveau total pour le rafraichir
    can2.delete("affichage")
    can2.create_text(380,235,font=("arial",50),fill='white',text=total,anchor=E,tag="affichage")

def egal(n,can2,total,Calculatrice_Secret,Screen): #verifie la valeur de total pour savoir si le bon mot de passe est rentre
    if total=="63+5":
        total=""
        can2.itemconfig(Screen,image=Calculatrice_Secret) #mene a l'indice
        clear(n,can2,Screen,total)
        return(n)
    else : #mauvais mots de passe
        total="ERROR"
        clear(n,can2,Screen,total)
        total=""
        return(n)

def annuler(n,can2,total,Screen): #vide total
    total=""
    limite(n,can2,Screen,total)
    return(total)

def plus(n,can2,total,Screen): #rajoute "+" au total (pareil pour tout le reste des fonctions)
    total=total+"+"
    limite(n,can2,Screen,total)
    return(total)

def moins(n,can2,total,Screen):
    total=total+"-"
    limite(n,can2,Screen,total)
    return(total)

def multiplier(n,can2,total,Screen):
    total=total+"x"
    limite(n,can2,Screen,total)
    return(total)

def diviser(n,can2,total,Screen):
    total=total+"/"
    limite(n,can2,Screen,total)
    return(total)

def zero(n,can2,total,Screen):
    total=total+"0"
    limite(n,can2,Screen,total)
    return(total)

def un(n,can2,total,Screen):
    total=total+"1"
    limite(n,can2,Screen,total)
    return(total)

def deux(n,can2,total,Screen):
    total=total+"2"
    limite(n,can2,Screen,total)
    return(total)

def trois(n,can2,total,Screen):
    total=total+"3"
    limite(n,can2,Screen,total)
    return(total)

def quatre(n,can2,total,Screen):
    total=total+"4"
    limite(n,can2,Screen,total)
    return(total)

def cinq(n,can2,total,Screen):
    total=total+"5"
    limite(n,can2,Screen,total)
    return(total)

def six(n,can2,total,Screen):
    total=total+"6"
    limite(n,can2,Screen,total)
    return(total)

def sept(n,can2,total,Screen):
    total=total+"7"
    limite(n,can2,Screen,total)
    return(total)

def huit(n,can2,total,Screen):
    total=total+"8"
    limite(n,can2,Screen,total)
    return(total)

def neuf(n,can2,total,Screen):
    total=total+"9"
    limite(n,can2,Screen,total)
    return(total)
