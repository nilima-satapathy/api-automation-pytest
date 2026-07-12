"""
GET tests — Milestone 3: full GET coverage + parametrize.

Target API: https://jsonplaceholder.typicode.com (free, no auth)

What is parametrize?
  One test function + many input rows = many test cases.
  Same assertions, different data. Less copy-paste, clearer failures.
"""

from __future__ import annotations

import pytest

from utils.api_client import ApiClient


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------


def test_get_users_list_returns_200_and_data(api_client: ApiClient):
    """GET /users — list is a non-empty array of user objects."""
    response = api_client.get("/users")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert "id" in body[0]
    assert "email" in body[0]
    assert "name" in body[0]


@pytest.mark.parametrize("user_id", [1, 2, 3, 5, 10])
def test_get_single_user_by_id(api_client: ApiClient, user_id: int):
    """GET /users/{id} — each known id returns that user with core fields."""
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert "email" in user
    assert "name" in user
    assert "username" in user
    assert "@" in user["email"]


@pytest.mark.parametrize(
    "user_id, expected_username",
    [
        (1, "Bret"),
        (2, "Antonette"),
        (3, "Samantha"),
    ],
)
def test_get_user_expected_username(
    api_client: ApiClient,
    user_id: int,
    expected_username: str,
):
    """GET /users/{id} — known fixture data matches public demo usernames."""
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["username"] == expected_username


# ---------------------------------------------------------------------------
# Posts
# ---------------------------------------------------------------------------


def test_get_posts_list_returns_array(api_client: ApiClient):
    """GET /posts — list endpoint returns many posts."""
    response = api_client.get("/posts")

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) >= 100  # JSONPlaceholder ships 100 posts
    assert "userId" in posts[0]
    assert "title" in posts[0]
    assert "body" in posts[0]


@pytest.mark.parametrize("post_id", [1, 2, 50, 100])
def test_get_single_post_by_id(api_client: ApiClient, post_id: int):
    """GET /posts/{id} — single post has id, userId, title, body."""
    response = api_client.get(f"/posts/{post_id}")

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert "userId" in post
    assert isinstance(post["title"], str) and len(post["title"]) > 0
    assert isinstance(post["body"], str) and len(post["body"]) > 0


@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_get_posts_filtered_by_user_id(api_client: ApiClient, user_id: int):
    """GET /posts?userId=N — every item belongs to that user."""
    response = api_client.get("/posts", params={"userId": user_id})

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all(post["userId"] == user_id for post in posts)


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_nested_user_posts(api_client: ApiClient, user_id: int):
    """GET /users/{id}/posts — nested route returns that user's posts."""
    response = api_client.get(f"/users/{user_id}/posts")

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all(post["userId"] == user_id for post in posts)


# ---------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("post_id", [1, 2, 3, 10])
def test_get_comments_filtered_by_post_id(api_client: ApiClient, post_id: int):
    """GET /comments?postId=N — comments all reference that post."""
    response = api_client.get("/comments", params={"postId": post_id})

    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) > 0
    assert all(c["postId"] == post_id for c in comments)
    sample = comments[0]
    assert "email" in sample
    assert "body" in sample
    assert "@" in sample["email"]


@pytest.mark.parametrize("post_id", [1, 2, 5])
def test_get_nested_post_comments(api_client: ApiClient, post_id: int):
    """GET /posts/{id}/comments — nested comments route for a post."""
    response = api_client.get(f"/posts/{post_id}/comments")

    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) > 0
    assert all(c["postId"] == post_id for c in comments)


# ---------------------------------------------------------------------------
# Todos & albums (list shape checks)
# ---------------------------------------------------------------------------


def test_get_todos_list_shape(api_client: ApiClient):
    """GET /todos — list of todo items with completed flag."""
    response = api_client.get("/todos")

    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert len(todos) > 0
    sample = todos[0]
    assert "userId" in sample
    assert "title" in sample
    assert "completed" in sample
    assert isinstance(sample["completed"], bool)


@pytest.mark.parametrize("user_id", [1, 2, 5])
def test_get_todos_filtered_by_user_id(api_client: ApiClient, user_id: int):
    """GET /todos?userId=N — todos belong to that user."""
    response = api_client.get("/todos", params={"userId": user_id})

    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0
    assert all(t["userId"] == user_id for t in todos)


def test_get_albums_list_shape(api_client: ApiClient):
    """GET /albums — list of albums with userId + title."""
    response = api_client.get("/albums")

    assert response.status_code == 200
    albums = response.json()
    assert isinstance(albums, list)
    assert len(albums) > 0
    assert "userId" in albums[0]
    assert "title" in albums[0]
