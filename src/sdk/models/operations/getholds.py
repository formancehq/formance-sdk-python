"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getholdsresponse as shared_getholdsresponse
from typing import Dict, Optional


@dataclasses.dataclass
class GetHoldsRequest:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when the pagination token is set.
    """
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    r"""Filter holds by metadata key value pairs. Nested objects can be used as seen in the example below."""
    page_size: Optional[int] = dataclasses.field(default=15, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page"""
    wallet_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'walletID', 'style': 'form', 'explode': True }})
    r"""The wallet to filter on"""
    



@dataclasses.dataclass
class GetHoldsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_holds_response: Optional[shared_getholdsresponse.GetHoldsResponse] = dataclasses.field(default=None)
    r"""Holds"""
    

