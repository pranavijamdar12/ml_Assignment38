import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

total_students = len(df)

pass_student = (df["FinalResult"]==1).sum()

fail_student = (df["FinalResult"]==0).sum()


print("total number of student:",total_students)
print("total number of a pass student:",pass_student)
print("total number of failed student:",fail_student)
