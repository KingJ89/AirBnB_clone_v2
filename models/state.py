#!/usr/bin/python3
"""State class for the HBNB project."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City


class State(BaseModel, Base):
    """Representation of a State.

    Attributes:
        name (str): Name of the state.
        cities (relationship): Relationship to City objects.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Returns the list of City instances associated with this State."""
        all_cities = models.storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]

