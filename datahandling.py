import torch
import pandas as pd
from sklearn.model_selection import train_test_split


class data():
    def __init__(self):
        heart = pd.read_csv("heart.csv")
        heart = heart.drop(['thal'], axis=1)
        train, test = train_test_split(heart, test_size=0.1)
        self.trainInputs = train[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope','ca']].values
        self.trainTargets = train[train.columns[12]].values
        self.ptestInputs = test[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope','ca']].values
        self.testTargets = test[test.columns[12]].values
    def grabdata(self, name):
        if name == "inputs":
            output = torch.tensor(self.trainInputs, dtype=torch.float)
        if name == "targets":
            output = torch.tensor(self.trainTargets, dtype=torch.long)
        if name == "testInputs":
            output = torch.tensor(ptestInputs, dtype=torch.float)
        if name == "testTargets":
            output = torch.tensor(ptestTargets, dtype=torch.long)
        else:
            print("fix data grab")
            exit(1)
        return output


