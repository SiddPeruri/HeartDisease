import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import tkinter as tk
from MLP import NeuralNetwork as mlp
from datahandling import data

class mlprun():
    def __init__(self):
        self.device = torch.device('cpu')
        self.model = mlp(input_size=10, hidden_size=256, num_classes=2)  # updated from 12 variables to 10 inputs
    def modelin(self, tensor):
        self.model.load_state_dict(torch.load("aml.model", map_location=self.device))
        self.model.to(self.device)
        myPrediction = self.model(tensor)
        _, myResult = torch.max(myPrediction, dim=1)
        return myResult