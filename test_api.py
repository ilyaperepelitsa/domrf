import requests
from fake_useragent import UserAgent
import pandas as pd
import time
import random
import csv
import os.path

ua = UserAgent()

# API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/geoObjects"
API_ENDPOINT = "https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group"
DEVELOPER_ENDPOINT = "https://наш.дом.рф/аналитика/grapi/v1/developer_group_region?developerGroupId={developer_id}"
# https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/developer_group_region?developerGroupId=429726001

# 81.177.103.102:443

headers = requests.utils.default_headers()
headers['User-Agent'] = ua.random

request_bod = requests.get(url=API_ENDPOINT, headers=headers)
request_developers = request_bod.json()


# from itertools import filter
# developer = [elem for elem in filter(lambda x: x['developer_group_id'] == '429726001', request_data)][0]
# [elem for elem in request_data if elem['developer_group_id'] == 429726001]
# request_data[0]
# developer = request_data[200]


# file_exists = os.path.isfile("data.csv")
developer["developer_group_id"] in existing_data_test["developer_group_id"].unique()

for developer in request_developers:
    file_exists = os.path.isfile("data.csv")
    # if file_exists:
    #     existing_data_test = pd.read_csv("data.csv", encoding = "utf-8")
    #     if developer["developer_group_id"] in existing_data_test["developer_group_id"].unique():
    #         break
    #     else:
    #         pass

    # time.sleep(random.random() * 1)
    print(developer)
    DETAILED_DEVELOPER_ENDPOINT = DEVELOPER_ENDPOINT.format(**{"developer_id" : developer["developer_group_id"]})
    REPORT_ENDPOINT = "https://наш.дом.рф/аналитика/grapi/v1/entityInfoDateRange?id={developer_id}&type=devGroup"
    ALT_DEV_INFO_ENDPOINT = "https://наш.дом.рф/аналитика/grapi/v1/developer_group_info?developerGroupId={developer_id}"

    REPORT_ENDPOINT = REPORT_ENDPOINT.format(**{"developer_id" : developer["developer_group_id"]})
    ALT_DEV_INFO_ENDPOINT = ALT_DEV_INFO_ENDPOINT.format(**{"developer_id" : developer["developer_group_id"]})


    try:
        report_data = requests.get(url= REPORT_ENDPOINT, headers=headers)
        report_data = report_data.json()["payload"]
    except:
        time.sleep((random.random() * 2) + 5)
        report_data = requests.get(url= REPORT_ENDPOINT, headers=headers)
        report_data = report_data.json()["payload"]
    # report_data = {k: v.encode('utf-8','ignore') for k,v in report_data.items()}
    # developer = {k: v.encode('utf-8','ignore') for k,v in developer.items()}
    try:
        developer_bod = requests.get(url=DETAILED_DEVELOPER_ENDPOINT, headers=headers)
        developer_data = developer_bod.json()
    except:
        time.sleep((random.random() * 2) + 5)
        developer_bod = requests.get(url=DETAILED_DEVELOPER_ENDPOINT, headers=headers)
        developer_data = developer_bod.json()

    # developer_data = {k: v.encode('utf-8','ignore') for k,v in developer_data.items()}

    # Cast developer ids only (sql prepared)
    try:
        ald_dev_info = requests.get(url=ALT_DEV_INFO_ENDPOINT, headers=headers)
        ald_dev_info_data = ald_dev_info.json()
    except:
        time.sleep((random.random() * 2) + 5)
        ald_dev_info = requests.get(url=ALT_DEV_INFO_ENDPOINT, headers=headers)
        ald_dev_info_data = ald_dev_info.json()



    developer_data = [dict(dev_data, **{k: v for k, v in ald_dev_info_data.items() if
                k in ["developer_group_id",
                        "developer_group_name",
                        "developer_group_address"]}) for dev_data in developer_data]

    # Cast all developer data on entries
    # developer_data = [dict(dev_data, **developer) for dev_data in developer_data]

    # Cast all developer data on entries
    developer_data = [dict(dev_data, **report_data) for dev_data in developer_data]

    print(len(developer_data))

    developer_data_df = pd.DataFrame(developer_data)



    if len(developer_data) > 0:

        if file_exists:
            existing_data = pd.read_csv("data.csv", encoding = "utf-8")
            # existing_data = pd.read_csv("data.csv", encoding='cp866')
            # existing_data = existing_data.drop_duplicates()
            existing_data = existing_data.loc[:,['developer_group_id','developer_group_name', 'developer_group_address', 'region_id',
                   'region_name',  'startDate', 'endDate',
                   'total_living_floor_size', 'appt_num', 'object_count',
                   'total_living_floor_size_pct', 'typed_volume_pct', 'rating']
                   ]
            developer_data_df = developer_data_df.reindex(existing_data.columns.tolist(), axis =1)
            developer_data_df = developer_data_df.astype(existing_data.dtypes.to_dict())

            developer_data_df = developer_data_df.merge(existing_data,
                                    on=existing_data.columns.tolist(),
                                    how='left', indicator=True)

            developer_data_unique = developer_data_df.loc[developer_data_df["_merge"] == "left_only",:].drop("_merge", axis = 1)
            developer_data_non_unique = developer_data_df.loc[developer_data_df["_merge"] != "left_only",:].drop("_merge", axis = 1)
            # print("________________________________________")
            # print(developer_data_unique.to_dict())
            # print(developer_data_non_unique.to_dict())
            # print("________________________________________")

            # if len(developer_data) != developer_data_df.shape[0]:
            #
            #     print("PEW  " + str(developer_data_df.shape[0]))
            if developer_data_unique.shape[0] > 0:
                developer_data_unique = pd.concat([existing_data, developer_data_unique], axis = 0)
                developer_data_unique.drop_duplicates(subset = ['developer_group_id',
                                                'region_id', 'startDate', 'endDate']).to_csv('data.csv',header=True, index = False, encoding = "utf-8")
        else:
            developer_data_df = developer_data_df.loc[:,['developer_group_id','developer_group_name', 'developer_group_address', 'region_id',
                   'region_name',  'startDate', 'endDate',
                   'total_living_floor_size', 'appt_num', 'object_count',
                   'total_living_floor_size_pct', 'typed_volume_pct', 'rating']
                   ]
            developer_data_df.drop_duplicates(subset = ['developer_group_id',
                                            'region_id', 'startDate', 'endDate']).\
                                to_csv('data.csv',header=True, index = False, encoding = "utf-8")
    else:
        developer_empty = pd.Series(developer)
        developer_empty = developer_empty.loc[['developer_group_id', 'developer_group_name']]
        if os.path.isfile("data_missing.csv"):
            developer_empty.to_csv('data_missing.csv', mode='a', header=False, index = False)
        else:
            developer_empty.to_csv('data_missing.csv', mode='a', header=True, index = False)


