import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")
plt.hist(df["StudyHours"],
         bins= 10,
         edgecolor = "black")
plt.title("Distribustion of study hours")
plt.xlabel("Study hours")
plt.ylabel("Number of Distribution")

plt.legend()
plt.grid()
plt.show()
