#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
        name = Column(String(128), nullable=False)
        __tablename__ = "cities"
    else:
        state_id = ""
        name = ""