ald_dev_info.json()
developer
{'developer_group_name': 'Застройщик-ДВ', 'developer_group_id': '5904592001'}

ald_dev_info = requests.get(url=ALT_DEV_INFO_ENDPOINT, headers=headers)
ald_dev_info_data = ald_dev_info.json()
ald_dev_info_data

pd.Series(developer).loc[['developer_group_id', 'developer_group_name']]


report_data
existing_data.dtypes.to_dict()
developer


developer = request_developers[-1]
developer
DETAILED_DEVELOPER_ENDPOINT = DEVELOPER_ENDPOINT.format(**{"developer_id" : developer["developer_group_id"]})
developer_bod = requests.get(url=DETAILED_DEVELOPER_ENDPOINT, headers=headers)
developer_data = developer_bod.json()
developer_data

REPORT_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/entityInfoDateRange?id={developer_id}&type=devGroup"
REPORT_ENDPOINT = REPORT_ENDPOINT.format(**{"developer_id" : developer["developer_group_id"]})
report_data = requests.get(url= REPORT_ENDPOINT, headers=headers)
report_data = report_data.json()["payload"]

developer_data = [dict(dev_data, **developer) for dev_data in developer_data]
developer_data = [dict(dev_data, **report_data) for dev_data in developer_data]
developer_data


