"""This module defines a class to store data with SQLAlchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
import models.base_model
from models.base_model import Base
import models.state
import models.city
import models.user
import models.place
import models.amenity
import models.review


class DBStorage:
    """This class manages data storage for a SQL Database"""
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = os.getenv(HBNB_MYSQL_USER)
        HBNB_MYSQL_PWD = os.getenv(HBNB_MYSQL_PWD)
        HBNB_MYSQL_HOST = os.getenv(HBNB_MYSQL_HOST)
        HBNB_MYSQL_DB = os.getenv(HBNB_MYSQL_DB)
        HBNB_ENV = os.getenv(HBNB_ENV)
        self.__engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db', pool_pre_ping=True)

        if os.getenv(HBNB_ENV) == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):)


