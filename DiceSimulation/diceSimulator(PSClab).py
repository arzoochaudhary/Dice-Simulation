# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:12:16 2021

@author: Arzoo
"""
import random
from PIL import Image, ImageTk
import tkinter

root=tkinter.Tk()
root.geometry('400x400')
root.title('Dice Simulation')

line=tkinter.Label(root,text="")
line.pack()

heading1=tkinter.Label(root,text='Dice Simulator',fg='white',bg='black',font='100')
heading1.pack()
heading1.config(font=("",44))
heading1.config(width=200)
line=tkinter.Label(root,text="")
line.pack()



"""
alldice=ImageTk.PhotoImage(Image.open("C:/Users/Arzoo/Desktop/DiceSimulation/allDice.png"))
label=tkinter.Label(root,image=alldice)
label.image=alldice
"""

dice = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open('C:/Users/Arzoo/Desktop/DiceSimulation/'+random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.place(anchor='sw')

# packing a widget in the parent widget 
ImageLabel.pack( side=tkinter.LEFT,expand=True)

def roll_dice():
    DiceImage = ImageTk.PhotoImage(Image.open('C:/Users/Arzoo/Desktop/DiceSimulation/'+random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image=DiceImage
button=tkinter.Button(root,text="Roll the normal Dice",fg='black',bg='white',height=2,width=15,command=roll_dice)
button.pack(side=tkinter.LEFT,expand=True)

dice1 = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png','6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage1 = ImageTk.PhotoImage(Image.open('C:/Users/Arzoo/Desktop/DiceSimulation/'+random.choice(dice1)))

# construct a label widget for image
ImageLabel1 = tkinter.Label(root, image=DiceImage1)
ImageLabel1.image = DiceImage1

# packing a widget in the parent widget 
ImageLabel1.pack(side=tkinter.RIGHT, expand=True)

def roll_dice1():
    DiceImage1 = ImageTk.PhotoImage(Image.open('C:/Users/Arzoo/Desktop/DiceSimulation/'+random.choice(dice1)))
    ImageLabel1.configure(image=DiceImage1)
    ImageLabel1.image=DiceImage1
button1=tkinter.Button(root,text="Roll the Dice with high prob of 6",fg='black',bg='white',height=2,command=roll_dice1)
button1.pack(side=tkinter.RIGHT,expand=True)
root.mainloop()
