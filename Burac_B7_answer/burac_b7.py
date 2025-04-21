import pandas as pd

df = pd.read_csv('Exam_Table.csv', skip_blank_lines=True).dropna()

df2 = df.transpose()

print(df2)

df2.to_csv("b7_output1.csv")