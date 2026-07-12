"""
Negative & edge-case tests — Milestone 6.

Happy-path tests prove the API works when input is good.
Negative tests prove we handle *bad* input the way we expect:

  - unknown IDs → 404
  - unknown routes → 404
  - filters with no matches → empty list (still 200 on this API)
  - invalid updates → error status (JSONPlaceholder quirk)

Target API: https://jsonplaceholder.typicode.com
Note: this is a *fake* API; some write errors differ from production APIs.
"""

from __future__ import annotations

import pytest

from utils.api_client import ApiClient


# ---------------------------------------------------------------------------
# 404 — resource does not exist
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "path",
    [
        "/users/999",
        "/users/0",
        "/posts/999",
        "/posts/0",
        "/comments/999",
        "/todos/999",
        "/albums/999",
    ],
)
def test_get_unknown_resource_returns_404(api_client: ApiClient, path: str):
    """GET unknown id → 404 and empty JSON object."""
    response = api_client.get(path)

    assert response.status_code == 404
    assert response.json() == {}


def test_get_unknown_route_returns_404(api_client: ApiClient):
    """GET a path that does not exist → 404."""
    response = api_client.get("/this-route-does-not-exist")

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.parametrize("user_id", [999, 0, -1])
def test_get_unknown_user_has_no_user_fields(api_client: ApiClient, user_id: int):
    """
    404 body must NOT look like a real user.

    Guards against APIs that wrongly return 200 + empty/partial objects.
    """
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 404
    body = response.json()
    assert "id" not in body
    assert "email" not in body
    assert "username" not in body


# ---------------------------------------------------------------------------
# Empty results (edge case — valid request, no data)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "resource, param, value",
    [
        ("/posts", "userId", 999),
        ("/todos", "userId", 999),
        ("/albums", "userId", 999),
        ("/comments", "postId", 999),
    ],
)
def test_filter_with_no_matches_returns_empty_list(
    api_client: ApiClient,
    resource: str,
    param: str,
    value: int,
):
    """
    Filter that matches nothing → 200 + [] (not an error).

    Important distinction:
      - bad URL / missing resource id → often 404
      - valid list endpoint, zero matches → often 200 + empty array
    """
    response = api_client.get(resource, params={param: value})

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert body == []


# ---------------------------------------------------------------------------
# Nested routes with unknown parent
# ---------------------------------------------------------------------------


def test_nested_posts_for_unknown_user_returns_empty_list(api_client: ApiClient):
    """GET /users/999/posts — fake API returns empty list (not always 404)."""
    response = api_client.get("/users/999/posts")

    # JSONPlaceholder returns 200 [] for nested lists of missing parents
    assert response.status_code == 200
    assert response.json() == []


def test_nested_comments_for_unknown_post_returns_empty_list(api_client: ApiClient):
    """GET /posts/999/comments — empty list when parent post is missing."""
    response = api_client.get("/posts/999/comments")

    assert response.status_code == 200
    assert response.json() == []


# ---------------------------------------------------------------------------
# Write-side edge cases (demo API behaviour)
# ---------------------------------------------------------------------------


def test_put_unknown_post_returns_server_error(api_client: ApiClient):
    """
    PUT /posts/999 — this demo API returns 500 (not a clean 404).

    Real production APIs often return 404/400 instead.
    We still lock the *observed* contract so regressions are visible.
    """
    payload = {
        "id": 999,
        "title": "should not exist",
        "body": "negative test",
        "userId": 1,
    }
    response = api_client.put("/posts/999", json=payload)

    assert response.status_code == 500


def test_delete_unknown_post_still_returns_200_on_demo_api(api_client: ApiClient):
    """
    DELETE /posts/999 — JSONPlaceholder fakes success (200 + {}).

    Documenting this teaches: never assume DELETE of missing id is 404
    without reading the API contract.
    """
    response = api_client.delete("/posts/999")

    assert response.status_code == 200
    assert response.json() == {}


def test_post_with_empty_body_still_accepted_by_demo_api(api_client: ApiClient):
    """
    POST /posts with {} — demo API still returns 201.

    Production APIs usually reject empty/invalid bodies (400).
    This test records the loose demo behaviour and keeps the suite honest.
    """
    response = api_client.post("/posts", json={})

    assert response.status_code == 201
    body = response.json()
    assert "id" in body  # server still assigns an id
