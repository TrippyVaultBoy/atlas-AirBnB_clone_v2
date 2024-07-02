#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import ForeignKey
import os
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Text


class Review(BaseModel):
    """ Review classto store review information """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(Text, nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
