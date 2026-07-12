"""
Thin HTTP client for API tests.

M1: GET support + shared session defaults.
M4: POST / PUT / PATCH / DELETE for write operations.
"""

from __future__ import annotations

from typing import Any

import requests


class ApiClient:
    """Minimal wrapper around requests.Session for consistent API calls."""

    def __init__(
        self,
        base_url: str = "https://jsonplaceholder.typicode.com",
        timeout: float = 10.0,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                **(headers or {}),
            }
        )

    def _url(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send GET request and return the raw Response (assert in tests)."""
        return self.session.get(
            self._url(path),
            params=params,
            timeout=self.timeout,
            **kwargs,
        )

    def post(
        self,
        path: str,
        *,
        json: dict[str, Any] | list[Any] | None = None,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send POST (create) with a JSON body."""
        return self.session.post(
            self._url(path),
            json=json,
            params=params,
            timeout=self.timeout,
            **kwargs,
        )

    def put(
        self,
        path: str,
        *,
        json: dict[str, Any] | list[Any] | None = None,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send PUT (full replace/update) with a JSON body."""
        return self.session.put(
            self._url(path),
            json=json,
            params=params,
            timeout=self.timeout,
            **kwargs,
        )

    def patch(
        self,
        path: str,
        *,
        json: dict[str, Any] | list[Any] | None = None,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send PATCH (partial update) with a JSON body."""
        return self.session.patch(
            self._url(path),
            json=json,
            params=params,
            timeout=self.timeout,
            **kwargs,
        )

    def delete(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send DELETE (remove resource)."""
        return self.session.delete(
            self._url(path),
            params=params,
            timeout=self.timeout,
            **kwargs,
        )

    def close(self) -> None:
        self.session.close()
