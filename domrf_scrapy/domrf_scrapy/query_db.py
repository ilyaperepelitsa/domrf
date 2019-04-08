# domrf_scrapy
from domrf_scrapy.domrf_scrapy.models_test import *

# # docker run --name domrf -e POSTGRES_PASSWORD=qwerty123 -e POSTGRES_USER=vtbuser -d postgres
# docker run --name domrf -e POSTGES_USER=vtbuser -e POSTGRES_PASSWORD=qwerty123 -e POSTGRES_DB=domrf postgres
#
# docker run --name postgres1 --network postgres-network -e POSTGRES_PASSWORD=qwerty123 -d postgres
#
# docker network create --driver bridge postgres-network
# docker run --name domrf -e POSTGRES_PASSWORD=qwerty123 -d postgres
#
#
#
# docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
#
import pandas as pd

def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    # if delete_id:
    #     dat.pop("num")
    return dat

q = (session_test.query(DeveloperData, Developer, Region)
            .join(Developer, DeveloperData.developer_group_id == Developer.developer_group_id)
            .join(Region, DeveloperData.region_id == Region.region_id)
            .all())
q

test_df = pd.concat([pd.DataFrame(list(map(lambda x: inst_to_dict(x[0]), q))),
                                pd.DataFrame(list(map(lambda x: inst_to_dict(x[1]), q))),
                                pd.DataFrame(list(map(lambda x: inst_to_dict(x[2]), q)))], axis = 1)
