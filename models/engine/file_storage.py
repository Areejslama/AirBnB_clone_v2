#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary"""
        if cls:
            return {
                key: value
                for key, value in self.__objects.items()
                if isinstance(value, cls)
            }
        return self.__objects

    def new(self, obj):
        """add new object to dictionary"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """Save object to dict"""
        my_objects = {}
        for k, obj in self.__objects.items():
            my_objects[k] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(my_objects, file)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
        }
        try:
             with open(FileStorage.__file_path, 'r', encoding='UTF-8') as f:
                 temp = json.load(f)
                 for key, val in temp.items():
                     name = val['__class__']
                     my_obj = classes[name](**val)
                     self.new(my_obj)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
    
    def delete(self, obj=None):
        """method to delete objects"""
        if obj:
            item = "{}.{}".format(obj.__class.____name__, obj.id)
            if item in self.__objects:
                del self.__objects[item]
                self.save()

    def close(self):
        """method to close json file"""
        self.reload()
