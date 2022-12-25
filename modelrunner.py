import torch
import torch.nn as nn
import pandas as pd
import torch.utils.model_zoo as model_zoo
import torch.onnx
from torch import nn
import torch.nn.init as init
from sklearn.model_selection import train_test_split

device = torch.device('cpu')

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = NeuralNetwork(input_size=12, hidden_size=256, num_classes=2)
model.load_state_dict(torch.load("heart.model", map_location=device))
model.to(device)
criterion = nn.CrossEntropyLoss()

heart = pd.read_csv("heart.csv")
heart=heart.drop(['thal'],axis=1)
train, test = train_test_split(heart, test_size=0.01)
testInputs = torch.tensor(test[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca']].values, dtype=torch.float)
#print(testInputs)
testTarget = torch.tensor(test[test.columns[12]].values, dtype=torch.long)
#print(testTarget)

myTest = torch.tensor([[55,0,1,132,342,0,1,166,0,1.2,2,0
                        ]], dtype=torch.float)

with torch.no_grad():
    probabilities = model(testInputs)
    loss = criterion(probabilities, testTarget)
    print(f'Test set loss: {loss.item():.4f}')
    _, predicted_classes = torch.max(probabilities, dim=1)
    print(predicted_classes)
    print(testTarget)

    myPrediction = model(myTest)
    _, myResult = torch.max(myPrediction, dim=1)
    print(myResult)

