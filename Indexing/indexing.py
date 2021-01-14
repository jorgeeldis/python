import pandas as pd

presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

print(type(presidents_df.loc['Abraham Lincoln']))
print(presidents_df.loc['Abraham Lincoln'].shape)
print(presidents_df.iloc[15:18])
print(presidents_df[['height', 'age']].head(n=3))
