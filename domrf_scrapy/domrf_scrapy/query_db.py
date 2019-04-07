# domrf_scrapy
from domrf_scrapy.domrf_scrapy.models import *

# docker run --name domrf -e POSTGRES_PASSWORD=qwerty123 -e POSTGRES_USER=vtbuser -d postgres
docker run postgres -e 'POSTGES_USER=vtbuser' -e 'POSTGRES_PASSWORD=qwerty123' -e 'POSTGRES_DB=domrf'
