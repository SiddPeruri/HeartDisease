import time

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from tkinter import *
from mlprunner import mlprun
import customtkinter as ctk
from PIL import Image, ImageSequence
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
       # self.dataColumns = ["age",'sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca']
        #self.dataColumns = ["Diagnosis Age",'Sex','Ethnicity Category', 'Mutation Count', 'Abnormal Lymphocyte Percent', 'Atra Exposure', 'Basophils Cell Count', 'Blast Count', 'Platelet count preresection', 'Prior Cancer Diagnosis Occurence']
        self.dataColumns = ["Mutation Count", 'Diagnosis Age', 'Sex', 'Ethnicity Category','Abnormal Lymphocyte Percent','Atra Exposure','Basophils Cell Count','Blast Count','Platelet count preresection', 'Prior Cancer Diagnosis Occurence']
        self.tabview = ctk.CTkTabview(self, height=400, width=400, command=self.onChangeTab)
        self.tabview.pack(padx=5, pady=5)
        #self.tabview.grid_propagate(False)

        self.tabview.add("Neural Network")
        self.tabview.add("Data")

        self.canvas = None
        self.data = None
        self.fig = None
        self.ax = None
        self.plot = None

        self.heartGIFs = []
        heartGIF = Image.open('AML.gif')
        #heartGIF = Image.open('heart.gif')
        for i in range(0,28):    #heartGIF.n_frames):
            imgName = "resources/AML_" + str(i+1) + ".png"  # renamed .png to .JPEG replace heart with AML later;
            self.heartGIFs.append(ctk.CTkImage(light_image=Image.open(imgName), dark_image=Image.open(imgName),size=(180, 180)))
            #time.sleep(2)
    def createnninputframe(self):
        self.yoffset = 320
        self.xoffset = 40

        self.inputframe = ctk.CTkFrame(self.tabview.tab("Neural Network"), height=320, width=800, corner_radius=15)
        self.inputframe.grid_propagate(False)
        self.inputframe.grid(row=0, column=0, pady=5, padx=5)

#Diagnosis Age
        self.age = ctk.CTkEntry(self.inputframe)
        self.age.grid(row=1, column=1, pady=5, sticky=W)
        self.agelabel = ctk.CTkLabel(self.inputframe, text="Age", font=("Arial", 20))
        self.agelabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)  # place(x=self.xoffset, y=self.yoffset)
#Gender/Sex
        self.sex = ctk.CTkOptionMenu(self.inputframe, values=['Male', 'Female'])  # CTkEntry(root)
        self.sex.grid(row=2, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 30)
        self.sexlabel = ctk.CTkLabel(self.inputframe, text="Gender", font=("Arial", 20))
        self.sexlabel.grid(row=2, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 30)
#Prior Cancer (Drop Down) commented as it is not used. Delete later.
        #self.cp = ctk.CTkOptionMenu(self.inputframe, values=['typical angina', 'atypical angina', 'non-anginal pain',
           #                                       'asymptomatic'])  # CTkEntry(self)
        #Prior AML Diagnosis (Cancer Prior)
        # self.cp = ctk.CTkOptionMenu(self.inputframe, values=['Yes', 'No', 'Unknown'])
        # self.cp.grid(row=1, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 60)
        # self.cplabel = ctk.CTkLabel(self.inputframe, text="Prior Cancer", font=("Arial", 20))

#(Basophils cell count (2nd half of the screen)
        # cholestorol (For AML : Platelet Count)
        self.cp = ctk.CTkEntry(self.inputframe)
        self.cp.grid(row=1, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 120)
        self.cplabel = ctk.CTkLabel(self.inputframe, text="Basophils cell count", font=("Arial", 20))
        self.cplabel.grid(row=1, column=3, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 120)
        CreateToolTip(self.inputframe, "Basophils cell count", row=1, column=5, padx=8,pady=5)

