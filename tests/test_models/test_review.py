#!/usr/bin/python3
"""test for review"""
import unittest
import os
from models.city import City
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Armando"
        cls.user.last_name = "Casas"
        cls.user.id = "10"
        cls.user.email = "123@aoeu.com"
        cls.user.password = "apasswd"
        cls.user.save()

        cls.state = State(name="New Mexico", id="22")
        cls.state.save()

        cls.city = City()
        cls.city.name = "Farmington"
        cls.city.state_id = "22"
        cls.city.save()

        cls.place = Place()
        cls.place.id = "99"
        cls.place.city_id = "24"
        cls.place.user_id = "10"
        cls.place.name = "Rest"
        cls.place.description = "Good place to rest"
        cls.place.number_rooms = 100000
        cls.place.number_bathrooms = 3
        cls.place.max_guest = 5986
        cls.place.price_by_night = 30
        cls.place.latitude = 100.0
        cls.place.longitude = 10.0
        cls.place.save()

        cls.rev = Review()
        cls.rev.place_id = "99"
        cls.rev.user_id = "10"
        cls.rev.text = "Good place"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def test_save_Review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
