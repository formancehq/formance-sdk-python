"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getwalletsummaryresponse as shared_getwalletsummaryresponse
from typing import Optional


@dataclasses.dataclass
class GetWalletSummaryRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetWalletSummaryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_wallet_summary_response: Optional[shared_getwalletsummaryresponse.GetWalletSummaryResponse] = dataclasses.field(default=None)
    r"""Wallet summary"""
    

