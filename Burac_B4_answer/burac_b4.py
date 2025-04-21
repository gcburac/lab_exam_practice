import pandas as pd

df = pd.read_csv('Exam_Table.csv', skip_blank_lines=True).dropna()

df2 = df["Scientific Name"].unique()

df3 = df.groupby("Scientific Name")["Size Est (cm)"].mean()

#print (df3)

df4 = pd.DataFrame({"Average" : df3})

print (df4)

df4.to_csv("b4_output1.csv")