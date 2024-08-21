#!/usr/bin/python3
"""SQLAlchemy storage class for HBNB project."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Interacts with the MySQL database using SQLAlchemy."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine and drops tables in test environment."""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}',
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database session.
        
        Args:
            cls: Optional class to filter results.

        Returns:
            Dictionary of objects in the format <class name>.<object id>.
        """
        result_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query_results = self.__session.query(cls).all()
            for obj in query_results:
                key = f"{type(obj).__name__}.{obj.id}"
                result_dict[key] = obj
        else:
            for model_class in [State, City, User, Place, Review, Amenity]:
                query_results = self.__session.query(model_class).all()
                for obj in query_results:
                    key = f"{type(obj).__name__}.{obj.id}"
                    result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits the current session to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database, creating tables and starting a session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the current session."""
        self.__session.remove()

