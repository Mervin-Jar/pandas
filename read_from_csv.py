import pandas as pd

data = pd.read_csv('data.csv')

# this will not print all the datas inside the csv file
print(data)

# this willprint all the datas present inside the csv files
print(data.to_string())
