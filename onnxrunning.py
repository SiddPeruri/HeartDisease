import onnx
import onnxruntime
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn

heart = pd.read_csv("heart.csv")
heart=heart.drop(['thal'],axis=1)
#print(heart.head())

train, test = train_test_split(heart, test_size=0.1)

trainInputs = train[train.columns[:11]].values
#print(trainInputs)
trainTargets = train[train.columns[12]].values
#print(trainTargets)



inputs = torch.tensor(trainInputs, dtype=torch.float)
targets = torch.tensor(trainTargets, dtype=torch.long)
#print(targets)

testInputs = torch.tensor(test[test.columns[:11]].values, dtype=torch.float)
#print(testInputs)
testTarget = torch.tensor(test[test.columns[12]].values, dtype=torch.long)
#print(testTarget)

onnxmodel = onnx.load("mlp.onnx")
onnx.checker.check_model(onnxmodel)

ort_session = onnxruntime.InferenceSession("mlp.onnx")

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

# compute ONNX Runtime output prediction
ort_inputs = {ort_session.get_inputs()[0].name.max(dim=1): to_numpy(targets.float())}
ort_outs = ort_session.run(None, ort_inputs)

# compare ONNX Runtime and PyTorch results
np.testing.assert_allclose(to_numpy(torch_out), ort_outs[0], rtol=1e-03, atol=1e-05)

print("Exported model has been tested with ONNXRuntime, and the result looks good!")