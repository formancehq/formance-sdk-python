"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import v2ledgerlistresponse as shared_v2ledgerlistresponse
from typing import Optional


@dataclasses.dataclass
class V2ListLedgersRequest:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    """
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page."""
    



@dataclasses.dataclass
class V2ListLedgersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_ledger_list_response: Optional[shared_v2ledgerlistresponse.V2LedgerListResponse] = dataclasses.field(default=None)
    r"""OK"""
    

