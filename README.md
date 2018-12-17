Project: Item Catalog
========================

The goal of this project is to develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

How to run the application?
----------------------------
- Install Vagrant and VirtualBox
- Launch the Vagrant VM (`vagrant up`)
- Go to the project directory (`cd /vagrant/catalog`)
- Install the python dependencies (`sudo pip3 install -r requirements.txt`)
- Create `client_secrets.json` and copy the file contents sent on project submission
- Setup the database (`python3 database_setup.py`)
- Populate the database (`python3 database_populate.py`)
- Run the application within the VM (`python3 application.py`)
- Access the application by visiting http://localhost:8000 locally 

Screenshots
-----------
**Home Page**
![Home](/screenshots/home.PNG)

**View Item**
![View Item](/screenshots/view_item.PNG)

**All Items**
![All Items 1](/screenshots/all_items_1.PNG)
![All Items 2](/screenshots/all_items_2.PNG)

**Items from a category**
![Category Items](/screenshots/category_items.PNG)

**Categories**
![Categories](/screenshots/categories.PNG)

**Add Item**
![Add Item](/screenshots/add_item.PNG)
