import torch
import torch.nn as nn
import pandas as pd
import torch.utils.model_zoo as model_zoo
import torch.onnx
from torch import nn
import torch.nn.init as init
from sklearn.model_selection import train_test_split

device = torch.device("cpu")
#heart = pd.read_csv("heart.csv")
aml =pd.read_csv("aml_clinical_data.csv")
#heart=heart.drop(['thal'],axis=1)
#aml=aml.drop(['thal'],axis=1) [check this attribute later]
#print(heart.head())
#print(heart.columns)
#exit(0)

#train, test = train_test_split(heart, test_size=0.1)
train, test = train_test_split(aml, test_size=0.1)

#trainInputs = train[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca']].values
trainInputs = train[['Mutation Count','Diagnosis Age','Sex','Ethnicity Category', 'Abnormal Lymphocyte Percent', 'Atra Exposure', 'Basophils Cell Count', 'Blast Count', 'Platelet count preresection', 'Prior Cancer Diagnosis Occurence']].values
#print(trainInputs)

trainTargets = train[train.columns[10]].values
#print(trainTargets) (print it while testing)

inputs = torch.tensor(trainInputs, dtype=torch.long)
#inputs = torch.from_numpy(trainInputs).type(torch.float32)
targets = torch.tensor(trainTargets, dtype=torch.long)
print(targets)

#testInputs = torch.tensor(test[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca']].values, dtype=torch.float)
testInputs = torch.tensor(test[['Mutation Count', 'Diagnosis Age', 'Sex', 'Ethnicity Category','Abnormal Lymphocyte Percent','Atra Exposure','Basophils Cell Count','Blast Count','Platelet count preresection', 'Prior Cancer Diagnosis Occurence']].values, dtype=torch.float)
#print ("inputs")
#print(testInputs)
#print("output")
testTarget = torch.tensor(test[test.columns[10]].values, dtype=torch.long)
print("testTarget values are...\n")
print(testTarget)

#print(testInputs.size())

#print(inputs.shape[1])
#exit(0)

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        return out

model = NeuralNetwork(input_size=inputs.shape[1], hidden_size=256, num_classes=targets.max().item()+1)

model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
#num_epochs = 10000
num_epochs =10000  #250 #4500    #3000
model.train(True)
#file_obj = open("writing.txt", "w")

for epoch in range(num_epochs):
    outputs = model(inputs.to(torch.float))
    loss = criterion(outputs, targets)

    print(f"Epoch: {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}")
    #print(outputs)
    #file_obj.write(f'\n{loss.item():.4f}')

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

model.train(False)

#prediction
# Step 6: Evaluate the model on the test set
with torch.no_grad():
    probabilities = model(testInputs)
    loss = criterion(probabilities, testTarget)
    print(f'Test set loss: {loss.item():.4f}')

    _, predicted_classes = torch.max(probabilities, dim=1)
   # print(predicted_classes)
   # print(testTarget)

# Export the model
'''
torch.onnx.export(model,               # model being run
                  testInputs,                         # model input (or a tuple for multiple inputs)
                  "aml.onnx",   # where to save the model (can be a file or file-like object. rename from heart to aml)
                  export_params=True,        # store the trained parameter weights inside the model file
                  opset_version=10,          # the ONNX version to export the model to
                  do_constant_folding=True,  # whether to execute constant folding for optimization
                  input_names = ['Mutation Count', 'Diagnosis Age', 'Sex', 'Ethnicity Category','Abnormal Lymphocyte Percent','Atra Exposure','Basophils Cell Count','Blast Count','Platelet count preresection', 'Prior Cancer Diagnosis Occurence',],   # the model's input names
                  output_names = ['Detected'], # the model's output names
                  dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                                'output' : {0 : 'batch_size'}})
## (prior order of attribiutes.. need to match with dataset) input_names = ['Diagnosis Age', 'Sex', 'Ethnicity Category', 'Mutation Count', 'Abnormal Lymphocyte Percent', 'Atra Exposure', 'Basophils Cell Count', 'Blast Count', 'Platelet count preresection', 'Prior Cancer Diagnosis Occurence',],   # the model's input names                                
# input_names = ['age', 'sex','cp','trestbps','chol', 'restecg', 'thalach', 'exang', 'oldpeak', 'fbs', 'slope','ca',],   # the model's input names
#output_names = ['target'], # the model's output names
x = torch.rand((10, 1), dtype=torch.float) # updated to 10 attributes instead of 12..
torch.onnx.export(
            model,
            x,
            "aml.onnx",
            export_params=True,
            opset_version=10,
            do_constant_folding=True,
            #input_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca'],   # the model's input names
            output_names = ['Detected'])


'''

torch.save(model.state_dict(), "aml.model")
#file_obj.close()
