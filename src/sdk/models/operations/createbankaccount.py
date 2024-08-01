"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bankaccountresponse as shared_bankaccountresponse
from typing import Optional


@dataclasses.dataclass
class CreateBankAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    bank_account_response: Optional[shared_bankaccountresponse.BankAccountResponse] = dataclasses.field(default=None)
    r"""OK"""
    

