import pandas as pd

df = pd.read_csv('Exam_Table.csv', skip_blank_lines=True).dropna()

#df2 = df[df["Scientific Name"]=="Pomacentrus adelus"]

df2 = df.groupby("Scientific Name")["Count"].mean()

df3 = pd.DataFrame({"Scientific Name": ["Pomacentrus adelus"], "Average count": df2["Pomacentrus adelus"]})

print(df3)

df3.to_csv("b5_output1.csv", index=False)