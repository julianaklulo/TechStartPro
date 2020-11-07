from rest_framework.reverse import reverse
from products.models import Product
from decimal import Decimal
import pytest


pytestmark = pytest.mark.django_db


def test_product_list(client):
    response = client.get(reverse("products-list"))
    assert response.status_code == 200


def test_product_create(client):
    response = client.post(reverse("categories-list"), {"name": "Category 1"})
    category_id = response.data["id"]

    client.post(reverse("products-list"), {
        "name": "Product",
        "description": "Random product",
        "price": 26.00,
        "categories": category_id
    })
    assert len(Product.objects.all()) == 1


def test_product_read(client):
    response = client.post(reverse("categories-list"), {"name": "Category 1"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "Another random product",
        "price": 45.00,
        "categories": category_id
    })
    product_id = response.data["id"]

    response = client.get(reverse("products-detail", kwargs={"pk": product_id}))
    assert response.data["name"] == "Product 1"
    assert response.data["description"] == "Another random product"
    assert Decimal(response.data["price"]) == Decimal(45.00)
    assert response.data["categories"][0] == category_id


def test_product_update(client):
    response = client.post(reverse("categories-list"), {"name": "Category 1"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "Awesome product",
        "price": 8.00,
        "categories": category_id
    })
    product_id = response.data["id"]

    response = client.patch(reverse("products-detail", kwargs={"pk": product_id}), {
        "name": "Product 2"
    }, content_type='application/json')

    assert response.data["name"] == "Product 2"


def test_product_delete(client):
    response = client.post(reverse("categories-list"), {"name": "Category 1"})
    category_id = response.data["id"]

    response = client.post(reverse("products-list"), {
        "name": "Product 1",
        "description": "One product to rule them all",
        "price": 50.00,
        "categories": category_id
    })
    product_id = response.data["id"]

    response = client.delete(reverse("products-detail", kwargs={"pk": product_id}))

    assert response.status_code == 204
    assert len(Product.objects.filter(id=product_id)) == 0
