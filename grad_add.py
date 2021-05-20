import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

grad_data = pd.read_csv("other/Admission_Predict.csv")

gre_score = grad_data["GRE Score"]
addmision_chance = grad_data["Chance of Admit "]

plt.plot(gre_score, addmision_chance * 100, 'ro')
plt.title("Gre Score vs Chance of Admit")
plt.xlabel("GRE Score")
plt.ylabel("Chance of Admission (%)")
plt.axis([290,340,0,100])
plt.grid(True)
plt.show()