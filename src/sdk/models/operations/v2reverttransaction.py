"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import v2errorresponse as errors_v2errorresponse
from ...models.shared import v2reverttransactionresponse as shared_v2reverttransactionresponse
from typing import Optional


@dataclasses.dataclass
class V2RevertTransactionRequest:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Transaction ID."""
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    force: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'force', 'style': 'form', 'explode': True }})
    r"""Force revert"""
    



@dataclasses.dataclass
class V2RevertTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_error_response: Optional[errors_v2errorresponse.V2ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    v2_revert_transaction_response: Optional[shared_v2reverttransactionresponse.V2RevertTransactionResponse] = dataclasses.field(default=None)
    r"""OK"""
    

