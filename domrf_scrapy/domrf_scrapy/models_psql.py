import json
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey

# from sqlalchemy.types import TEXT, VARCHAR, INTEGER, FLOAT, TIMESTAMP, ARRAY

from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, INTEGER, FLOAT
from sqlalchemy.dialects.postgresql import TIMESTAMP, ARRAY, BIGINT

from sqlalchemy.sql import select
from sqlalchemy.sql import exists


# Change postgres_domrf to localhost for queries
engine_test = create_engine('postgres://vtbuser:example@postgres_domrf:5432/domrf_test')
# engine_test = create_engine("sqlite:////Users/ilyaperepelitsa/quant/domrf/domrf_scrapy/domrf.db")
# engine_test = create_engine('postgres://postgres:qwerty123@localhost:5432/domrf')
Base_item = declarative_base()

class Developer(Base_item):
    __tablename__ = "developers"
    developer_group_id = Column(VARCHAR(20), primary_key = True)
    developer_group_name = Column(TEXT, nullable=False)
    developer_group_address = Column(TEXT, nullable=True)

    def __repr__(self):
        return "<Base_item(developer_group_id='%s', developer_group_name='%s',\
                            developer_group_address='%s')>"\
        %(self.developer_group_id, self.developer_group_name, self.developer_group_address)

class Region(Base_item):
    __tablename__ = "regions"
    region_id = Column(VARCHAR(20), primary_key = True)
    region_name = Column(TEXT, nullable=False)

    def __repr__(self):
        return "<Base_item(region_id='%s', region_name='%s')>"\
        %(self.region_id, self.region_name)


class DeveloperData(Base_item):
    __tablename__ = "developer_Data"
    id = Column(Integer, primary_key = True)
    developer_group_id = Column(VARCHAR(20), ForeignKey("developers.developer_group_id"), nullable=False)
    region_id = Column(VARCHAR(20), ForeignKey("regions.region_id"), nullable=False)
    startDate = Column(VARCHAR(20))
    endDate = Column(VARCHAR(20))

    total_living_floor_size = Column(INTEGER, nullable=True)
    appt_num = Column(INTEGER, nullable=True)
    object_count = Column(INTEGER, nullable=True)
    total_living_floor_size_pct = Column(FLOAT, nullable=True)
    typed_volume_pct = Column(FLOAT, nullable=True)
    rating = Column(INTEGER, nullable=True)

    def __repr__(self):
        return "<Base_item(id='%s', developer_group_id='%s',\
                        region_id='%s', startDate='%s'\
                        endDate='%s', total_living_floor_size='%s'\
                        appt_num='%s', object_count='%s'\
                        total_living_floor_size_pct='%s', typed_volume_pct='%s'\
                        rating='%s')>"\
        %(self.id, self.developer_group_id,
            self.region_id, self.startDate,
            self.endDate, self.total_living_floor_size,
            self.appt_num, self.object_count,
            self.total_living_floor_size_pct, self.typed_volume_pct,
            self.rating)

Base_item.metadata.create_all(engine_test)
Session_test = sessionmaker(bind = engine_test)
session_test = Session_test()


# q = session_test.query(DeveloperData).all()
# # # # session_test.rollback()
# # # q
# len(q)
