#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        __tablename__ : represents the table name
        name: input name
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
