#!/usr/bin/python3
"""This script defines the DBStorage class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Represents the DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        url = f"mysql+mysqldb://{user}:{passwd}@{host}/{db}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects"""
        my_objects = []
        classes = [State, City, User, Amenity, Place, Review]
        if cls is None:
             for cls_obj in classes:
                 my_objects.extend(self.__session.query(cls_obj).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
                my_objects = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in my_objects}

    def new(self, obj):
        """Add an object to the current database session."""
        if obj is not None:
            self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Reloads the database by creating all tables and setting up the session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """Close session."""
        self.__session.remove()
