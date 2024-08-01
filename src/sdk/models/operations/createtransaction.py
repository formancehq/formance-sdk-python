"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import posttransaction as shared_posttransaction
from ...models.shared import transactionsresponse as shared_transactionsresponse
from typing import Optional


@dataclasses.dataclass
class CreateTransactionRequest:
    post_transaction: shared_posttransaction.PostTransaction = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""The request body must contain at least one of the following objects:
      - `postings`: suitable for simple transactions
      - `script`: enabling more complex transactions with Numscript
    """
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    preview: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'preview', 'style': 'form', 'explode': True }})
    r"""Set the preview mode. Preview mode doesn't add the logs to the database or publish a message to the message broker."""
    



@dataclasses.dataclass
class CreateTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    transactions_response: Optional[shared_transactionsresponse.TransactionsResponse] = dataclasses.field(default=None)
    r"""OK"""
    

