#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60),nullable=False, primary_key=True) 
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())

        if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     kronos)
        else:
            self.created_at = datetime.now()

        if "updated_at" in kwargs:
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     kronos)
        else:
            self.updated_at = datetime.now()
        for keys, values in kwargs.items():
            if "__class__" not in keys:
                setattr(self, keys, values)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
