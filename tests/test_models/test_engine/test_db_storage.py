#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
import models
import MySQLdb
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Won't work in DB")
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    def test_State(self):
        """
        test state
        """
        state = State(name="California")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "California")

    def test_City(self):
        """
        test city
        """
        city = City(name="Miami")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Miami")

    def test_Place(self):
        """
        test place
        """
        place = Place(name="Dreams", number_rooms=3, number_bathrooms=2)
        if place.id in models.storage.all():
            self.assertTrue(place.name, "Dreams")
            self.assertTrue(place.number_rooms, 3)
            self.assertTrue(place.number_bathrooms, 2)

    def test_User(self):
        """
        test user
        """
        user = User(name="Dario", email="dario@gmail.com")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Dario")
            self.assertTrue(user.email, "dario@gmail.com")

    def test_Amenity(self):
        """
        test amenity
        """
        amenity = Amenity(name="Pool")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Pool")

    def test_Review(self):
        """
        test review
        """
        review = Review(text="Good place")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "Good place")

    def teardown(self):
        """
        cleaning the end
        """
        self.session.close()
        self.session.rollback()
