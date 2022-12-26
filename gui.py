import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from tkinter import *
from mlprunner import mlprun
import customtkinter as ctk


mlp = mlprun()
global answer


root = ctk.CTk()

root.geometry("1920x1080")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
yoffset=320
xoffset = 40

def input():
    gpp = sex.get()
    if gpp == 'M' or gpp == 'm':
        gpp = 1
    if gpp == 'F' or gpp == 'f':
        gpp = 0
    try:
        inputs = torch.tensor([[float(age.get()), float(gpp), float(cp.get()), float(bps.get()), float(chol.get()), float(fbs.get()), float(restcg.get()), float(thalach.get()), float(exang.get()), float(oldpeak.get()), float(slope.get()), float(ca.get())]])
        output = mlp.modelin(inputs)
        return str(output)
    except:
        print("null")
        return(1)



def update():
    answer = str(input())
    if answer == 'tensor([0])':
        answer = 'Heart disease unlikely'
    if answer == 'tensor([1])':
        answer = 'Heart disease likely'
    out.configure(text=answer)
    print(str(input()))
    print("answer should appear")

age = ctk.CTkEntry(root)
age.place(x=xoffset+100, y=yoffset)
agelabel = ctk.CTkLabel(root, text="age", font=("Arial", 20))
agelabel.place(x=xoffset, y=yoffset)

sex = ctk.CTkEntry(root)
sex.place(x=xoffset+100, y=yoffset+30)
sexlabel = ctk.CTkLabel(root, text="sex", font=("Arial", 20))
sexlabel.place(x=xoffset, y=yoffset+30)

cp = ctk.CTkEntry(root)
cp.place(x=xoffset+100, y=yoffset+60)
cplabel = ctk.CTkLabel(root, text="cp", font=("Arial", 20))
cplabel.place(x=xoffset, y=yoffset+60)

bps = ctk.CTkEntry(root)
bps.place(x=xoffset+100, y=yoffset+90)
bpslabel = ctk.CTkLabel(root, text="trestbps", font=("Arial", 20))
bpslabel.place(x=xoffset, y=yoffset+90)

chol = ctk.CTkEntry(root)
chol.place(x=xoffset+100, y=yoffset+120)
chollabel = ctk.CTkLabel(root, text="cholesterol", font=("Arial", 20))
chollabel.place(x=xoffset, y=yoffset+120)
#fbs
fbs = ctk.CTkEntry(root)
fbs.place(x=xoffset+100, y=yoffset+150)
fbslabel = ctk.CTkLabel(root, text="fbs", font=("Arial", 20))
fbslabel.place(x=xoffset, y=yoffset+150)
#restecg
restcg = ctk.CTkEntry(root)
restcg.place(x=xoffset+100, y=yoffset+180)
restcglabel = ctk.CTkLabel(root, text="restcg", font=("Arial", 20))
restcglabel.place(x=xoffset, y=yoffset+180)
#thalach
thalach = ctk.CTkEntry(root)
thalach.place(x=xoffset+100, y=yoffset+210)
thalachlabel = ctk.CTkLabel(root, text="thalach", font=("Arial", 20))
thalachlabel.place(x=xoffset, y=yoffset+210)
#exang
exang = ctk.CTkEntry(root)
exang.place(x=xoffset+100, y=yoffset+240)
exanglabel = ctk.CTkLabel(root, text="exang", font=("Arial", 20))
exanglabel.place(x=xoffset, y=yoffset+240)
#oldpeak
oldpeak = ctk.CTkEntry(root)
oldpeak.place(x=xoffset+100, y=yoffset+270)
oldpeaklabel = ctk.CTkLabel(root, text="oldpeak", font=("Arial", 20))
oldpeaklabel.place(x=xoffset, y=yoffset+270)
#slope
slope = ctk.CTkEntry(root)
slope.place(x=xoffset+100, y=yoffset+300)
slopelabel = ctk.CTkLabel(root, text="slope", font=("Arial", 20))
slopelabel.place(x=xoffset, y=yoffset+300)
#ca
ca = ctk.CTkEntry(root)
ca.place(x=xoffset+100, y=yoffset+330)
calabel = ctk.CTkLabel(root, text="ca", font=("Arial", 20))
calabel.place(x=xoffset, y=yoffset+330)


B = ctk.CTkButton(root, text= 'Enter', command=lambda: update())
B.place(x=xoffset+40, y= yoffset+360)
out = ctk.CTkLabel(root, text="", font=("Arial", 20))
out.pack(anchor=ctk.CENTER, pady=460)





root.mainloop()