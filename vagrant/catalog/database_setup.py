#!/usr/bin/python3

###############################################################################
# Item Catalog Database Setup
###############################################################################


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

###############################################################################


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

###############################################################################


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }

###############################################################################


class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(1000))
    image_url = Column(String(512))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def short_description(self):
        return self.description[:100] + '...'

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'id': self.id,
            'category_name': self.category.name,
            'user_name': self.user.name,
        }

###############################################################################


engine = create_engine('postgresql://catalog:arkantos@localhost:5432/catalog')
Base.metadata.create_all(engine)
