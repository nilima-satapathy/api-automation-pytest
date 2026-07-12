"""
Pytest configuration and shared fixtures.

Milestone 1: project root on sys.path so `utils` imports work.
Milestone 2: shared base_url, headers, and api_client fixtures.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Generator
from pathlib import Path

import pytest

# Project root (parent of tests/)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def base_url() -> str:
    """API root URL. Override with env var API_BASE_URL if needed."""
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def default_headers() -> dict[str, str]:
    """Headers shared by all API calls in this suite."""
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


@pytest.fixture
def api_client(base_url: str, default_headers: dict[str, str]) -> Generator[ApiClient, None, None]:
    """
    Fresh ApiClient per test.

    Setup: create client with shared base URL + headers.
    Teardown: close the session after the test finishes.
    """
    client = ApiClient(base_url=base_url, headers=default_headers)
    yield client
    client.close()
