"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bankaccountresponse as shared_bankaccountresponse
from ...models.shared import forwardbankaccountrequest as shared_forwardbankaccountrequest
from typing import Optional


@dataclasses.dataclass
class ForwardBankAccountRequest:
    bank_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'bankAccountId', 'style': 'simple', 'explode': False }})
    r"""The bank account ID."""
    forward_bank_account_request: shared_forwardbankaccountrequest.ForwardBankAccountRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class ForwardBankAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bank_account_response: Optional[shared_bankaccountresponse.BankAccountResponse] = dataclasses.field(default=None)
    r"""OK"""
    

