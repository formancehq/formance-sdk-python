"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import reversetransferinitiationrequest as shared_reversetransferinitiationrequest


@dataclasses.dataclass
class ReverseTransferInitiationRequest:
    reverse_transfer_initiation_request: shared_reversetransferinitiationrequest.ReverseTransferInitiationRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    transfer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transferId', 'style': 'simple', 'explode': False }})
    r"""The transfer ID."""
    



@dataclasses.dataclass
class ReverseTransferInitiationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    

