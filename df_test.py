import pandas as pd
pew = pd.read_csv("data.csv")
pew.shape
pew = pd.read_csv("data.csv")
pew.shape
pew = pd.read_csv("data.csv")
pew.shape
pew = pd.read_csv("data.csv")
pew.shape
pew = pd.read_csv("data.csv")
pew.shape
pew.drop_duplicates().groupby(["developer_group_id","region_id"]).count()["developer_group_name"].sort_values(ascending = False)
pew.groupby(["developer_group_id","region_id"]).count()["developer_group_name"].sort_values(ascending = False)


pew

pew.loc[(pew.region_id == 1764) &(pew.developer_group_id == 755344001) ,:].drop_duplicates()
