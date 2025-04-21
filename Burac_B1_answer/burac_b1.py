import pandas as pd

df = pd.read_csv( 'Exam_Table.csv', sep="," , skip_blank_lines=True).dropna()

df2 = df[df['Interval']==('30-0')]

print (df2)

df2.to_csv("b1_output1.csv", index=False)