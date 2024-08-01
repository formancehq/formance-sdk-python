"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Dict, Optional


@dataclasses.dataclass
class AddMetadataOnTransactionRequest:
    UNSET='__SPEAKEASY_UNSET__'
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    txid: int = dataclasses.field(metadata={'path_param': { 'field_name': 'txid', 'style': 'simple', 'explode': False }})
    r"""Transaction ID."""
    request_body: Optional[Dict[str, Any]] = dataclasses.field(default=UNSET, metadata={'request': { 'media_type': 'application/json' }})
    r"""metadata"""
    



@dataclasses.dataclass
class AddMetadataOnTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

