import pandas as pd

df = pd.read_csv("student_performance_ml.csv")
pass_study = df[df["FinalResult"]==1]["StudyHours"].mean()
fail_study = df[df["FinalResult"]==0]["StudyHours"].mean()

pass_attendence = df[df["FinalResult"]==1]["Attendance"].mean()
fail_attendence = df[df["FinalResult"]==0]["Attendance"].mean()
print("Avarage study hours of pass student:",pass_study)
print("Avarage study hours os fail student:",fail_study)

print("Avarage of pass Attendence student:",pass_attendence)
print("Avarage of fail Attendence student:",fail_attendence)