#Blast Count
        self.bps = ctk.CTkEntry(self.inputframe)
        self.bps.grid(row=2, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 90)
        self.bpslabel = ctk.CTkLabel(self.inputframe, text="Blast Count", font=("Arial", 20))
        self.bpslabel.grid(row=2, column=3, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 90)
        CreateToolTip(self.inputframe, "Blast Count)", row=2, column=5, padx=8,pady=5)

        #cholestorol (For AML : Platelet Count)
        self.chol = ctk.CTkEntry(self.inputframe)
        self.chol.grid(row=3, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 120)
        self.chollabel = ctk.CTkLabel(self.inputframe, text="Platelet Count", font=("Arial", 20))
        self.chollabel.grid(row=3, column=3, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 120)
        CreateToolTip(self.inputframe, "Platelets count in blood", row=3, column=5, padx=8,pady=5)

        # fbs ; Prior Cancer  renamed from fbs to fbs_pc
        self.fbs_pc = ctk.CTkCheckBox(self.inputframe, onvalue=1, offvalue=0,
                                   text='')  # CTkOptionMenu(root, values=["False", "True"])#ctk.CTkEntry(root)
        self.fbs_pc.grid(row=3, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 150)
        self.fbslabel_pc = ctk.CTkLabel(self.inputframe, text="Prior Cancer", font=("Arial", 20))
        self.fbslabel_pc.grid(row=3, column=0, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 150)
        CreateToolTip(self.inputframe, "Prior Cancer Detected", row=3, column=2, padx=8,pady=5)
        # restecg (Mutation Count)
        #self.restcg = ctk.CTkOptionMenu(self.inputframe, values=["normal", "ST-T wave abnormal", "left ventricular hypertrophy"])#CTkEntry(self.inputframe)
        #self.restcg.grid(row=4, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 180)
        #self.restcglabel = ctk.CTkLabel(self.inputframe, text="Mutation Count", font=("Arial", 20))
        #self.restcglabel.grid(row=4, column=0, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 180)
        #CreateToolTip(self.inputframe, "Mutation Count", row=4, column=2, padx=8,pady=5)

        # CTkEntry(self.inputframe)
        self.restcg = ctk.CTkEntry(self.inputframe)
        self.restcg.grid(row=4, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 180)
        self.restcglabel = ctk.CTkLabel(self.inputframe, text="Mutation Count", font=("Arial", 20))
        self.restcglabel.grid(row=4, column=0, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 180)
        CreateToolTip(self.inputframe, "Mutation Count", row=4, column=2, padx=8,pady=5)


        # thalach (#Abnormal Lymphocyte %)
        self.thalach = ctk.CTkEntry(self.inputframe)
        self.thalach.grid(row=4, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 210)
        self.thalachlabel = ctk.CTkLabel(self.inputframe, text="Abnormal Lymphocyte %", font=("Arial", 20))
        self.thalachlabel.grid(row=4, column=3, padx=10, pady=5,sticky=W)  # place(x=self.xoffset, y=self.yoffset + 210)
        CreateToolTip(self.inputframe, "Abnormal Lymphocyte Percent", row=4, column=5, padx=8,pady=5)

        # exang (can reuse for Atra Exposure...>
        self.exang = ctk.CTkCheckBox(self.inputframe, onvalue=1, offvalue=0, text='')  # CTkEntry(root)
        self.exang.grid(row=5, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 240)
        self.exanglabel = ctk.CTkLabel(self.inputframe, text="Atra Exposure", font=("Arial", 20))
        self.exanglabel.grid(row=5, column=0, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 240)
        CreateToolTip(self.inputframe, "Breathing issues", row=5, column=2, padx=8, pady=5)

        # slope (Ethnicity Category)
        #self.slope = ctk.CTkEntry(self.inputframe)
        self.slope = ctk.CTkOptionMenu(self.inputframe, values=['Not Hispanic OR Latino','Hispanic OR Latino', 'Asian','OTHERS'])  # CTkEntry(self)
        self.slope.grid(row=6, column=1, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 300)
        self.slopelabel = ctk.CTkLabel(self.inputframe, text="Ethnicity Category", font=("Arial", 20))
        self.slopelabel.grid(row=6, column=0, padx=10, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 300)
        CreateToolTip(self.inputframe,"Ethnicity: \n Value 1: Hispanic, \nValue 2: Latino, \nValue 3: Asian, \nValue 4: Others", row=6,column=2, padx=8, pady=5)

        # ca (commented out due to removal of variable in the model
        # self.ca = ctk.CTkOptionMenu(self.inputframe, values=['0', '1', '2', '3']) #ctk.CTkEntry(self.inputframe)
        # self.ca.grid(row=6, column=4, pady=5, sticky=W)  # place(x=self.xoffset + 100, y=self.yoffset + 330)
        # self.calabel = ctk.CTkLabel(self.inputframe, text="extra variable", font=("Arial", 20))
        # self.calabel.grid(row=6, column=3, padx=20, pady=5, sticky=W)  # place(x=self.xoffset, y=self.yoffset + 330)
        # CreateToolTip(self.inputframe, "Number of major vessels seen by flourosopy. \nNormal person has 3 major vessels", row=6, column=5, padx=8, pady=5)

        self.B = ctk.CTkButton(self.inputframe, text='Enter', command=lambda: self.updateoutput())
        self.B.grid(row=7, column=3, padx=20, pady=5)#place(x=self.xoffset + 40, y=self.yoffset + 360)

    def getinputs(self):
        gpp = self.sex.get()
        fbsvar = self.fbs_pc.get()
        cptype = self.cp.get()
        #cg = self.restcg.get()
        cgnum = self.restcg.get()
        #cgnum =0
        exangvar= self.exang.get()
        slopevar = self.slope.get()

        mlp = mlprun()
        if gpp == 'Male':
            gpp = 1
        if gpp == 'Female':
            gpp = 0

        if fbsvar == "False" or fbsvar == 0:
            fbsvar = 0
        if fbsvar == "True" or fbsvar == 1:
            fbsvar = 1

        if exangvar == "False" or exangvar == 0:
            exangvar = 0
        if exangvar == "True" or exangvar == 1:
            exangvar = 1

