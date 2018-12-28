from tkinter import *
from PIL import Image, ImageTk
import winsound
import time

def Fav(n,can2,Screen,Photo_Fav):
    n=23#change la variable n
    can2.itemconfig(Screen,image=Photo_Fav) #change limage du telephone
    return(n)#retourne dans le programme principale le n qui a changer

def FeuxArtifice(n,can2,Screen,Photo_FeuxArtifice):
    n=17
    can2.itemconfig(Screen,image=Photo_FeuxArtifice)
    return(n)

def DarkVador(n,can2,Screen,Photo_DarkVador):
    n=17
    can2.itemconfig(Screen,image=Photo_DarkVador)
    return(n)

def Selfie(n,can2,Screen,Photo_Selfie):
    n=17
    can2.itemconfig(Screen,image=Photo_Selfie)
    return(n)

def Insecte(n,can2,Screen,Photo_Insecte):
    n=17
    can2.itemconfig(Screen,image=Photo_Insecte)
    return(n)

def Code(n,can2,Screen,Photo_Code):
    n=17
    can2.itemconfig(Screen,image=Photo_Code)
    return(n)

def Chat(n,can2,Screen,Photo_Chat):
    n=17
    can2.itemconfig(Screen,image=Photo_Chat)
    return(n)

def Nourriture(n,can2,Screen,Photo_Nourriture):
    n=17
    can2.itemconfig(Screen,image=Photo_Nourriture)
    return(n)
