import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

passed = df[df["FinalResult"]==1]
failed = df[df["FinalResult"]==0]

plt.scatter(
    passed["AssignmentsCompleted"],
    passed["FinalResult"],
    color = "green",
    label = "Pass"


)

plt.scatter(
    failed["AssignmentsCompleted"],
    failed["FinalResult"],
    color = "red",
    label = "Fail"

)

plt.xlabel("Assignment Completed")
plt.ylabel("Final Result")
plt.title("AssignmentCompleted vas FinalResult")

plt.legend()
plt.grid()
plt.show()
