import pandas as pd
df = pd.read_csv("2016-2019_sorted.csv")
df["zip_code"] = df["zip_code"].astype('Int64')
result = df.groupby(["item_description","zip_code","store_name"])["volume_sold_liters"].aggregate('sum')
final_result = result.sort_values(ascending=False)
print(final_result)
final_result.to_csv("most_sold_item.csv")