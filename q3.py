import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Avarage Study hours:")
print(df["StudyHours"].mean())

print("Avarage attendence:")
print(df["Attendance"].mean())

print("Maximum previous score:")
print(df["PreviousScore"].max())

print("Minimum SleepHours:")
print(df["SleepHours"].min())
