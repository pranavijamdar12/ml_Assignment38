import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

passed = df[df["FinalResult"]==1]
failed = df[df["FinalResult"]==0]

plt.scatter(
    passed["SleepHours"],
    passed["FinalResult"],
    color = "green",
    label = "passed"
)

plt.scatter(
    failed["SleepHours"],
    failed["FinalResult"],
    color = "black",
    label = "failed"

    
)
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.title("Sleep Hours vs Final Result")

plt.legend()
plt.grid()
plt.show()
