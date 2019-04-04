import requests
from fake_useragent import UserAgent
import pandas as pd
ua = UserAgent()

# API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/geoObjects"
API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/dim_developer_group"
DEVELOPER_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/developer_group_region?developerGroupId={developer_id}"
# https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/developer_group_region?developerGroupId=429726001

# 81.177.103.102:443

headers = requests.utils.default_headers()
headers['User-Agent'] = ua.random

request_bod = requests.get(url=API_ENDPOINT, headers=headers)
request_developers = request_bod.json()


# from itertools import filter
developer = [elem for elem in filter(lambda x: x['developer_group_id'] == '429726001', request_data)][0]
# [elem for elem in request_data if elem['developer_group_id'] == 429726001]
request_data[0]
# developer = request_data[200]

for developer in request_developers:

    DETAILED_DEVELOPER_ENDPOINT = DEVELOPER_ENDPOINT.format(**{"developer_id" : developer["developer_group_id"]})

    developer_bod = requests.get(url=DETAILED_DEVELOPER_ENDPOINT, headers=headers)
    developer_data = developer_bod.json()


    for key,val in developer_data.iteritems():
        ret[val].append(key)
# len(request_bod.json())
#
# pd.DataFrame(request_bod.json())

map(lambda x: x["developer_group_name"] d.update()
for key,val in developer_data.iteritems():
    ret[val].append(key)


import random
# https://xn--80az8a.xn--d1aqf.xn--p1ai/%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0/grapi/v1/geoObjects
# [random.random() * 5 for i in range(10)]
