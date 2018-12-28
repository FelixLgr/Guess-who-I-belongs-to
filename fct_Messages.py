from tkinter import *
from PIL import Image, ImageTk
import winsound
import time


def Luke(n,can2,Screen,Messages_Luke): #mene a la conversation avec Luke (pareil pour le reste des conversations)
    n=5#change la variable n
    can2.itemconfig(Screen,image=Messages_Luke)#change l'image du telephone
    return(n)#retourne dans le programme principale le n qui a changer

def Maman(n,can2,Screen,Messages_Maman):
    n=5
    can2.itemconfig(Screen,image=Messages_Maman)
    return(n)

def Papa(n,can2,Screen,Messages_Papa):
    n=5
    can2.itemconfig(Screen,image=Messages_Papa)
    return(n)

def Patrice(n,can2,Screen,Messages_Patrice):
    n=5
    can2.itemconfig(Screen,image=Messages_Patrice)
    return(n)

def Cusmar(n,can2,Screen,Messages_Cusmar):
    n=5
    can2.itemconfig(Screen,image=Messages_Cusmar)
    return(n)

def Alex(n,can2,Screen,Messages_Alex):
    n=5
    can2.itemconfig(Screen,image=Messages_Alex)
    return(n)

def BackMessages(n,can2,Screen,Messages_Home): #permet de revenir a l'ecran d'accueil des messages
    n=4
    can2.itemconfig(Screen,image=Messages_Home)
    return(n)
