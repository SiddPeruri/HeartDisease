import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl


heart = pd.read_csv("heart.csv")
heart=heart.drop('fbs',axis=1)

sns.set_theme()

sns.stripplot(data=heart, x="age", y="chol", hue="target")
plt.show()