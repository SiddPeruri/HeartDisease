#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#import matplotlib as mpl


#heart = pd.read_csv("heart.csv")
#heart=heart.drop('fbs',axis=1)

#sns.set_theme()

#sns.stripplot(data=heart, x="age", y="chol", hue="target")
#plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# heart = pd.read_csv("heart.csv")
aml = pd.read_csv("aml_clinical_data.csv")
# heart=heart.drop('fbs',axis=1)
aml = aml.drop('Basophils Cell Count', axis=1)
sns.set_theme()
# sns.stripplot(data=heart, x="age", y="chol", hue="target")
sns.stripplot(data=aml, x="Diagnosis Age", y="Platelet count preresection", hue="Detected")
plt.show()