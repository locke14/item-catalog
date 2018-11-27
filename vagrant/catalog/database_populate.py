#!/usr/bin/python3

###############################################################################
# Product Catalog Database Populate
###############################################################################


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Product
from loremipsum import get_sentences

###############################################################################


engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###############################################################################


CATEGORY_NAME = 'Category {}'
PRODUCT_NAME = 'Product {} of Category {}'

NUM_CATEGORIES = 10
NUM_PRODUCTS_PER_CATEGORY = 25
PRODUCT_DESCRIPTION_NUM_SENTENCES = 5

###############################################################################


def clear_db():
    session.query(Product).delete()
    session.query(Category).delete()
    session.commit()

###############################################################################


def populate_db():

    for c in range(NUM_CATEGORIES):
        category = Category(name=CATEGORY_NAME.format(c))
        session.add(category)
        session.commit()

        for p in range(NUM_PRODUCTS_PER_CATEGORY):
            name = PRODUCT_NAME.format(p, c)
            description = get_sentences(PRODUCT_DESCRIPTION_NUM_SENTENCES)
            product = Product(name=name,
                              description='. '.join(description),
                              category=category)
            session.add(product)
            session.commit()

###############################################################################


if __name__ == '__main__':
    clear_db()
    populate_db()
