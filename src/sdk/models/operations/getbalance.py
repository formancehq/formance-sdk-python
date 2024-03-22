"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import walletserrorresponse as errors_walletserrorresponse
from ...models.shared import getbalanceresponse as shared_getbalanceresponse
from typing import Optional


@dataclasses.dataclass
class GetBalanceRequest:
    balance_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'balanceName', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetBalanceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_balance_response: Optional[shared_getbalanceresponse.GetBalanceResponse] = dataclasses.field(default=None)
    r"""Balance summary"""
    wallets_error_response: Optional[errors_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

