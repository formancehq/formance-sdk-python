"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import walletserrorresponse as errors_walletserrorresponse
from ...models.shared import getholdresponse as shared_getholdresponse
from typing import Optional


@dataclasses.dataclass
class GetHoldRequest:
    hold_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'holdID', 'style': 'simple', 'explode': False }})
    r"""The hold ID"""
    



@dataclasses.dataclass
class GetHoldResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_hold_response: Optional[shared_getholdresponse.GetHoldResponse] = dataclasses.field(default=None)
    r"""Holds"""
    wallets_error_response: Optional[errors_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

