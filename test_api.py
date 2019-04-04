import requests
from fake_useragent import UserAgent
import pandas as pd
ua = UserAgent()

# API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/geoObjects"
API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/dim_developer_group"

# https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/developer_group_region?developerGroupId=429726001

# 81.177.103.102:443

headers = requests.utils.default_headers()
headers['User-Agent'] = ua.random

request_bod = requests.get(url=API_ENDPOINT, headers=headers)
request_data = request_bod.json()

429726001
developer = request_data[200]

DETAILED_DEVELOPER_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/developer_group_region?developerGroupId={developer_id}".format(**{"developer_id" : developer["developer_group_id"]})
DETAILED_DEVELOPER_ENDPOINT

developer_bod = requests.get(url=DETAILED_DEVELOPER_ENDPOINT, headers=headers)
developer_data = developer_bod.json()
developer_data
# len(request_bod.json())
#
# pd.DataFrame(request_bod.json())


import random
# https://xn--80az8a.xn--d1aqf.xn--p1ai/%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0/grapi/v1/geoObjects
# [random.random() * 5 for i in range(10)]
