import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

grad_data = pd.read_csv("other/Admission_Predict.csv")

gre_score = grad_data["GRE Score"]
addmision_chance = grad_data["Chance of Admit "]

x = np.array(addmision_chance).reshape((-1,1))
y = np.array(gre_score)

model = LinearRegression().fit(x,y)
y_pred = model.predict(x)

plt.plot(gre_score, addmision_chance * 100, 'ro',  y_pred, addmision_chance *100)
plt.title("Gre Score vs Chance of Admit")
plt.xlabel("GRE Score")
plt.ylabel("Chance of Admission (%)")
plt.axis([290,340,0,100])
plt.grid(True)
plt.show()