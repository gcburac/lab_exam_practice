import pandas as pd

df = pd.read_csv('Exam_Table.csv', skip_blank_lines=True).dropna()

df["HRID"] = df["Location"].apply(lambda x: x.replace(",","-").replace(" ","")) + "-" + df["Site"] + "-" + df["Replicate"].astype(int).astype(str)

print(df)

df.to_csv("b6_output1.csv", index=False)
