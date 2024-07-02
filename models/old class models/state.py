#!/usr/bin/python3
""" State Module for HBNB project """
"""Now includes switch for new storage system"""
import models
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""
        cities = []

    @property
    def cities(self):
        """Getter for cities"""
        cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
