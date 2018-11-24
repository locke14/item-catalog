#!/usr/bin/python3

###############################################################################
# Product Catalog Database Setup
###############################################################################


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

###############################################################################


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

###############################################################################


class Product(Base):
    __tablename__ = 'product'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

###############################################################################


engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.create_all(engine)
