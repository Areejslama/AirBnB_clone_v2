#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {
                    key: vlaue
                    for key, value in self.__objects.items()
                    if isinstance(value, cls)
                    }
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        value = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[value] = obj

    def save(self):
        """save object to dictionary"""
        with open(FileStorage.__file_path, 'w') as f:
            my_list= {}
            my_list.update(FileStorage.__objects)
            for key, value in my_list.items():
                my_list[key] = value.to_dict()
            json.dump(my_list, f)

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
