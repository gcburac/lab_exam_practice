import pandas as pd

df = pd.read_csv('Exam_Table.csv', sep="," , skip_blank_lines=True).dropna()

df2 = df[df['Genus'].str.startswith('St' or 'st' or 'sT' or 'ST')]

print(df2)

df2.to_csv("b2_output1.csv")