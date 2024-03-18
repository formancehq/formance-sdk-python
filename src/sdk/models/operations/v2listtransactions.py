"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import v2errorresponse as errors_v2errorresponse
from ...models.shared import v2transactionscursorresponse as shared_v2transactionscursorresponse
from datetime import datetime
from typing import Any, Dict, Optional


@dataclasses.dataclass
class V2ListTransactionsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    request_body: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    """
    expand: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expand', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page."""
    pit: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pit', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class V2ListTransactionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_error_response: Optional[errors_v2errorresponse.V2ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    v2_transactions_cursor_response: Optional[shared_v2transactionscursorresponse.V2TransactionsCursorResponse] = dataclasses.field(default=None)
    r"""OK"""
    

