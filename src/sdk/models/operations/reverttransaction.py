"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import errorresponse as errors_errorresponse
from ...models.shared import transactionresponse as shared_transactionresponse
from typing import Optional


@dataclasses.dataclass
class RevertTransactionRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    txid: int = dataclasses.field(metadata={'path_param': { 'field_name': 'txid', 'style': 'simple', 'explode': False }})
    r"""Transaction ID."""
    disable_checks: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'disableChecks', 'style': 'form', 'explode': True }})
    r"""Allow to disable balances checks"""
    



@dataclasses.dataclass
class RevertTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error_response: Optional[errors_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    transaction_response: Optional[shared_transactionresponse.TransactionResponse] = dataclasses.field(default=None)
    r"""OK"""
    

