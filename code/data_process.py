import csv
import pandas as pd
# with open('data/daily_sales_data_0.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

df_zero = pd.read_csv("data/daily_sales_data_0.csv")

df_filtered_zero = df_zero[df_zero['product'] == 'pink morsel']

df_filtered = df_filtered_zero[['product', 'quantity', 'price', 'region', 'date']]

df_filtered_zero['price'] = df_filtered_zero['price'].astype(str).str.extract(r'\$(\d+\.?\d*)')[0]
df_filtered_zero['price'] = df_filtered_zero['price'].astype(float)

df_filtered_zero['sales'] = df_filtered['quantity'] * df_filtered_zero['price']

df_filtered_zero = df_filtered_zero.drop(columns=['product'])
print(df_filtered_zero.head())


df_one = pd.read_csv("data/daily_sales_data_1.csv")

df_filtered_one = df_one[df_one['product'] == 'pink morsel']

df_filtered_one = df_filtered_one[['product', 'quantity', 'price', 'region', 'date']]

df_filtered_one['price'] = df_filtered_one['price'].astype(str).str.extract(r'\$(\d+\.?\d*)')[0]
df_filtered_one['price'] = df_filtered_one['price'].astype(float)

df_filtered_one['sales'] = df_filtered_one['quantity'] * df_filtered_one['price']

df_filtered_one = df_filtered_one.drop(columns=['product'])

print(df_filtered_one.head())



df_two = pd.read_csv("data/daily_sales_data_2.csv")

df_filtered_two = df_two[df_two['product'] == 'pink morsel']

df_filtered_two = df_filtered_two[['product', 'quantity', 'price', 'region', 'date']]

df_filtered_two['price'] = df_filtered_two['price'].astype(str).str.extract(r'\$(\d+\.?\d*)')[0]
df_filtered_two['price'] = df_filtered_two['price'].astype(float)

df_filtered_two['sales'] = df_filtered_two['quantity'] * df_filtered_two['price']

df_filtered_two = df_filtered_two.drop(columns=['product'])

print(df_filtered_two.head())

full_df = df_filtered_zero.merge(df_filtered_one, how="right")
full_df = full_df.merge(df_filtered_two, how="right")
print(full_df)

full_df.to_csv(r'data/filtered_dataset.csv', index=False)


