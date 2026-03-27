""" This file is not auto-generated and can be freely modified. """

"""Payments account ID helper."""

import base64
import json
from typing import Any


def build_account_id(connector_id: str, reference: str) -> str:
    """
    Build an Formance Payments account ID from a connector ID and reference.

    Args:
        connector_id: The identifier of the connector.
        reference: The identifier of the account from the connector's provider.

    Returns:
        The Formance Payments account ID.

    Raises:
        ValueError: If connector_id is invalid or if reference is null/empty
    """
    if connector_id is None or (isinstance(connector_id, str) and not connector_id.strip()):
        raise ValueError("connector_id must be a non-empty string")
    if reference is None or (isinstance(reference, str) and not reference.strip()):
        raise ValueError("reference must be a non-empty string")

    try:
        padded = connector_id + "=" * (4 - len(connector_id) % 4) if len(connector_id) % 4 else connector_id
        decoded_bytes = base64.b64decode(padded, validate=True)
    except Exception as e:
        raise ValueError("connector_id is invalid") from e

    try:
        decoded_str = decoded_bytes.decode("utf-8")
        connector_id_decoded: Any = json.loads(decoded_str)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise ValueError("connector_id is invalid") from e

    payload = {"ConnectorID": connector_id_decoded, "Reference": reference}
    json_str = json.dumps(payload, separators=(",", ":"))
    encoded = base64.b64encode(json_str.encode("utf-8")).decode("ascii").rstrip("=")
    return encoded
