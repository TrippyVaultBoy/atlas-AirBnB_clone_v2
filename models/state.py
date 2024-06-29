#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import os
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
        name = Column(String(128), nullable=False)
        __tablename__ = "states"
    else:
        name = ""
        cities = []

    @property
    def cities(self):
        """Getter for cities"""
        cities = []
        for city in models.storage.all("City").values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
