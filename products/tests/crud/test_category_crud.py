from rest_framework.reverse import reverse
from products.models import Category
import pytest


pytestmark = pytest.mark.django_db


def test_category_list(client):
    response = client.get(reverse("categories-list"))
    assert response.status_code == 200


def test_category_create(client):
    client.post(reverse("categories-list"), {"name": "Category"})
    assert len(Category.objects.all()) == 1


def test_category_read(client):
    response = client.post(reverse("categories-list"), {"name": "Category 73"})
    category_id = response.data["id"]

    response = client.get(reverse("categories-detail", kwargs={"pk": category_id}))
    assert response.data["name"] == "Category 73"


def test_category_update(client):
    response = client.post(reverse("categories-list"), {"name": "Category 73"})
    category_id = response.data["id"]

    response = client.patch(reverse("categories-detail", kwargs={"pk": category_id}), {
        "name": "Category 37"
    }, content_type='application/json')

    assert response.data["name"] == "Category 37"


def test_category_delete(client):
    response = client.post(reverse("categories-list"), {"name": "Category"})
    category_id = response.data["id"]

    response = client.delete(reverse("categories-detail", kwargs={"pk": category_id}))

    assert response.status_code == 204
    assert len(Category.objects.filter(id=category_id)) == 0
