import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#heart = pd.read_csv("heart.csv")
heart = pd.read_csv("aml_clinical_data.csv")
heart=heart.drop('Atra Exposure',axis=1)
sns.set_theme()

#AML disease by age
sns.countplot(x="Diagnosis Age", hue="Detected", data=heart)
plt.show()

#AML disease by Blast Count
sns.countplot(x="Blast Count", hue="Detected", data=heart)
plt.show()

#based on gender/sex
sns.relplot(x='Sex', hue="Detected", data=heart)
plt.show()

#based on Platelet count
sns.countplot(x="Platelet count preresection", hue="Detected", data=heart)
plt.show()
#based on Mutation count
sns.countplot(x="Mutation Count", hue="Detected", data=heart)
plt.show()

def byvalue(value):
    sns.countplot(x=value, hue="Detected", data=heart)
    plt.show()

print("ended")