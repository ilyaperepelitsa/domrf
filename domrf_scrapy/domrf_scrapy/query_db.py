# domrf_scrapy
from domrf_scrapy.domrf_scrapy.models import *

# docker run --name domrf -e POSTGRES_PASSWORD=qwerty123 -e POSTGRES_USER=vtbuser -d postgres
docker run --name domrf -e POSTGES_USER=vtbuser -e POSTGRES_PASSWORD=qwerty123 -e POSTGRES_DB=domrf postgres

docker run --name postgres1 --network postgres-network -e POSTGRES_PASSWORD=qwerty123 -d postgres

docker network create --driver bridge postgres-network
docker run --name domrf -e POSTGRES_PASSWORD=qwerty123 -d postgres



docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres


q = (session_test.query(Trade_aggregation_entry).all())
