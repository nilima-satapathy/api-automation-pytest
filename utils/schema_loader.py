"""Load JSON Schema files and validate API response bodies (Milestone 5)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator, ValidationError

SCHEMAS_DIR = Path(__file__).resolve().parents[1] / "data" / "schemas"


def load_schema(name: str) -> dict[str, Any]:
    """
    Load a schema file by name.

    Example: load_schema("user.json")
    """
    path = SCHEMAS_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Schema not found: {path}")
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise TypeError(f"Schema must be a JSON object: {name}")
    return data


def validate_schema(instance: Any, schema: dict[str, Any]) -> None:
    """
    Validate instance against schema.

    Raises jsonschema.ValidationError on failure (pytest will show details).
    """
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if not errors:
        return

    # First error is enough for a clear pytest failure message
    err: ValidationError = errors[0]
    path = ".".join(str(p) for p in err.absolute_path) or "(root)"
    raise ValidationError(
        f"Schema validation failed at '{path}': {err.message}"
    ) from err
