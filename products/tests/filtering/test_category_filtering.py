from rest_framework.reverse import reverse
import pytest


pytestmark = pytest.mark.django_db


def test_category_search_by_name(client):
    client.post(reverse("categories-list"), {"name": "Category 42"})

    response = client.get(reverse("categories-list"), {"name": "42"})
    assert response.data["results"][0]["name"] == "Category 42"
