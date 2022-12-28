import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from tkinter import *
from mlprunner import mlprun
import customtkinter as ctk
from genericframe import genericframe


mlp = mlprun()
global answer

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Heart disease prediction app(Science fair 2022-2023)")
        self.geometry("1920x1080")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.titleWidget = ctk.CTkLabel(self, text="Heart Disease Prediction Science Fair Project 2022-2023", font=("Arial", 25))
        self.titleWidget.grid(row=0, column=0, padx=5, pady=5)

        self.ioframe = genericframe(self)
        self.ioframe.grid(row=1, column = 0)

        self.ioframe.createnninputframe()
        self.ioframe.creatennoutputframe()

        self.ioframe.createdatainputs()
        #self.ioframe.createdataoutputs()

if __name__ == "__main__":
    app = App()
    app.mainloop()