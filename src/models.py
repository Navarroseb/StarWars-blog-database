import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)
    
    


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(Integer())
    gender = Column(String(250))
    height = Column(Integer())
    
    

class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer,ForeignKey("Users"))
    Characters_id = Column(Integer,ForeignKey("Characters"))
    user = relationship("users.id")
    character = relationship("character.id")
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))
    users_id = Column(Integer, ForeignKey('users.id'))
    
    

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("Users"))
    Planets_id = Column(Integer, ForeignKey("Planets"))
    user = relationship("users.id")
    planets = relationship("planets.id")    

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    passengers_capacity = Column(Integer)
    pilots = Column(String(250))
    users_id = Column(Integer, ForeignKey("users.id"))
    

class Favorites_starships(Base):
    __tablename__ = 'favorites_starships'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("Users"))
    Starships_id = Column(Integer, ForeignKey("Starships"))
    user = relationship("users.id")
    starships = relationship("starships.id")    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')