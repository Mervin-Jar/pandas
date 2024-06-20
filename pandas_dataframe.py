import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
mydataset = pd.DataFrame(data)

print(mydataset.loc[0:1])

