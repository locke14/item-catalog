#!/usr/bin/python3

###############################################################################
# Item Catalog Database Populate
###############################################################################


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from loremipsum import get_sentences

###############################################################################


engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###############################################################################


CATEGORY_NAME = 'Category {}'
ITEM_NAME = 'Item {} of Category {}'

NUM_CATEGORIES = 5
NUM_ITEMS_PER_CATEGORY = 3
ITEM_DESCRIPTION_NUM_SENTENCES = 50

###############################################################################


def clear_db():
    session.query(Item).delete()
    session.query(Category).delete()
    session.commit()

###############################################################################


def populate_db():

    default_user = User(name="Default User",
                        email="default@user.com",
                        picture='https://cdn.stocksnap.io/img-thumbs/960w/B3QV6RMDVT.jpg')
    session.add(default_user)
    session.commit()

    for c in range(NUM_CATEGORIES):
        category = Category(name=CATEGORY_NAME.format(c + 1))
        session.add(category)
        session.commit()

        for p in range(NUM_ITEMS_PER_CATEGORY):
            name = ITEM_NAME.format(p + 1, c + 1)
            description = get_sentences(ITEM_DESCRIPTION_NUM_SENTENCES)
            item = Item(name=name,
                        description='. '.join(description),
                        category=category,
                        user=default_user)

            session.add(item)
            session.commit()

###############################################################################


if __name__ == '__main__':
    clear_db()
    populate_db()
