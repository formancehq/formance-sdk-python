"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    bankaccountresponse as shared_bankaccountresponse,
)
from formance_sdk_python.types import BaseModel
import httpx
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateBankAccountResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    bank_account_response: NotRequired[
        shared_bankaccountresponse.BankAccountResponseTypedDict
    ]
    r"""OK"""


class CreateBankAccountResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    bank_account_response: Optional[shared_bankaccountresponse.BankAccountResponse] = (
        None
    )
    r"""OK"""