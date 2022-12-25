import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from tkinter import *
from mlprunner import mlprun


mlp = mlprun()
global answer


root = tk.Tk()

global answer

def input():
    try:
        inputs = torch.tensor([[float(age.get()), float(sex.get()), float(cp.get()), float(bps.get()), float(chol.get()), float(fbs.get()), float(restcg.get()), float(thalach.get()), float(exang.get()), float(oldpeak.get()), float(slope.get()), float(ca.get())]])
        output = mlp.modelin(inputs)
        return str(output)
    except:
        print("null")
        return(1)



def update():
    out.config(text=input())
    print(str(input()))
    print("answer should appear")

age = Entry(root)
age.place(x=50, y=0)
agelabel = tk.Label(root, text="age")
agelabel.place(x=0, y=0)

sex = Entry(root)
sex.place(x=50, y=25)
sexlabel = tk.Label(root, text="sex")
sexlabel.place(x=0, y=25)

cp = Entry(root)
cp.place(x=50, y=50)
cplabel = tk.Label(root, text="cp")
cplabel.place(x=0, y=50)

bps = Entry(root)
bps.place(x=50, y=75)
bpslabel = tk.Label(root, text="trestbps")
bpslabel.place(x=0, y=75)

chol = Entry(root)
chol.place(x=60, y=100)
chollabel = tk.Label(root, text="cholesterol")
chollabel.place(x=0, y=100)
#fbs
fbs = Entry(root)
fbs.place(x=50, y=125)
fbslabel = tk.Label(root, text="fbs")
fbslabel.place(x=0, y=125)
#restecg
restcg = Entry(root)
restcg.place(x=50, y=150)
restcglabel = tk.Label(root, text="restcg")
restcglabel.place(x=0, y=150)
#thalach
thalach = Entry(root)
thalach.place(x=50, y=175)
thalachlabel = tk.Label(root, text="thalach")
thalachlabel.place(x=0, y=175)
#exang
exang = Entry(root)
exang.place(x=50, y=200)
exanglabel = tk.Label(root, text="exang")
exanglabel.place(x=0, y=200)
#oldpeak
oldpeak = Entry(root)
oldpeak.place(x=50, y=225)
oldpeaklabel = tk.Label(root, text="oldpeak")
oldpeaklabel.place(x=0, y=225)
#slope
slope = Entry(root)
slope.place(x=50, y=250)
slopelabel = tk.Label(root, text="slope")
slopelabel.place(x=0, y=250)
#ca
ca = Entry(root)
ca.place(x=50, y=275)
calabel = tk.Label(root, text="ca")
calabel.place(x=0, y=275)


B = tk.Button(root, text= 'Enter', command=lambda: update())
B.place(x=0, y= 300)
out = tk.Label(root, text="")
out.pack(anchor=tk.CENTER)





root.mainloop()