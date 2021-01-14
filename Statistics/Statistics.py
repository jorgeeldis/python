import pandas as pd

presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

print(presidents_df.mean())
print(presidents_df.max())
print(presidents_df.min())
print(pd.Series([1, 2, 1, 4, 2]).mean())
print(presidents_df.std())
print(presidents_df['age'].var())
print(presidents_df.describe())
