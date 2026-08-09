import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

passed = df[df["FinalResult"]==1]
fail = df[df["FinalResult"]==0]

plt.scatter(
    passed["StudyHours"],
    passed["PreviousScore"],
    color = "green",
    label = "Pass"


)

plt.scatter(
    fail["StudyHours"],
    fail["PreviousScore"],
    color = "black",
    label = "fail"

)

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study hours vs previousscore")

plt.legend()
plt.grid()
plt.show()
