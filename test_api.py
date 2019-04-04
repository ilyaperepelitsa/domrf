import requests
from fake_useragent import UserAgent
import pandas as pd
ua = UserAgent()

# API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/geoObjects"
API_ENDPOINT = "https://xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/grapi/v1/dim_developer_group"
# 81.177.103.102:443

headers = requests.utils.default_headers()
headers['User-Agent'] = ua.random

request_bod = requests.get(url=API_ENDPOINT, headers=headers)
len(request_bod.json())

pd.DataFrame(request_bod.json())
# https://xn--80az8a.xn--d1aqf.xn--p1ai/%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0/grapi/v1/geoObjects
