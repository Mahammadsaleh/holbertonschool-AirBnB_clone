#!/usr/bin/python3
"""
serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """File Storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
            for k in data:
                self.__objects[k] = BaseModel(**data[k])
        except FileNotFoundError:
            pass
