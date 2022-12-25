import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


heart = pd.read_csv("heart.csv")
heart=heart.drop('fbs',axis=1)

sns.set_theme()

#heart disease by age
sns.countplot(x="age", hue="target", data=heart)
plt.show()

#heart disease by cholestorol
sns.countplot(x="chol", hue="target", data=heart)
plt.show()

#based on gender/sex
sns.relplot(x='sex', hue='target', data=heart)
plt.show()

#based on bps at rest
sns.countplot(x="trestbps", hue="target", data=heart)
plt.show()

def byvalue(value):
    sns.countplot(x=value, hue="target", data=heart)
    plt.show()




print("ended")