"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import reconciliationerrorresponse as shared_reconciliationerrorresponse
from ..shared import reconciliationscursorresponse as shared_reconciliationscursorresponse
from typing import Optional


@dataclasses.dataclass
class ListReconciliationsRequest:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    """
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page."""
    



@dataclasses.dataclass
class ListReconciliationsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    reconciliation_error_response: Optional[shared_reconciliationerrorresponse.ReconciliationErrorResponse] = dataclasses.field(default=None)
    r"""Error response"""
    reconciliations_cursor_response: Optional[shared_reconciliationscursorresponse.ReconciliationsCursorResponse] = dataclasses.field(default=None)
    r"""OK"""
    

