#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
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

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db' and
    os.getenv('HBNB_ENV') == 'test', "HBNB_ENV=test not set")
class TestDBStorage2(unittest.TestCase):
    """
    Tests for DBStorage inside the DB
    """
    @classmethod
    def setUpClass(cls):
        db_conf = {
            'host': os.getenv('HBNB_MYSQL_HOST'),
            'port': 3306,
            'user': os.getenv('HBNB_MYSQL_USER'),
            'passwd': os.getenv('HBNB_MYSQL_PWD'),
            'db': os.getenv('HBNB_MYSQL_DB'),
        }
        print(db_conf)
        cls.store = DBStorage()
        cls.conn = MySQLdb.connect(**db_conf)

    def tearDownClass(self):
        self.conn.close()

    def setUp(self):
        self.store.reload()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.close()

    def test_State_create(self):
        """DBStorage are writing States in the DB?
        """
        name = 'Arizona'
        new_state = State(eval('name="{}"'.format(name)))
        self.store.new(new_state)
        self.store.save()
        self.cursor.execute('SELECT * FROM states WHERE name=%s', (name,))
        out = self.cursor.fetchall()
        self.assertGreater(len(out), 0)

