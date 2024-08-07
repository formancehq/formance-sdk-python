"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connector as shared_connector


@dataclasses.dataclass
class ResetConnectorV1Request:
    connector: shared_connector.Connector = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    r"""The name of the connector."""
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    r"""The connector ID."""
    



@dataclasses.dataclass
class ResetConnectorV1Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

