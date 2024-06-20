import pandas as pd


df =  pd.read_json('data.json')

#df.astype({'grade':int})
#print(df.to_string())
df.fillna()

print("Head output \n",df.head())
print('Tail output \n',df.tail())
print('Info output \n',df.info())