#commented the code as no heart animation
        # if cptype == 'typical angina':
        #     cptype = 0
        # if cptype == 'atypical angina':
        #     cptype = 1
        # if cptype == 'non-anginal pain':
        #     cptype = 2
        # if cptype == 'asymptomatic':
        #     cptype = 3

    # if cptype == "0"
    #         cptype = 1
    # if cptype > 10
    #         cptype =2

        # commented code as CG in AML model is a value
        # if cg == "normal":
        #     cgnum=0
        # if cg== 'ST-T wave abnormal':
        #     cgnum=1
        # if cg== "left ventricular hypertrophy":
        #     cgnum=2
        #write for Slope varible used for Ethnicity

        if slopevar == "Not Hispanic OR Latino":
            slopevar = 0
        else: slopevar =1 # Hispanic OR Latino', 'Asian','OTHERS')


        # if cg== "left ventricular hypertrophy":
        #     cgnum=2

        try:
            #tensor = torch.tensor([[float(self.age.get()), float(gpp), float(cptype), float(self.bps.get()), float(self.chol.get()),float(fbsvar), float(cgnum), float(self.thalach.get()), float(self.exangvar.get()),float(slopevar)]], dtype=torch.float)
            tensor = torch.tensor([[float(cgnum),float(self.age.get()),float(gpp),float(slopevar),float(self.thalach.get()), float(exangvar),float(self.cp.get()), float(self.bps.get()), float(self.chol.get()),float(fbsvar)]], dtype=torch.float)

            #'Mutation Count', 'Diagnosis Age', 'Sex', 'Ethnicity Category', 'Abnormal Lymphocyte Percent', 'Atra Exposure', 'Basophils Cell Count', 'Blast Count', 'Platelet count preresection', 'Prior Cancer Diagnosis Occurence'
            #update code to include slope.get to slopevar
            # tensor = torch.tensor(
            #     [[float(self.age.get()), float(gpp), float(cptype), float(self.bps.get()), float(self.chol.get()),
            #       float(fbsvar), float(cgnum), float(self.thalach.get()), float(self.exangvar.get()),
            #       float(self.oldpeak.get()), float(self.slope.get()), float(self.ca.get())]], dtype=torch.float)
            #print (tensor.data)  # To be removed later.
            return mlp.modelin(tensor)
        except:
            print("issue")
            #print(self.tensor)
            #exit(1)
            return "Please provide all values"

    def creatennoutputframe(self):
        self.outputframe = ctk.CTkFrame(self.tabview.tab("Neural Network"), corner_radius=15)
        self.outputframe.grid(row=0, column=1, pady=5, padx=5)

        self.outputl = ctk.CTkLabel(self.outputframe, text="Please provide all inputs", font=("Comic Sans", 20))
        self.outputl.grid(row=0, column=0, pady=5, padx=5)
