import pandas as pd

df = pd.read_csv('Exam_Table.csv', skip_blank_lines=True).dropna()

df2 = df["Scientific Name"].unique()

df3 = pd.DataFrame({"Scientific Names" : df2})

print(df3)

df3.to_csv("b3_output1.csv", index=False)