"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    transactions as shared_transactions,
    transactionsresponse as shared_transactionsresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTransactionsRequestTypedDict(TypedDict):
    transactions: shared_transactions.TransactionsTypedDict
    ledger: str
    r"""Name of the ledger."""


class CreateTransactionsRequest(BaseModel):
    transactions: Annotated[
        shared_transactions.Transactions,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""


class CreateTransactionsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    transactions_response: NotRequired[
        shared_transactionsresponse.TransactionsResponseTypedDict
    ]
    r"""OK"""


class CreateTransactionsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    transactions_response: Optional[
        shared_transactionsresponse.TransactionsResponse
    ] = None
    r"""OK"""
