import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from tkinter import *
from mlprunner import mlprun
import customtkinter as ctk
from PIL import Image
from hovertooltip import CreateToolTip


class inputs(ctk.CTkFrame):
    def __init__(self, *args, headername='inputsframe', **kwargs):

        self.buttonpress=False
        def changevalue():
            self.buttonpress = True


        super().__init__(*args, **kwargs)

        self.headername = headername
        self.yoffset = 320
        self.xoffset = 40
        self.mlp = mlprun()

        self.tabview = ctk.CTkTabview(self)



        #self.title = ctk.CTkLabel(self, text=headername, font=("Comic Sans", 25))
        #self.title.grid(row=0, column = 2, pady=20, padx=20)

        self.age = ctk.CTkEntry(self)
        self.age.grid(row=1, column=1, pady=5, sticky=W)
        self.agelabel = ctk.CTkLabel(self, text="age", font=("Arial", 20))
        self.agelabel.grid(row=1, column = 0, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset)
        #ageinfo = ctk.CTkLabel(self, image=self.infopng, text="")
        #ageinfo.grid(row=0, column=5)
        #tix.Balloon(self).bind_widget(ageinfo, balloonmsg="Python is an interpreted, high-level and general - purpose programming language")
        #tooltip(ageinfo, "random")
        #b = balloon(self.winfo_toplevel())
        #b.bind_widget(ageinfo, balloonmsg="Some random text")
        #CreateToolTip(ageinfo, text='lets try this')


        self.sex = ctk.CTkOptionMenu(self, values=['Male', 'Female'])  # CTkEntry(root)
        self.sex.grid(row=2, column=1, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 30)
        self.sexlabel = ctk.CTkLabel(self, text="sex", font=("Arial", 20))
        self.sexlabel.grid(row=2, column=0, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 30)

        self.cp = ctk.CTkOptionMenu(self, values=['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])#CTkEntry(self)
        self.cp.grid(row=1, column=4, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 60)
        self.cplabel = ctk.CTkLabel(self, text="chest pain type", font=("Arial", 20))
        self.cplabel.grid(row=1, column=3, padx=20, pady=5, sticky=E)#(x=self.xoffset, y=self.yoffset + 60)
        CreateToolTip(self, "Type of chest pain: \n Value 1: typical angina, \nValue 2: atypical angina, \nValue 3: non-anginal pain, \nValue 4: asymptomatic",
                      row=1, column=5, padx=8, pady=5)

        self.bps = ctk.CTkEntry(self)
        self.bps.grid(row=2, column=4, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 90)
        self.bpslabel = ctk.CTkLabel(self, text="bps at rest", font=("Arial", 20))
        self.bpslabel.grid(row=2, column=3, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 90)

        self.chol = ctk.CTkEntry(self)
        self.chol.grid(row=3, column=4, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 120)
        self.chollabel = ctk.CTkLabel(self, text="cholesterol", font=("Arial", 20))
        self.chollabel.grid(row=3, column=3, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 120)
        # fbs
        self.fbs = ctk.CTkCheckBox(self, onvalue=1, offvalue=0, text='')  # CTkOptionMenu(root, values=["False", "True"])#ctk.CTkEntry(root)
        self.fbs.grid(row=3, column=1, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 150)
        self.fbslabel = ctk.CTkLabel(self, text="fbs", font=("Arial", 20))
        self.fbslabel.grid(row=3, column=0, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 150)
        # restecg
        self.restcg = ctk.CTkEntry(self)
        self.restcg.grid(row=4, column=1, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 180)
        self.restcglabel = ctk.CTkLabel(self, text="rest ecg", font=("Arial", 20))
        self.restcglabel.grid(row=4, column=0, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 180)
        # thalach
        self.thalach = ctk.CTkEntry(self)
        self.thalach.grid(row=4, column=4, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 210)
        self.thalachlabel = ctk.CTkLabel(self, text="max rate", font=("Arial", 20))
        self.thalachlabel.grid(row=4, column=3, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 210)
        # exang
        self.exang = ctk.CTkCheckBox(self, onvalue=1, offvalue=0, text='')  # CTkEntry(root)
        self.exang.grid(row=5, column=1, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 240)
        self.exanglabel = ctk.CTkLabel(self, text="agina", font=("Arial", 20))
        self.exanglabel.grid(row=5, column=0, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 240)
        CreateToolTip(self, "Whether the patient has exercise induced angina", row=5, column=4, padx=8, pady=5)
        # oldpeak
        self.oldpeak = ctk.CTkEntry(self)
        self.oldpeak.grid(row=5, column=4, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 270)
        self.oldpeaklabel = ctk.CTkLabel(self, text="ST depression", font=("Arial", 20))
        self.oldpeaklabel.grid(row=5, column=3, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 270)
        CreateToolTip(self, "The ST depression induced by exercise relative to rest", row=5, column=5, padx=8, pady=5)

        # slope
        self.slope = ctk.CTkEntry(self)
        self.slope.grid(row=6, column=1, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 300)
        self.slopelabel = ctk.CTkLabel(self, text="slope", font=("Arial", 20))
        self.slopelabel.grid(row=6, column=0, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 300)
        CreateToolTip(self, "The ST segment shift relative to exercise-induced increments in heart rate", row=6, column=2, padx=8, pady=5)
        # ca
        self.ca = ctk.CTkEntry(self)
        self.ca.grid(row=6, column=4, pady=5, sticky=W)#place(x=self.xoffset + 100, y=self.yoffset + 330)
        self.calabel = ctk.CTkLabel(self, text="major vessels", font=("Arial", 20))
        self.calabel.grid(row=6, column=3, padx=20, pady=5, sticky=W)#place(x=self.xoffset, y=self.yoffset + 330)
        CreateToolTip(self, "Number of major vessels colored by flourosopy", row=6, column=5, padx=8, pady=5)
        #enter info
        #self.B = ctk.CTkButton(self, text='Enter')#, command= )#lambda: update())
        #self.B.grid(row=7, column=2, padx=20, pady=5)#place(x=self.xoffset + 40, y=self.yoffset + 360)

    def getinputs(self):
        gpp = self.sex.get()
        fbsvar = self.fbs.get()
        cptype = self.cp.get()
        if gpp == 'Male':
            gpp = 1
        if gpp == 'Female':
            gpp = 0


        if fbsvar == "False":
            fbsvar = 0
        if fbsvar == "True":
            fbsvar = 1


        if cptype == 'typical angina':
            cptype = 0
        if cptype == 'atypical angina':
            cptype = 1
        if cptype == 'non-anginal pain':
            cptype = 2
        if cptype == 'asymptomatic':
            cptype=3



        try:
            tensor = torch.tensor([[float(self.age.get()), float(gpp), float(cptype), float(self.bps.get()), float(self.chol.get()),
                                    float(fbsvar), float(self.restcg.get()), float(self.thalach.get()), float(self.exang.get()),
                                    float(self.oldpeak.get()), float(self.slope.get()), float(self.ca.get())]], dtype = torch.float)


            return self.mlp.modelin(tensor)
        except:
            print("null")
            exit(1)

    def getbutton(self):
        return self.buttonpress
