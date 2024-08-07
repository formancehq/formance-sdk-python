"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import transactions as shared_transactions
from ...models.shared import transactionsresponse as shared_transactionsresponse
from typing import Optional


@dataclasses.dataclass
class CreateTransactionsRequest:
    transactions: shared_transactions.Transactions = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    



@dataclasses.dataclass
class CreateTransactionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    transactions_response: Optional[shared_transactionsresponse.TransactionsResponse] = dataclasses.field(default=None)
    r"""OK"""
    

