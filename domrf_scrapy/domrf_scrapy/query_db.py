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

q = (session_test.query(DeveloperData, Developer, Region)
            .filter(and_(Trade_aggregation_entry.reporter == query_params["reporter_id"],
                        Trade_aggregation_entry.trade_regime == query_params["trade_regime_id"],
                        Trade_aggregation_entry.classification == query_params["classification"],
                        Trade_aggregation_entry.aggregation_level == query_params["aggregation_level"]))
            .join(Trade_regime, Trade_aggregation_entry.trade_regime == Trade_regime.id)
            .join(Reporter, Trade_aggregation_entry.reporter == Reporter.id)
            .join(Partner, Trade_aggregation_entry.partner == Partner.id)
            .join(Quantity_code, Trade_aggregation_entry.quantity_code == Quantity_code.id)
            .join(Commodity_code_EN, Trade_aggregation_entry.commodity == Commodity_code_EN.id)
            .all())
