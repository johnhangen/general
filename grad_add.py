import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

grad_data = pd.read_csv("other/Admission_Predict.csv")

gre_score = grad_data["GRE Score"]
uni_rating = grad_data["University Rating"]
toefl_score = grad_data["TOEFL Score"]
addmision_chance = grad_data["Chance of Admit "]

# Gre reggresion 
x = np.array(addmision_chance).reshape((-1,1))
y = np.array(gre_score/(gre_score.max()) * 100)

model = LinearRegression().fit(x,y)
gre_predict = model.predict(x)

# toefl reggresion 
x = np.array(addmision_chance).reshape((-1,1))
y = np.array(toefl_score/(toefl_score.max()) * 100)

model = LinearRegression().fit(x,y)
toefl_predic = model.predict(x)

# univerity ranking reggresion 
x = np.array(addmision_chance).reshape((-1,1))
y = np.array(uni_rating/(uni_rating.max()) * 100)

model = LinearRegression().fit(x, y)
uni_rating_predict = model.predict(x)

# scaling
uni_rating = uni_rating/(uni_rating.max()) * 100
toefl_score = toefl_score/(toefl_score.max()) * 100
gre_score = gre_score/(gre_score.max()) * 100

#plot
plt.figure()

# Raw data points
plt.subplot(121)
plt.plot(gre_score, addmision_chance * 100, 'bo', toefl_score, addmision_chance * 100, 'C1o', uni_rating, addmision_chance * 100, 'go',)
plt.title("Raw Data")
plt.xlabel("Percent (out of 100)")
plt.ylabel("Chance of Admission (%)")
plt.grid(True)

# regresions of the data points
plt.subplot(122)
plt.plot(gre_predict, addmision_chance * 100, toefl_predic, addmision_chance * 100, uni_rating_predict, addmision_chance * 100)
plt.title("Reggresions")
plt.xlabel("Percent (out of 100)")
plt.ylabel("Chance of Admission (%)")
plt.grid(True)

plt.text(-20, 105, "blue = GRE, orange = TOEFL, green = unversity rank")
plt.suptitle("Gre Score vs Chance of Admit")
plt.show()