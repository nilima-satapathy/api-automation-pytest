"""GET tests using the shared api_client fixture (Milestone 2).

Target API: https://jsonplaceholder.typicode.com (free, no auth).
"""

from utils.api_client import ApiClient


def test_get_users_list_returns_200_and_data(api_client: ApiClient):
    """GET /users — list endpoint returns a non-empty array of users."""
    response = api_client.get("/users")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert "id" in body[0]
    assert "email" in body[0]


def test_get_single_user_returns_expected_fields(api_client: ApiClient):
    """GET /users/1 — single user payload has id, email, name fields."""
    response = api_client.get("/users/1")

    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "email" in user
    assert "name" in user
    assert "username" in user
    assert "@" in user["email"]


def test_get_posts_filtered_by_user_id(api_client: ApiClient):
    """GET /posts?userId=1 — filtered list returns posts for that user."""
    response = api_client.get("/posts", params={"userId": 1})

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)
    assert "title" in posts[0]
    assert "body" in posts[0]
