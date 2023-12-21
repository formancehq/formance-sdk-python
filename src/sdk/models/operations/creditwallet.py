"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import creditwalletrequest as shared_creditwalletrequest
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class CreditWalletRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    credit_wallet_request: Optional[shared_creditwalletrequest.CreditWalletRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreditWalletResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

