#!/usr/bin/python3
"""this script define class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from sqlalchemy.exc import InvalidRequestError
from models.state import State
from models.user import User


class DBStorage:
    """represent the class"""
    __engine = None
    __session = None
    def __init__(self):
        """initializ engine"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        Host = getenv("HBNB_MYSQL_HOST")
        DB = getenv("HBNB_MYSQL_DB")
        url = "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                    passwd,
                                                    Host,
                                                    DB)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if ("HBNB_ENV") == "test":
            {
                    Base.metadata.drop_all(self.__engine)
            }

    def all(self, cls=None):
        """connect query session"""
        classes = [State, City, User, Amenity, Place, Review]
        my_objects = []
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            my_objects = self.__session.query(cls).all()
        else:
            for class_obj in classes:
                my_objects.extend(self.__session.query(class_obj).all())
        return {
            "{}.{}".format(type(obj).__name__, obj.id): obj
            for obj in objects
        }

    def new(self, obj):
        """add ibject to session"""
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj:
            self.__session.delete()
    def reload(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = session()
