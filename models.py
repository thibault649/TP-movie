"""
model.py : database row <-> objet python
"""
from sqlalchemy import Table, Column, Integer, String, SmallInteger, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# association table play
play_association_table = Table('play', Base.metadata,
    Column('id_movie', Integer, ForeignKey('movies.id')),
    Column('id_actor', Integer, ForeignKey('stars.id'))
)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=250), nullable=False)
    year = Column(SmallInteger, nullable=False)
    duration = Column(SmallInteger, nullable=True)
    # Many to one relationship : director
    id_director = Column(Integer, ForeignKey('stars.id'), nullable=True)
    director = relationship('Star')
    # Many to many relationship : actors
    actors = relationship('Star', secondary=play_association_table)

class Star(Base):
    __tablename__ = "stars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=150), nullable=False)
    birthdate = Column(Date, nullable=True)
