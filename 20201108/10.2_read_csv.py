import pandas as pd
import os

print("-- file name --")
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))
print(os.getcwd())
print(os.path.dirname(__file__))

file_name = '\\titanic.csv'
file_path = os.getcwd() + file_name
print(file_path)

# df = pd.read_csv(file_name)
# df = df.loc[:,['age','sex','survived']]
# print(df.head())
# print()

# df2 = pd.read_csv(file_name,header = None)
# df2 = df2.loc[1:,[3,2,0]]
# print(df2.head())
# print()

