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
from tkintergraph import createplot
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from string import ascii_letters
import seaborn as sns
import matplotlib.pyplot as plt



class genericframe(ctk.CTkFrame):

    def __init__(self, *args, headername='frame', **kwargs):
        super().__init__(*args, **kwargs)



        self.tabview = ctk.CTkTabview(self, height=400, width=1870)
        self.tabview.pack()
        #self.tabview.grid_propagate(False)

        self.tabview.add("Neural Network")
        self.tabview.add("Data")






    def createnninputframe(self):
        self.yoffset = 320
        self.xoffset = 40

        self.inputframe = ctk.CTkFrame(self.tabview.tab("Neural Network"), height=320, width=650, corner_radius=15)
        self.inputframe.grid_propagate(False)
        self.inputframe.grid(row=0, column=0, pady=20, padx=20)


        self.age = ctk.CTkEntry(self.inputframe)
        self.age.grid(row=1, column=1, pady=5, sticky=W)
        self.agelabel = ctk.CTkLabel(self.inputframe, text="age", font=("Arial", 20))
        self.agelabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)  # place(x=self.xoffset, y=self.yoffset)

        self.sex = ctk.CTkOptionMenu(self.inputframe, values=['Male', 'Female'])  # CTkEntry(root)
        self.sex.grid(row=2, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 30)
        self.sexlabel = ctk.CTkLabel(self.inputframe, text="sex", font=("Arial", 20))
        self.sexlabel.grid(row=2, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 30)

        self.cp = ctk.CTkOptionMenu(self.inputframe, values=['typical angina', 'atypical angina', 'non-anginal pain',
                                                  'asymptomatic'])  # CTkEntry(self)
        self.cp.grid(row=1, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 60)
        self.cplabel = ctk.CTkLabel(self.inputframe, text="chest pain type", font=("Arial", 20))
        self.cplabel.grid(row=1, column=3, padx=15, pady=5, sticky=E)  # (x=self.xoffset, y=self.yoffset + 60)
        CreateToolTip(self.inputframe,
                      "Type of chest pain: \n Value 1: typical angina, \nValue 2: atypical angina, \nValue 3: non-anginal pain, \nValue 4: asymptomatic",
                      row=1, column=5, padx=8, pady=5)

        self.bps = ctk.CTkEntry(self.inputframe)
        self.bps.grid(row=2, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 90)
        self.bpslabel = ctk.CTkLabel(self.inputframe, text="bps at rest", font=("Arial", 20))
        self.bpslabel.grid(row=2, column=3, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 90)
        #cholestorol
        self.chol = ctk.CTkEntry(self.inputframe)
        self.chol.grid(row=3, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 120)
        self.chollabel = ctk.CTkLabel(self.inputframe, text="cholesterol", font=("Arial", 20))
        self.chollabel.grid(row=3, column=3, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 120)
        # fbs
        self.fbs = ctk.CTkCheckBox(self.inputframe, onvalue=1, offvalue=0,
                                   text='')  # CTkOptionMenu(root, values=["False", "True"])#ctk.CTkEntry(root)
        self.fbs.grid(row=3, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 150)
        self.fbslabel = ctk.CTkLabel(self.inputframe, text="fbs", font=("Arial", 20))
        self.fbslabel.grid(row=3, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 150)
        # restecg
        self.restcg = ctk.CTkOptionMenu(self.inputframe, values=["normal", "ST-T wave abnormality", "probable or definite left ventricular hypertrophy by Estes' criteria"])#CTkEntry(self.inputframe)
        self.restcg.grid(row=4, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 180)
        self.restcglabel = ctk.CTkLabel(self.inputframe, text="rest ecg", font=("Arial", 20))
        self.restcglabel.grid(row=4, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 180)
        # thalach
        self.thalach = ctk.CTkEntry(self.inputframe)
        self.thalach.grid(row=4, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 210)
        self.thalachlabel = ctk.CTkLabel(self.inputframe, text="max rate", font=("Arial", 20))
        self.thalachlabel.grid(row=4, column=3, padx=20, pady=5,
                               sticky=W)  # place(x=self.xoffset, y=self.yoffset + 210)
        # exang
        self.exang = ctk.CTkCheckBox(self.inputframe, onvalue=1, offvalue=0, text='')  # CTkEntry(root)
        self.exang.grid(row=5, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 240)
        self.exanglabel = ctk.CTkLabel(self.inputframe, text="agina", font=("Arial", 20))
        self.exanglabel.grid(row=5, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 240)
        CreateToolTip(self.inputframe, "Whether the patient has exercise induced angina", row=5, column=4, padx=8, pady=5)
        # oldpeak
        self.oldpeak = ctk.CTkEntry(self.inputframe)
        self.oldpeak.grid(row=5, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 270)
        self.oldpeaklabel = ctk.CTkLabel(self.inputframe, text="ST depression", font=("Arial", 20))
        self.oldpeaklabel.grid(row=5, column=3, padx=20, pady=5,
                               sticky=W)  # place(x=self.xoffset, y=self.yoffset + 270)
        CreateToolTip(self.inputframe, "The ST depression induced by exercise relative to rest", row=5, column=5, padx=8, pady=5)

        # slope
        self.slope = ctk.CTkEntry(self.inputframe)
        self.slope.grid(row=6, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 300)
        self.slopelabel = ctk.CTkLabel(self.inputframe, text="slope", font=("Arial", 20))
        self.slopelabel.grid(row=6, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 300)
        CreateToolTip(self.inputframe, "The ST segment shift relative to exercise-induced increments in heart rate", row=6,
                      column=2, padx=8, pady=5)
        # ca
        self.ca = ctk.CTkEntry(self.inputframe)
        self.ca.grid(row=6, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 330)
        self.calabel = ctk.CTkLabel(self.inputframe, text="major vessels", font=("Arial", 20))
        self.calabel.grid(row=6, column=3, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 330)
        CreateToolTip(self.inputframe, "Number of major vessels colored by flourosopy", row=6, column=5, padx=8, pady=5)

        self.B = ctk.CTkButton(self.inputframe, text='Enter', command=lambda: self.updateoutput())
        self.B.grid(row=7, column=3, padx=20, pady=5)#place(x=self.xoffset + 40, y=self.yoffset + 360)

    def getinputs(self):
        gpp = self.sex.get()
        fbsvar = self.fbs.get()
        cptype = self.cp.get()
        cg = self.restcg.get()
        mlp = mlprun()
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
            cptype = 3


        if cg == "normal":
            cg=0
        if cg== 'ST-T wave abnormality':
            cg=1
        if cg== "probable or definite left ventricular hypertrophy by Estes' criteria":
            cg=2
        try:
            tensor = torch.tensor([[float(self.age.get()), float(gpp), float(cptype), float(self.bps.get()), float(self.chol.get()),
                  float(fbsvar), float(cg), float(self.thalach.get()), float(self.exang.get()),
                  float(self.oldpeak.get()), float(self.slope.get()), float(self.ca.get())]], dtype=torch.float)

            return mlp.modelin(tensor)
        except:
            print("issue")
            #print(self.tensor)
            exit(1)

    def creatennoutputframe(self):
        self.outputframe = ctk.CTkFrame(self.tabview.tab("Neural Network"), corner_radius=15)
        self.outputframe.grid(row=0, column=1, pady=20, padx=20)
        self.outputl = ctk.CTkLabel(self.outputframe, text="this to be fixed", font=("Comic Sans", 20))
        self.outputl.grid(row=0, column=0, pady=20, padx=20)

    def updateoutput(self):
        output = str(self.getinputs())

        if output == "tensor([0])":
            self.outputl.configure(text="Heart disease unlikely")
            print(output)
        elif output == "tensor([1])":
            self.outputl.configure(text="Heart disease likely")
            print(output)
        else:
            print(output)
            print("error")
            exit(1)

    def createdatainputs(self):

        self.datainputframe = ctk.CTkFrame(self.tabview.tab("Data"), height=320, width=500, corner_radius=15)
        self.datainputframe.grid_propagate(False)
        self.datainputframe.grid(row=0, column=0, pady=20, padx=20)

        self.xinputlabel = ctk.CTkLabel(self.datainputframe, text="X axis", font=("Comic Sans", 20))
        self.xinputlabel.grid(row=1, column=0, pady=10, padx=10)
        self.yinputlabel = ctk.CTkLabel(self.datainputframe, text="Y axis", font=("Comic Sans", 20))
        self.yinputlabel.grid(row=1, column=3, pady=10, padx=10)

        self.xinput = ctk.CTkOptionMenu(self.datainputframe, values=["age",'sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca'])#ctk.CTkEntry(self.datainputframe)
        self.xinput.grid(row=2, column=0, pady=10, padx=10)
        self.yinput = ctk.CTkOptionMenu(self.datainputframe, values=["age",'sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca'])#ctk.CTkEntry(self.datainputframe)
        self.yinput.grid(row=2, column=3, pady=10, padx=10)

        self.databutton = ctk.CTkButton(self.datainputframe, text="Enter", font=("Comic Sans", 20), command=lambda: self.updateoutputs())
        self.databutton.grid(row=3, column=2, pady=10)

    def getdatainputs(self):
        outputx = str(self.xinput.get())
        outputy = str(self.yinput.get())

        print(outputx, outputy)
        return outputx, outputy

    def updateoutputs(self):

        x, y = self.getdatainputs()

        self.dataoutputframe = ctk.CTkFrame(self.tabview.tab("Data"), corner_radius=15)
        self.dataoutputframe.grid(row=0, column=1, pady=20, padx=20)

        self.dataouttitle = ctk.CTkLabel(self.dataoutputframe, text=f'{y} by {x}')
        self.dataouttitle.pack()

        fig = createplot(x, y)

        canvas = FigureCanvasTkAgg(fig, master=self.dataoutputframe)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack()