existing_data = pd.read_csv("data.csv")
existing_data = existing_data.drop(existing_data.columns[0], axis = 1)


new_data = pd.DataFrame(developer_data)
new_data.to_dict()
# existing_data.columns

existing_data = existing_data.loc[:,['developer_group_id','developer_group_name', 'region_id',
       'region_name',  'startDate', 'endDate',
       'total_living_floor_size', 'appt_num', 'object_count',
       'total_living_floor_size_pct', 'typed_volume_pct', 'rating']
       ]
new_data = new_data.reindex(existing_data.columns.tolist(), axis =1)
new_data = new_data.astype(existing_data.dtypes.to_dict())
# new_data.loc[:,existing_data.columns.tolist()]
# common = new_data.astype(existing_data.dtypes.to_dict()).merge(existing_data)
# common = existing_data.merge(new_data.astype(existing_data.dtypes.to_dict()))
# common

mask = new_data.values().isin(existing_data)
.any(axis = 1)
mask.to_dict()

new_data[~np.in1d(new_data, existing_data)]


new_data[~new_data.isin(existing_data.iloc[0:5,:])].dropna()
existing_data.iloc[0:5,:]

new_data.to_dict()
existing_data.loc[existing_data.developer_group_id.isin(new_data.developer_group_id.unique()),:].to_dict()

new_data.to_dict()

common.shape[0] == new_data.shape[0]

.loc[developer_data_df["_merge"] == "left_only",:].drop("_merge", axis = 1)

pew = new_data.\
        merge(existing_data, on=existing_data.columns.tolist(), how='left', indicator=True)


pew.loc[pew["_merge"] == "left_only",:].\
        drop("_merge", axis = 1)


                # to_dict().\

# np.in1d(new_data.values, existing_data.values, assume_unique = True).shape
# existing_data.shape
# print()
new_data.values == existing_data.values


    # developer_data_df.to_csv('data.csv', mode='a', header=True)


    #
    #
    # with open(filename, 'a') as f:
    #     df.to_csv(f, mode='a', header=f.tell()==0)
    #
    #
    # with open('data.csv', 'a', newline = "") as csvfile:
    #
    #     for developer_datum in developer_data:
    #         # developer_datum =
    #         headers_csv = list(developer_datum.keys())
    #         writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers_csv, dialect='excel')
    #         if not file_exists:
    #             writer.writeheader()
    #
    #         writer.writerow({k:v.encode('utf8') for k,v in developer_datum.items()})

# developer_datum


            # a = csv.writer(fp, delimiter=',')
            # a.writerows(developer_datum)
            #
            # headers = ['TimeStamp', 'light', 'Proximity']


      # file doesn't exist yet, write a header



# developer["developer_group_id"]
# developer_data

SAD = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/entityInfoDateRange?id={429726001}&type=devGroup".format(**{"developer_id" : developer["developer_group_id"]})
requests.get(url="https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/entityInfoDateRange?id={developer_id}&type=devGroup".format(**{"developer_id" : developer["developer_group_id"]}), headers=headers).json()



developer_datum.keys()
    # Use if need to have both dev id and dev name
    # developer_data = [dict(dev_data, **developer) for dev_data in developer_data]

    # print(len(developer_data))

    # for key,val in developer_data.iteritems():
    #     ret[val].append(key)
# len(request_bod.json())
#
# pd.DataFrame(request_bod.json())
developer_data = [dict(dev_data, **request_data[0]) for dev_data in developer_data]


map(lambda x: x.update({"developer_group_name" : request_data[0]["developer_group_name"]}), developer_data)
developer_data
# for key,val in developer_data.iteritems():
    # ret[val].append(key)
