"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import errorresponse as errors_errorresponse
from ...models.shared import accountscursorresponse as shared_accountscursorresponse
from typing import Any, Dict, Optional


@dataclasses.dataclass
class ListAccountsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'address', 'style': 'form', 'explode': True }})
    r"""Filter accounts by address pattern (regular expression placed between ^ and $)."""
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""Pagination cursor, will return accounts after given address, in descending order."""
    balance: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'balance', 'style': 'form', 'explode': True }})
    r"""Filter accounts by their balance (default operator is gte)"""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    """
    metadata: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    r"""Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below."""
    page_size: Optional[int] = dataclasses.field(default=15, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page."""
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    Deprecated, please use `cursor` instead.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    



@dataclasses.dataclass
class ListAccountsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    accounts_cursor_response: Optional[shared_accountscursorresponse.AccountsCursorResponse] = dataclasses.field(default=None)
    r"""OK"""
    error_response: Optional[errors_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