#added two lines to display AML.GIF
        #self.heartAnimation = ctk.CTkLabel(self.outputframe, text='', image="AML.GIF")
        #self.heartAnimation.grid(row=1, column=0, pady=5, padx=5)
        self.heartAnimation = ctk.CTkLabel(self.outputframe, text='', image=self.heartGIFs[0])
        self.heartAnimation.grid(row=1, column=0, pady=5, padx=5)

    def animateHeart(self, indx):
        if indx >= 0 and indx<=28:   #len(self.heartGIFs): commented due to lack of GIFs
            self.heartAnimation.configure(True, image=self.heartGIFs[indx])
            indx += 1
        else:
            indx = 0
        self.after(27, self.animateHeart, indx)

    def updateoutput(self):
        output = str(self.getinputs())
        print(output)
        if output == "tensor([0])":
            self.outputl.configure(text="AML disease unlikely")
            print(output)
        elif output == "tensor([1])":
            self.outputl.configure(text="AML disease likely")
            print(output)
        else:
            print(output)
            print("error")
            #exit(1)
            self.outputl.configure(text=output)

    def onChangeTab(self):
        self.updateoutputs()

    def createdatainputs(self):

        self.dataframe = ctk.CTkFrame(self.tabview.tab("Data"), width=800, height=600, corner_radius=15)
        self.dataframe.grid_propagate(False)
        self.dataframe.grid(row=0, column=0, pady=5, padx=5)

        self.datainputframe = ctk.CTkFrame(self.dataframe, corner_radius=15)
        self.datainputframe.grid(row=0, column=0, pady=5, padx=5)

        self.xinputlabel = ctk.CTkLabel(self.datainputframe, text="X axis", font=("Comic Sans", 20))
        self.xinputlabel.grid(row=1, column=0, pady=10, padx=10)
        self.yinputlabel = ctk.CTkLabel(self.datainputframe, text="Y axis", font=("Comic Sans", 20))
        self.yinputlabel.grid(row=1, column=3, pady=10, padx=10)

        self.xinput = ctk.CTkOptionMenu(self.datainputframe, values=self.dataColumns,command=self.updateX)
        self.xinput.grid(row=1, column=1, pady=10, padx=10)
        self.yinput = ctk.CTkOptionMenu(self.datainputframe, values=self.dataColumns,command=self.updateY)
        self.yinput.grid(row=1, column=4, pady=10, padx=10)

        #self.databutton = ctk.CTkButton(self.datainputframe, text="Enter", font=("Comic Sans", 20), command=lambda: self.updateoutputs())
        #self.databutton.grid(row=3, column=2, pady=10)

        self.dataoutputframe = ctk.CTkFrame(self.dataframe, corner_radius=15)
        self.dataoutputframe.grid(row=1, column=0, pady=5, padx=5)

    def updateX(self, indx):
        self.updateoutputs()

    def updateY(self, indx):
        self.updateoutputs()

    def updateoutputs(self):
        x = str(self.xinput.get())
        y = str(self.yinput.get())
        print(x, y)
        activeTab = self.tabview.get()
        if activeTab == 'Data':
            sns.set(style="white")
            if self.data is None:
                # Get data
                self.data = pd.read_csv("aml_clinical_data.csv")  # replaced parameter with heart.csv

            if self.fig is not None:
                plt.cla()
                plt.close(self.fig)

            # Set up the matplotlib figure
            self.fig, self.ax = plt.subplots(figsize=(7, 5))
            # Draw the dot plot
            # sns.stripplot(data=self.data, x=x, y=y, hue="target")
            heart_dis = self.data.eval("target == 1").rename("AML_disease")     #replaced hear disease with AML
            self.plot = sns.scatterplot(data=self.data, x=x, y=y, hue=heart_dis)
            # fig = createplot(x=x, y=y, self.data)

            if self.canvas is None:
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.dataoutputframe)  # A tk.DrawingArea.
                self.canvas.get_tk_widget().pack()
                self.canvas.draw()
            else:
                self.canvas.figure = self.fig
                self.canvas.draw()

