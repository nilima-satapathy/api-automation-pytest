"""
Schema validation tests — Milestone 5.

Idea: status codes are not enough. Check that the JSON *shape*
matches our contract (required fields + types).

Schemas live in data/schemas/*.json
Helper: utils.schema_loader.validate_schema
"""

from __future__ import annotations

import pytest

from utils.api_client import ApiClient
from utils.schema_loader import load_schema, validate_schema


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------


def test_users_list_matches_schema(api_client: ApiClient):
    """GET /users — list items match user_list schema."""
    response = api_client.get("/users")
    assert response.status_code == 200

    schema = load_schema("user_list.json")
    validate_schema(response.json(), schema)


@pytest.mark.parametrize("user_id", [1, 2, 5])
def test_single_user_matches_schema(api_client: ApiClient, user_id: int):
    """GET /users/{id} — full user object matches user schema."""
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 200

    schema = load_schema("user.json")
    validate_schema(response.json(), schema)


# ---------------------------------------------------------------------------
# Posts
# ---------------------------------------------------------------------------


def test_posts_list_matches_schema(api_client: ApiClient):
    """GET /posts — list matches post_list schema."""
    response = api_client.get("/posts")
    assert response.status_code == 200

    schema = load_schema("post_list.json")
    validate_schema(response.json(), schema)


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_single_post_matches_schema(api_client: ApiClient, post_id: int):
    """GET /posts/{id} — post object matches post schema."""
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200

    schema = load_schema("post.json")
    validate_schema(response.json(), schema)


# ---------------------------------------------------------------------------
# Comments, todos, albums (sample item shape)
# ---------------------------------------------------------------------------


def test_comment_item_matches_schema(api_client: ApiClient):
    """GET /comments?postId=1 — first comment matches comment schema."""
    response = api_client.get("/comments", params={"postId": 1})
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0

    schema = load_schema("comment.json")
    validate_schema(comments[0], schema)


def test_todo_item_matches_schema(api_client: ApiClient):
    """GET /todos — first todo matches todo schema."""
    response = api_client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0

    schema = load_schema("todo.json")
    validate_schema(todos[0], schema)


def test_album_item_matches_schema(api_client: ApiClient):
    """GET /albums — first album matches album schema."""
    response = api_client.get("/albums")
    assert response.status_code == 200
    albums = response.json()
    assert len(albums) > 0

    schema = load_schema("album.json")
    validate_schema(albums[0], schema)


# ---------------------------------------------------------------------------
# Create response still has expected post fields (demo API)
# ---------------------------------------------------------------------------


def test_created_post_response_matches_post_schema(api_client: ApiClient):
    """
    POST /posts — response should still look like a post.

    Note: JSONPlaceholder returns id=101; schema requires id >= 1.
    """
    payload = {"title": "schema check", "body": "body", "userId": 1}
    response = api_client.post("/posts", json=payload)
    assert response.status_code == 201

    schema = load_schema("post.json")
    validate_schema(response.json(), schema)
