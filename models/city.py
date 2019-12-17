#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """
    Class that inherits from BaseModel and Base (respect the order)
    Attributes:
        __tablename__ : represents the table name
        state_id: The state id
        name: input name
    """

    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Places", passive_deleted=True, backref="cities")
    else:
        state_id = ""
        name = ""
