#!/usr/bin/python3

###############################################################################
# Item Catalog Database Populate
###############################################################################


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from loremipsum import get_sentences

###############################################################################


engine = create_engine('postgresql://catalog:arkantos@localhost:5432/catalog')
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


def populate_db_random():
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


def populate_db_food():
    default_user = User(name="Default User",
                        email="default@user.com",
                        picture='https://cdn.stocksnap.io/img-thumbs/960w/B3QV6RMDVT.jpg')
    session.add(default_user)

    # Pasta Category
    pasta = Category(name="Pasta")
    session.add(pasta)

    session.add(Item(name="Spaghetti",
                     description="Spaghetti is a long, thin, solid, cylindrical pasta. Spaghettoni is a thicker form "
                                 "of spaghetti, while capellini is a very thin spaghetti. It is a staple food of "
                                 "traditional Italian cuisine. Like other pasta, spaghetti is made of milled wheat "
                                 "and water and sometimes enriched with vitamins and minerals. Authentic Italian "
                                 "spaghetti is made from durum wheat semolina, but elsewhere it may be made with "
                                 "other kinds of flour. Typically the pasta is white because refined flour is used, "
                                 "but whole wheat flour may be added.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/1/12/Spaghetti_spiral%2C_2008.jpg",
                     category=pasta,
                     user=default_user))

    session.add(Item(name="Fettuccine",
                     description="Fettuccine is a type of pasta popular in Roman and Tuscan cuisine. It is a flat "
                                 "thick pasta made of egg and flour (usually one egg for every 100 g of flour), "
                                 "wider than but similar to the tagliatelle typical of Bologna. It is often eaten "
                                 "with sugo d'umido (beef ragù) and ragù di pollo (chicken ragù).",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fettucine1.JPG",
                     category=pasta,
                     user=default_user))

    session.add(Item(name="Lasagne",
                     description="Lasagne are a type of wide, flat pasta, possibly one of the oldest types of pasta. "
                                 "Lasagne, or the singular lasagna, commonly refers to a culinary dish made with "
                                 "stacked layers of pasta alternated with sauces and ingredients such as meats, "
                                 "vegetables and cheese, and sometimes topped with melted grated cheese. Typically, "
                                 "the cooked pasta is assembled with the other ingredients and then baked in an oven. "
                                 "The resulting lasagne casserole is cut into single-serving square portions.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/1/1e/Lasagne.png",
                     category=pasta,
                     user=default_user))

    session.add(Item(name="Tagliatelle",
                     description="Tagliatelle and tagliolini (from the Italian tagliare, meaning 'to cut') are a "
                                 "traditional type of pasta from the Emilia-Romagna and Marche regions of Italy. "
                                 "Individual pieces of tagliatelle are long, flat ribbons that are similar in shape "
                                 "to fettuccine and are typically about 6.5 to 10 mm (0.26 to 0.39 in) wide. "
                                 "Tagliatelle can be served with a variety of sauces, though the classic is a meat "
                                 "sauce or Bolognese sauce. Tagliolini is another variety of tagliatelle that is long "
                                 "and cylindrical in shape, not long and flat.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/0/02/Tagliatelles2.jpg",
                     category=pasta,
                     user=default_user))

    session.add(Item(name="Fusilli",
                     description="Fusilli are a variety of pasta that are formed into corkscrew or helical shapes. "
                                 "The word fusilli presumably comes from fuso ('spindle'), as traditionally it is "
                                 "'spun' by pressing and rolling a small rod over the thin strips of pasta to wind "
                                 "them around it in a corkscrew shape.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Fusilli_lunghi_bucati.jpg",
                     category=pasta,
                     user=default_user))

    session.add(Item(name="Penne",
                     description="Penne is a type of pasta with cylinder-shaped pieces. Penne is the plural form of "
                                 "the Italian penna (meaning feather but pen as well), deriving from Latin penna ("
                                 "meaning 'feather' or 'quill'), and is a cognate of the English word pen. When this "
                                 "format was created in the 19th century it was supposed to imitate the fountain "
                                 "pen's steel nibs.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/0/0b/Pennelisce_closeup.png",
                     category=pasta,
                     user=default_user))

    session.add(Item(name="Rigatoni",
                     description="Rigatoni are a form of tube-shaped pasta of varying lengths and diameters "
                                 "originating in Italy. They are larger than penne and ziti, and sometimes "
                                 "slightly curved, though nowhere near as curved as elbow macaroni. Rigatoni "
                                 "characteristically have ridges down their length, sometimes spiraling around the "
                                 "tube, and unlike penne, rigatoni's ends are cut square (perpendicular) to the tube "
                                 "walls instead of diagonally.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Rigatoni.jpg",
                     category=pasta,
                     user=default_user))

    # Bread Category
    bread = Category(name="Bread")
    session.add(bread)

    session.add(Item(name="Zopf",
                     description="Zopf or Züpfe is a type of Swiss, Austrian or Bavarian bread made from white flour, "
                                 "milk, eggs, butter and yeast. The dough is brushed with egg yolk before baking, "
                                 "lending it its golden crust. It is baked in the form of a plait and traditionally "
                                 "eaten on Sunday mornings. A variant from Swabia is known as a Hefekranz (also: "
                                 "Hefezopf), and is distinguished from the Zopf in being sweet. The name 'Zopf' is "
                                 "derived from the shape of the bread, and literally means 'braid'.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/9/9c/Zopf.jpg",
                     category=bread,
                     user=default_user))

    session.add(Item(name="Bagel",
                     description="A bagel, also spelled beigel, is a bread product originating in the Jewish "
                                 "communities of Poland. It is traditionally shaped by hand into the form of a ring "
                                 "from yeasted wheat dough, roughly hand-sized, that is first boiled for a short time "
                                 "in water and then baked. The result is a dense, chewy, doughy interior with a "
                                 "browned and sometimes crisp exterior. Bagels are often topped with seeds baked on "
                                 "the outer crust, with the traditional ones being poppy or sesame seeds. Some may "
                                 "have salt sprinkled on their surface, and there are different dough types, "
                                 "such as whole-grain or rye.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Bagel-Plain-Alt.jpg",
                     category=bread,
                     user=default_user))

    session.add(Item(name="Baguette",
                     description="A baguette is a long, thin loaf of French bread that is commonly made from basic "
                                 "lean dough (the dough, though not the shape, is defined by French law). It is "
                                 "distinguishable by its length and crisp crust. A baguette has a diameter of about 5 "
                                 "or 6 cm (2-2.3 in) and a usual length of about 65 cm (26 in), although a baguette "
                                 "can be up to 1 m (39 in) long.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/f/f5/Baguettes_-_stonesoup.jpg",
                     category=bread,
                     user=default_user))

    session.add(Item(name="Brioche",
                     description="Brioche is a pastry of French origin that is similar to a highly enriched bread, "
                                 "and whose high egg and butter content (400 grams for each kilogram of flour) give "
                                 "it a rich and tender crumb. Chef Joël Robuchon describes it as 'light and slightly "
                                 "puffy, more or less fine, according to the proportion of butter and eggs'. It has a "
                                 "dark, golden, and flaky crust, frequently accentuated by an egg wash applied after "
                                 "proofing.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/4/4a/Brioche.jpg",
                     category=bread,
                     user=default_user))

    session.add(Item(name="Ciabatta",
                     description="Ciabatta (literally 'slipper') is an Italian white bread made from wheat flour, "
                                 "water, olive oil, salt, and yeast, created in 1982 by a baker in Verona, Veneto, "
                                 "Italy, in response to the popularity of French baguettes. Ciabatta is somewhat "
                                 "elongated, broad, and flat, and is baked in many variations.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Ciabatta_cut.JPG",
                     category=bread,
                     user=default_user))

    session.add(Item(name="Bazlama",
                     description="Bazlama is a single-layered, flat, circular and leavened bread with a creamy yellow "
                                 "colour, found in Turkey. It has an average thickness of 2 cm and diameters ranging "
                                 "from 10 to 25 cm. This popular flatbread is made from wheat flour, water, "
                                 "salt and yeast. After mixing and two to three hours fermentation, 200- to 250-gram "
                                 "pieces of dough are divided, rounded, sheeted to a desired thickness and baked on a "
                                 "hot plate. During baking, the bread is turned over to bake the other side. After "
                                 "baking, it is generally consumed fresh. Shelf life of bazlama varies from several "
                                 "hours to a few days, depending on storage conditions.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Bazlama.jpg",
                     category=bread,
                     user=default_user))

    # Cake Category
    cake = Category(name="Cake")
    session.add(cake)

    session.add(Item(name="Panettone",
                     description="Panettone is an Italian type of sweet bread loaf originally from Milan, usually "
                                 "prepared and enjoyed for Christmas and New Year in Western, Southern, "
                                 "and Southeastern Europe as well as in the Horn of Africa, and to a lesser extent in "
                                 "former French, Spanish, and Portuguese colonies.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Panettone_-_Nicolettone_2017_"
                               "-_IMG_7085_%2831752542285%29.jpg",
                     category=cake,
                     user=default_user))

    session.add(Item(name="Bibingka",
                     description="Bibingka is a type of baked rice cake from the Philippines and in Christian "
                                 "communities in Indonesia. It is usually eaten for breakfast, especially during the "
                                 "Christmas season. It is traditionally cooked in clay pots lined with leaves. It is "
                                 "a subtype of kakanin (rice cakes) in Philippine cuisine.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Bebinca.jpg",
                     category=cake,
                     user=default_user))

    session.add(Item(name="Black Forest Gateau",
                     description="Black Forest gâteau (British English) or Black Forest cake (American English) is a "
                                 "chocolate sponge cake with a rich cherry filling based on the German dessert "
                                 "Schwarzwälder Kirschtorte, literally 'Black Forest Cherry-torte'.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Black_Forest_gateau.jpg",
                     category=cake,
                     user=default_user))

    session.add(Item(name="Croquembouche",
                     description="A croquembouche or croque-en-bouche is a French dessert consisting of choux pastry "
                                 "balls piled into a cone and bound with threads of caramel. In Italy and France, "
                                 "it is often served at weddings, baptisms and first communions.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/a/a0/Croquembouche_wedding_cake.jpg",
                     category=cake,
                     user=default_user))

    session.add(Item(name="Tiramisu",
                     description="Tiramisu is a coffee-flavoured Italian dessert. It is made of ladyfingers ("
                                 "savoiardi) dipped in coffee, layered with a whipped mixture of eggs, sugar, "
                                 "and mascarpone cheese, flavoured with cocoa. The recipe has been adapted into many "
                                 "varieties of cakes and other desserts.[2] Its origins are often disputed among "
                                 "Italian regions of Veneto, Friuli-Venezia Giulia, Piedmont, and others.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc"
                               "/Tiramisu_with_blueberries_and_raspberries%2C_July_2011.jpg",
                     category=cake,
                     user=default_user))

    # Cheese Category
    cheese = Category(name="Cheese")
    session.add(cheese)

    session.add(Item(name="Feta",
                     description="Feta is a brined curd white cheese made in Greece from sheep's milk or from a "
                                 "mixture of sheep and goat's milk. Similar brined white cheeses are often made "
                                 "partly or wholly of cow's milk, and they are sometimes also called feta. It is a "
                                 "crumbly aged cheese, commonly produced in blocks, and has a slightly grainy "
                                 "texture. Feta is used as a table cheese, as well as in salads (e.g. the Greek "
                                 "salad) and pastries.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/Feta_Cheese.jpg",
                     category=cheese,
                     user=default_user))

    session.add(Item(name="Appenzeller Cheese",
                     description="Appenzeller cheese is a hard cow's-milk cheese produced in the Appenzell region of "
                                 "northeast Switzerland, such as the canton of Appenzell Innerrhoden, "
                                 "Appenzell Ausserrhoden, St. Gallen and Thurgau.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/Appenzeller_%28cheese%29.jpg",
                     category=cheese,
                     user=default_user))

    session.add(Item(name="Emmental Cheese",
                     description="Emmental (Emmentaler or Emmenthal) is a yellow, medium-hard Swiss cheese that "
                                 "originated in the area around Emmental, Canton Bern. It has a savory, "
                                 "but mild taste. While the denomination 'Emmentaler Switzerland' is protected, "
                                 "'Emmentaler' alone is not; similar cheeses of other origins, especially from France "
                                 "and Bavaria and even Finland, are widely available and sold by that name. Emmental "
                                 "dates to the time of ancient history.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Emmental_015.jpg",
                     category=cheese,
                     user=default_user))

    session.add(Item(name="Mozzarella",
                     description="Mozzarella is a traditionally southern Italian spun paste dairy made with Italian "
                                 "buffalo's milk by the pasta filata method. Mozzarella received a Traditional "
                                 "Specialities Guaranteed certification from the European Union in 1998. This "
                                 "protection scheme requires that mozzarella sold in the European Union is produced "
                                 "according to a traditional recipe.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/5/57/Mozzarella_di_bufala3.jpg",
                     category=cheese,
                     user=default_user))

    session.add(Item(name="Cheddar Cheese",
                     description="Cheddar cheese is a relatively hard, off-white (or orange if spices such as annatto "
                                 "are added), sometimes sharp-tasting, natural cheese. Originating in the English "
                                 "village of Cheddar in Somerset, cheeses of this style are produced beyond the "
                                 "region and in several countries around the world.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Somerset-Cheddar.jpg",
                     category=cheese,
                     user=default_user))

    # Stew Category
    stew = Category(name="Stew")
    session.add(stew)

    session.add(Item(name="Ratatouille",
                     description="Ratatouille is a French Provençal stewed vegetable dish, originating in Nice, "
                                 "and sometimes referred to as ratatouille niçoise. The modern ratatouille – tomatoes "
                                 "as a foundation for sautéed garlic, onions, zucchini, eggplant, bell peppers, "
                                 "marjoram, fennel and basil, or bay leaf and thyme, or a mix of green herbs like "
                                 "herbes de Provence.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Ratatouille-Dish.jpg",
                     category=stew,
                     user=default_user))

    session.add(Item(name="Bamia",
                     description="Bamia or bamia bi-lahm, is a Middle Eastern stew prepared using lamb, okra and "
                                 "tomatoes as primary ingredients. Additional ingredients used include tomato sauce, "
                                 "onion, garlic, cilantro (coriander), vegetable oil, cardamom, salt and pepper. In "
                                 "Egypt, sinew (tendons) of lamb are typically used, which can endure long cooking "
                                 "times. Ta'aleya, an Egyptian garlic sauce, is used as an ingredient to add flavor "
                                 "to Bamia. The word 'bamia' itself is simply the Arabic word for okra.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Bamia-Ocras_tomate.JPG",
                     category=stew,
                     user=default_user))

    session.add(Item(name="Goulash",
                     description="Goulash is a stew of meat, usually seasoned with paprika and other spices. "
                                 "Originating from the medieval Hungary, goulash is a popular meal predominantly "
                                 "eaten in Central Europe but also in other parts of Europe. Goulash can be prepared "
                                 "from beef, veal,[10] pork, or lamb. Typical cuts include the shank, shin, "
                                 "or shoulder; as a result, goulash derives its thickness from tough, well-exercised "
                                 "muscles rich in collagen, which is converted to gelatin during the cooking process.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/0/0a/2009-09-gulasch-p%C3%B6rk%C3%B6lt"
                               "-paprikas-3.jpg",
                     category=stew,
                     user=default_user))

    session.add(Item(name="Bigos",
                     description="Bigos, often translated into English as hunter's stew, is a Polish dish of chopped "
                                 "meat of various kinds stewed with sauerkraut and shredded fresh cabbage. The dish "
                                 "is also traditional for Belarusian, Ukrainian and Lithuanian cuisine.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Bigos_in_Krak%C3%B3w.jpg",
                     category=stew,
                     user=default_user))

    session.add(Item(name="Bouillabaisse",
                     description="Bouillabaisse is a traditional Provençal fish stew originating from the port city "
                                 "of Marseille. The French and English form bouillabaisse comes from the Provençal "
                                 "Occitan word bolhabaissa, a compound that consists of the two verbs bolhir (to "
                                 "boil) and abaissar (to reduce heat, i.e., simmer).",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Bullabessa.jpg",
                     category=stew,
                     user=default_user))

    # Sausage Category
    sausage = Category(name="Sausage")
    session.add(sausage)

    session.add(Item(name="Chorizo",
                     description="Chorizo or chouriço is a type of pork sausage. Traditionally, it uses natural "
                                 "casings made from intestines, a method used since Roman times. In Europe, "
                                 "chorizo is a fermented, cured, smoked sausage, which may be sliced and eaten "
                                 "without cooking, or added as an ingredient to add flavor to other dishes. "
                                 "Elsewhere, some sausages sold as chorizo may not be fermented and cured, "
                                 "and require cooking before eating. Spanish chorizo and Portuguese chouriço get "
                                 "their distinctive smokiness and deep red color from dried, smoked, red peppers",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/9/93/Chorizo_%284776711673%29.jpg",
                     category=sausage,
                     user=default_user))

    session.add(Item(name="Saucisson",
                     description="Saucisson, or 'saucisson sec,' is a variety of thick, dry cured sausage that "
                                 "originates in France. Similar sausages are called Salchichón in Spain. Typically "
                                 "made of pork, or a mixture of pork and other meats, saucisson are a type of "
                                 "charcuterie similar to salami or summer sausage.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/9/90/Saucisson_04.JPG",
                     category=sausage,
                     user=default_user))

    session.add(Item(name="Skilandis",
                     description="Skilandis or Kindziukas is a Lithuanian matured sausage made of meat, fat, salt, "
                                 "pepper and garlic. The ground meat is traditionally pressed into a pig's stomach or "
                                 "bladder, but today may be contained in other skins. The sausage is dried and "
                                 "cold-smoked. Skilandis dates back to at least the 16th century - the word skilandis "
                                 "is referred to in documents from various locations across the Grand Duchy of "
                                 "Lithuania as early as in the 16th-18th centuries.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/2/25/Skilandis2.jpg",
                     category=sausage,
                     user=default_user))

    session.add(Item(name="Braadworst",
                     description="A braadworst or verse worst is a large Dutch sausage, most often composed of pork "
                                 "for its meat to fat ratio, although beef or veal can be used too. The meat is "
                                 "spiced with pepper and nutmeg, but other spices and herbs such as cloves, sage, "
                                 "fennel seed, coriander seed, or juniper berries can be used in addition. Along with "
                                 "rookworst it is the most common sausage served along most varieties of stamppot but "
                                 "is eaten with other dishes as well and can be found throughout the Netherlands and "
                                 "Flanders.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Braadworst.jpg",
                     category=sausage,
                     user=default_user))

    session.add(Item(name="Wurstebrei",
                     description="Wurstebrei is a German dish from Westphalia which is "
                                 "similar to Grützwurst or Knipp. It consists of barley groats cooked in sausage "
                                 "juices (Wurstbrühe), which are enriched with pieces of meat, offal, such as heart, "
                                 "kidney or liver and seasoned with spices and salt. More rarely, finely chopped "
                                 "onions are added. The cooked ingredients are minced after the juices have been "
                                 "poured off and a crumbly cake is left which is held together with fat and which "
                                 "sets on cooling. There are various recipes, but they all contain barley groats, "
                                 "fat and meat.",
                     image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/Wurstebrei-1.jpg",
                     category=sausage,
                     user=default_user))

    session.commit()


###############################################################################


if __name__ == '__main__':
    clear_db()
    populate_db_food()
