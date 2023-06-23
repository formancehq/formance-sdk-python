"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import statsresponse as shared_statsresponse
from typing import Optional



@dataclasses.dataclass
class ReadStatsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""name of the ledger"""
    




@dataclasses.dataclass
class ReadStatsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    stats_response: Optional[shared_statsresponse.StatsResponse] = dataclasses.field(default=None)
    r"""OK"""
    
