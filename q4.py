import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

result_count = df["FinalResult"].value_counts()

print("FinalResult Distribution:")
print(result_count)

total = len(df)

pass_percentage = (result_count.get(1,0)/total)*100
fail_percentage = (result_count.get(0,0)/total)*100

difference = abs(pass_percentage - fail_percentage)

if difference <= 10:
    print("\nDataset is Balence:")
else:
    print("\n Dataset is not Balence:")
    
