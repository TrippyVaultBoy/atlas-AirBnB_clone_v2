#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        state_id = Column(String(60),ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
        __tablename__ = "cities"

        def state_id(self):
            """returns associated state id"""
            return self.state_id

        def state_id(self, value):
            """sets state id"""
            if not isinstance(value, str):
                raise TypeError("state_id must be a string")
            if len(value) > 60:
                raise ValueError("state_id cannot be longer than 60 characters")
            if not value.strip():
                raise ValueError("state_id cannot be empty")
            self._state_id = value.strip()

        def name(self):
            """returns name"""
            return self.name

        def name(self, value):
            """sets name"""
            if not isinstance(value, str):
                raise TypeError("name must be a string")
            if len(value) > 128:
                raise ValueError("name cannot be longer than 128 characters")
            if not value.strip():
                raise ValueError("name cannot be empty")
            self._name = value.strip()

    else:
        def __init__(self, *args, **kwargs):
            """initializes city"""
            super().__init__(*args, **kwargs)
            self.state_id = ""
            self.name = ""
