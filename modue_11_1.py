import pandas as pd
import numpy as np

df1 = pd.read_excel("Book1.xlsx")

print(df1.head())
print(df1.tail())
print()

print(df1.describe())
print()
print(df1.describe(percentiles=[0.75, 0.9, 0.95]))
print()

print(df1.info(show_counts=True, verbose=True))
print()

print(df1.shape)
print(df1.shape[0])
print(df1.shape[1])
print()

print(list(df1.columns))
print()

print(df1["stolb_1"])
print()
print(df1[["stolb_1", "stolb_2"]])

df2 = df1.copy()
print(df2)
print()

print(df2.loc[1])
print(df2.iloc[1])
print(df2.loc[1:5])
print()

print(df1.mean())
print(df1.mode())
print(df1.median())
