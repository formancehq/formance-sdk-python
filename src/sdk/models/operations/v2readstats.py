"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import v2statsresponse as shared_v2statsresponse
from typing import Optional


@dataclasses.dataclass
class V2ReadStatsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""name of the ledger"""
    



@dataclasses.dataclass
class V2ReadStatsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_stats_response: Optional[shared_v2statsresponse.V2StatsResponse] = dataclasses.field(default=None)
    r"""OK"""
    

