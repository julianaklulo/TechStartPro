from rest_framework.reverse import reverse
from decimal import Decimal
import pytest


pytestmark = pytest.mark.django_db


def test_product_search_by_name(client):
    response = client.post(reverse("categories-list"), {"name": "Very Good Category"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 10.00,
        "categories": category_id
    })

    response = client.post(reverse("products-list"), {
        "name": "Product 2",
        "description": "Yet another product",
        "price": 20.00,
        "categories": category_id
    })

    response = client.get(reverse("products-list"), {"name": "2"})
    for product in response.data["results"]:
        assert "2" in product["name"]


def test_product_search_by_description(client):
    response = client.post(reverse("categories-list"), {"name": "Very Good Category"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 10.00,
        "categories": category_id
    })

    response = client.post(reverse("products-list"), {
        "name": "Product 2",
        "description": "Yet another product",
        "price": 20.00,
        "categories": category_id
    })

    response = client.get(reverse("products-list"), {"description": "One product to rule them all"})
    for product in response.data["results"]:
        assert "One product to rule them all" in product["description"]


def test_product_search_by_price(client):
    response = client.post(reverse("categories-list"), {"name": "Very Good Category"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 10.00,
        "categories": category_id
    })

    response = client.post(reverse("products-list"), {
        "name": "Product 2",
        "description": "Yet another product",
        "price": 20.00,
        "categories": category_id
    })

    response = client.get(reverse("products-list"), {"price": 20.00})
    for product in response.data["results"]:
        assert Decimal(product["price"]) == Decimal(20.00)


def test_product_search_by_categories(client):
    response = client.post(reverse("categories-list"), {"name": "Very Good Category"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 10.00,
        "categories": category_id
    })

    response = client.post(reverse("products-list"), {
        "name": "Product 2",
        "description": "Yet another product",
        "price": 20.00,
        "categories": category_id
    })

    response = client.get(reverse("products-list"), {"categories__name": "Very Good Category"})
    for product in response.data["results"]:
        assert product["categories"] == [category_id]


def test_product_search_by_all_fields(client):
    response = client.post(reverse("categories-list"), {"name": "Very Good Category"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 10.00,
        "categories": category_id
    })

    response = client.post(reverse("products-list"), {
        "name": "Product 2",
        "description": "Yet another product",
        "price": 20.00,
        "categories": category_id
    })

    response = client.get(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 10.00,
        "categories__name": "Very Good Category"})

    for product in response.data["results"]:
        assert product["name"] == "Product 1"
        assert "One product to rule them all" in product["description"]
        assert Decimal(product["price"]) == Decimal(10.00)
        assert product["categories"] == [category_id]
