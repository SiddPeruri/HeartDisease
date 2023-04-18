Heart Disease Prediction with a Trained Multilayer Perceptron

This project is a Python implementation of a multilayer perceptron (MLP) that predicts the presence of heart disease based on a patient's medical data. 
The MLP is trained using a dataset of patient data from the Heart Disease Dataset by David Lapp(https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset). 
This includes data points such as age, sex, chest pain type (4 values), resting blood pressure, serum cholestoral in mg/dl, fasting blood sugar > 120 mg/dl
resting electrocardiographic results (values 0,1,2), maximum heart rate achieved, exercise induced angina, oldpeak = ST depression induced by exercise relative to rest
the slope of the peak exercise ST segment, number of major vessels (0-3) colored by flourosopy, thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

The MLP is implemented using the PyTorch library and consists of three layers: an input layer, a hidden layer, and an output layer. 
The input layer has 14 neurons, one for each feature in the dataset. The hidden layer has 8 neurons and uses the ReLU activation function. 
The output layer has 1 neuron and uses the sigmoid activation function to produce a probability of the patient having heart disease.

The MLP is trained using a binary cross-entropy loss function and the Adam optimizer. 
The training data is split into a training set and a validation set using a 80/20 split, and the model is trained for 100 epochs 
with early stopping based on the validation loss.

The trained MLP can be used to predict the presence of heart disease for new patients based on their medical data. 
The input data is expected to be in the form of a CSV file with 14 columns, one for each feature in the dataset.

To run the heart disease prediction model, you can use the predict.py script, which takes the path to the input CSV file as a command-line argument 
and outputs the predicted probability of the patient having heart disease.

Requirements:

Python 3.10
Torch 1.13.0 or higher
Pandas 1.5.2 or higher
scikit-learn 1.2.0 or higher
customtkinter 5.03 or higher
Seaborn 0.12.1 or higher

Extras:
Tkinter, Numpy, PIL, wheel



Usage:

1. Download Zip

2. Unzip

3. Instal Dependencies

4. (optional) Run training file

5. Run GUI file

6. Use at will!
