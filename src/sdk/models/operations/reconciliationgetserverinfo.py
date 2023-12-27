"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import reconciliationerrorresponse as shared_reconciliationerrorresponse
from ..shared import serverinfo as shared_serverinfo
from typing import Optional


@dataclasses.dataclass
class ReconciliationgetServerInfoResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    reconciliation_error_response: Optional[shared_reconciliationerrorresponse.ReconciliationErrorResponse] = dataclasses.field(default=None)
    r"""Error response"""
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    r"""Server information"""
    
