#!/usr/bin/python3
"""
tracks a register of models used in the App
"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

models_dict = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
    'User': User
}

models_list = [val for val in models_dict.values()]
