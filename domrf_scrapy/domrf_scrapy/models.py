import json
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, INTEGER
from sqlalchemy.dialects.postgresql import TIMESTAMP, ARRAY
from sqlalchemy.sql import select
from sqlalchemy.sql import exists

# import keys
# import pkg_resources
# json_path = pkg_resources.resource_filename('credentials', 'passwords.json')

# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# json_path = os.path.join(root_path, "credentials/passwords.json")

# data = json.load(open(json_path))

# json.loads(s)

# dataslap_postgres = data["aws"]["personal"]["dataslap"]["postgres"]["free_20gb"]["dataslap_user"]
# dataslap_postgres = keys.get_dataslap_postgres()


engine_test = create_engine('postgres://localhost:5432')
Base_item = declarative_base()

# class Url_entry(Base_item):
#     __tablename__ = "urls"
#     url_id = Column(INTEGER, primary_key = True)
#     url = Column(TEXT, unique = True)
#
#     def __repr__(self):
#         return "<Base_item(url_id='%s', url='%s')>"\
#         %(self.url_id, self.url)

class Developer(Base_item):
    __tablename__ = "developers"
    id = Column(INTEGER, primary_key = True)
    url_id = Column(INTEGER, ForeignKey("urls.url_id"), nullable=False)
    article_title = Column(TEXT)
    article_text = Column(TEXT)
    author_id = Column(ARRAY(INTEGER, dimensions=1), nullable=False)
    date_published = Column(TIMESTAMP)
    date_scraped = Column(TIMESTAMP) # '2016-06-22 19:10:25-07'
    source_id = Column(INTEGER, ForeignKey("sources.source_id"), nullable=False)

    def __repr__(self):
        return "<Base_item(url='%s', article_text='%s', author_id='%s',\
                            date_published='%s', date_scraped='%s', source_id='%s')>"\
        %(self.url, self.article_text, self.author_id,
            self.date_published, self.date_scraped, self.source_id)

class Author_entry(Base_item):
    __tablename__ = "authors"
    author_id = Column(INTEGER, primary_key = True)
    author_name = Column(VARCHAR(50), unique = True)

    def __repr__(self):
        return "<Base_item(author_id='%s', author_name='%s')>"\
        %(self.author_id, self.author_name)

class Source_entry(Base_item):
    __tablename__ = "sources"
    source_id = Column(INTEGER, primary_key = True)
    source_spider = Column(VARCHAR(20), unique = True)
    source_domain = Column(VARCHAR(50), unique = True)

    def __repr__(self):
        return "<Base_item(source_id='%s', source_spider='%s', source_domain='%s')>"\
        %(self.source_id, self.source_spider, self.source_domain)

Base_item.metadata.create_all(engine_test)
Session_test = sessionmaker(bind = engine_test)
session_test = Session_test()
