"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connector as shared_connector
from ...models.shared import transferrequest as shared_transferrequest
from ...models.shared import transferresponse as shared_transferresponse
from typing import Optional


@dataclasses.dataclass
class ConnectorsTransferRequest:
    transfer_request: shared_transferrequest.TransferRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    connector: shared_connector.Connector = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    r"""The name of the connector."""
    



@dataclasses.dataclass
class ConnectorsTransferResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    transfer_response: Optional[shared_transferresponse.TransferResponse] = dataclasses.field(default=None)
    r"""OK"""
    

