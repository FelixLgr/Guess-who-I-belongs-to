from tkinter import *
from PIL import Image, ImageTk

def AccepterWin(n,can1,can2,canWin): #Mene a l'ecran de victoire
    n=42#change la variable n
    can1.destroy() #detruit le canvas 1
    can2.destroy() #detruit le canvas 2
    canWin.place(x=0,y=0) #place le canvas win au coordonees 0 0
    return(n)#retourne dans le programme principale le n qui a changer

def AccepterLose(n,can1,can2,canLose): #Mene a l'ecran de defaite quand le mauvais personnage est valide
    n=42#change la variable n
    n=43
    can1.destroy() #detruit le canvas 1
    can2.destroy() #detruit le canvas 2
    canLose.place(x=0,y=0)  #place le canvas lose au coordonees 0 0
    return(n)#retourne dans le programme principale le n qui a changer

def RefuserJawad(can1,Cacher):
    can1.create_image(68,105, anchor = NW,image= Cacher)#crée une image par dessus les personnages pour les cacher

def RefuserPeter(can1,Cacher):
    can1.create_image(68,340, anchor = NW,image= Cacher)

def RefuserPatrick(can1,Cacher):
    can1.create_image(68,575, anchor = NW,image= Cacher)

def RefuserJean(can1,Cacher):
    can1.create_image(68,810, anchor = NW,image= Cacher)

def RefuserLionel(can1,Cacher):
    can1.create_image(1652,105, anchor = NW,image= Cacher)

def RefuserBrandon(can1,Cacher):
    can1.create_image(1652,340, anchor = NW,image= Cacher)

def RefuserNicolas(can1,Cacher):
    can1.create_image(1652,575, anchor = NW,image= Cacher)

def RefuserFrancois(can1,Cacher):
    can1.create_image(1652,810, anchor = NW,image= Cacher)
