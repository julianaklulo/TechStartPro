# Olist - Tech Start Pro

This repository contains an application for a catalog to store products data.

It's a REST API that can also be accessed through a web browseable API, developed using Python, Django and Django REST Framework.

### Setup Instructions
1. Clone this repository
```bash
$ git clone https://github.com/julianaklulo/TechStartPro.git
```
2. Move into the folder
```bash
$ cd TechStartPro
```
3. Create the virtualenv and install the dependencies
```bash
$ pipenv install
```
4. Activate the created virtualenv
```bash
$ pipenv shell
```
5. Migrate the database
```bash
(TechStartPro) $ python manage.py migrate
```
6. Start the server
```bash
(TechStartPro) $ python manage.py runserver
```

### Testing Instructions
The tests were written using `pytest`. To run, type
```bash
(TechStartPro) $ pytest
```

### API Documentation
Each product has a name, description, price and a list of categories, and each category has a name.

The categories' data can also be imported into the database using a CSV file.

To import from file, create a .csv formatted as:
```
name
category
another_category
also_a_category

```

Then, run
```bash
$ python manage.py import_categories categories.csv
```

#### Endpoints for Categories

Method |  Endpoint  | Description
-------|------------|------------
POST | **/categories/** | Create a category on database. 
GET | **/categories/** | Return a list containing all categories' information (paginated, 10 categories per page).
GET | **/categories/?name=[** name_to_search **]** | Search for categories whose name contains the "name_to_search" string.
GET | **/categories/[** id **]/** | Retrieve information of the category with the specified id.
PATCH, PUT | **/categories/[** id **]/** | Update the category information with the specified id.
DELETE |  **/categories/[** id **]/** | Delete the category with the specified id.

Payload for POST:
```
{
    "name": // name of the category
}
```

#### Endpoints for Products

Method |  Endpoint  | Description
-------|------------|------------
POST | **/products/** | Create a product on database. 
GET | **/products/** | Return a list containing all products' information (paginated, 10 products per page).
GET | **/products/?name=[** name **]&description=[** description **]&price=[** price **]&categories__name=[** category_name **]** | Search for products that match the query params (any combination of the parameters can be used for filtering).
GET | **/products/[** id **]/** | Retrieve information of the product with the specified id.
PATCH, PUT |  **/products/[** id **]/** | Update the product information with the specified id.
DELETE |  **/products/[** id **]/** | Delete the product with the specified id.

Payload for POST:
```
 {
    "name": // Name of the product
    "description": // Description of the product
    "price": // Price of the product
    "categories": // List of categories ids
}
```


### Work environment
**Operating system:** Arch Linux

**IDE:** Visual Studio Code

**Python version:** 3.8.6

**Virtual environmnet:** pipenv

**Libraries:**
* Django
* Django REST Framework
* django-filter *to create custom filters*
* Pytest *to test the application*

**DBMS:** SQLite3
