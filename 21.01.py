import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
value = df.iloc[1, 1]
print(value) 