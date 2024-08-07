"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import paymentsaccountresponse as shared_paymentsaccountresponse
from typing import Optional


@dataclasses.dataclass
class PaymentsgetAccountRequest:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    r"""The account ID."""
    



@dataclasses.dataclass
class PaymentsgetAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    payments_account_response: Optional[shared_paymentsaccountresponse.PaymentsAccountResponse] = dataclasses.field(default=None)
    r"""OK"""
    

