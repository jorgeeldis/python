import pandas as pd

wine_dict = {
    'red_wine': [3, 6, 5],
    'white_wine': [5, 0, 10]
}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
print(sales['white_wine'])

presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
presidents_df.shape
presidents_df.shape[0]
presidents_df.size
print(presidents_df.head(n=3))
