"""
Write tests — Milestone 4: POST / PUT / PATCH / DELETE + payloads.

Target API: https://jsonplaceholder.typicode.com

Note: JSONPlaceholder *fakes* writes (does not really store data).
We assert status codes + response body echo — not "GET after POST".
"""

from __future__ import annotations

import pytest

from utils.api_client import ApiClient
from utils.payload_loader import load_payload


# ---------------------------------------------------------------------------
# POST — create
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "payload_file",
    ["create_post.json", "create_post_alt.json"],
)
def test_create_post_returns_201_and_echoes_body(
    api_client: ApiClient,
    payload_file: str,
):
    """POST /posts — create a post from a JSON payload file."""
    payload = load_payload(payload_file)

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body  # server assigns an id (JSONPlaceholder: 101)


def test_create_user_returns_201(api_client: ApiClient):
    """POST /users — create a user from payload file."""
    payload = load_payload("create_user.json")

    response = api_client.post("/users", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["username"] == payload["username"]
    assert body["email"] == payload["email"]
    assert "id" in body


# ---------------------------------------------------------------------------
# PUT — full update (replace)
# ---------------------------------------------------------------------------


def test_update_post_with_put(api_client: ApiClient):
    """PUT /posts/1 — full update; response echoes the new body."""
    payload = load_payload("update_post.json")

    response = api_client.put("/posts/1", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_put_post_keeps_requested_id(api_client: ApiClient, post_id: int):
    """PUT /posts/{id} — id in path is reflected in the response."""
    payload = {
        "id": post_id,
        "title": f"Updated post {post_id}",
        "body": "Parametrized PUT body",
        "userId": 1,
    }

    response = api_client.put(f"/posts/{post_id}", json=payload)

    assert response.status_code == 200
    assert response.json()["id"] == post_id
    assert response.json()["title"] == payload["title"]


# ---------------------------------------------------------------------------
# PATCH — partial update
# ---------------------------------------------------------------------------


def test_patch_post_title_only(api_client: ApiClient):
    """PATCH /posts/1 — send only fields that change."""
    payload = load_payload("patch_post.json")

    response = api_client.patch("/posts/1", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == payload["title"]
    # Other fields still present on fake API response
    assert "userId" in body or "body" in body


# ---------------------------------------------------------------------------
# DELETE — remove
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("post_id", [1, 2, 50])
def test_delete_post(api_client: ApiClient, post_id: int):
    """DELETE /posts/{id} — successful delete returns 200 on this demo API."""
    response = api_client.delete(f"/posts/{post_id}")

    assert response.status_code == 200
    # JSONPlaceholder returns {} for DELETE
    assert response.json() == {}


def test_delete_user(api_client: ApiClient):
    """DELETE /users/1 — same pattern for users resource."""
    response = api_client.delete("/users/1")

    assert response.status_code == 200
