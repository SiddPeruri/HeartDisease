import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from tkinter import *
from mlprunner import mlprun
import customtkinter as ctk
from inputframe import inputs


mlp = mlprun()
global answer


root = ctk.CTk()






root.geometry("1920x1080")
root.title('Heart disease prediction app(Science fair 2022-2023)')
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

inputsframe = inputs(root, headername='inputs:')

inputsframe.grid(row=1, column=0, pady=20)

title = ctk.CTkLabel(root, text="Heart Disease Prediction App", font=('Comic Sans', 46))
title.grid(row=0, column=0, padx=10)


root.mainloop()