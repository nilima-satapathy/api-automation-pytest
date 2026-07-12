"""Load request body JSON files from data/payloads/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PAYLOADS_DIR = Path(__file__).resolve().parents[1] / "data" / "payloads"


def load_payload(name: str) -> dict[str, Any]:
    """
    Load a payload file by name.

    Example: load_payload("create_post.json")
    """
    path = PAYLOADS_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Payload not found: {path}")
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise TypeError(f"Payload must be a JSON object: {name}")
    return data
