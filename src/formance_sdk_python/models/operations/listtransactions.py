"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.models.shared import (
    transactionscursorresponse as shared_transactionscursorresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import httpx
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListTransactionsRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    account: NotRequired[str]
    r"""Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $)."""
    after: NotRequired[str]
    r"""Pagination cursor, will return transactions after given txid (in descending order)."""
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    destination: NotRequired[str]
    r"""Filter transactions with postings involving given account at destination (regular expression placed between ^ and $)."""
    end_time: NotRequired[datetime]
    r"""Filter transactions that occurred before this timestamp.
    The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute).

    """
    metadata: NotRequired[Dict[str, Any]]
    r"""Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below."""
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """
    reference: NotRequired[str]
    r"""Find transactions by reference field."""
    source: NotRequired[str]
    r"""Filter transactions with postings involving given account at source (regular expression placed between ^ and $)."""
    start_time: NotRequired[datetime]
    r"""Filter transactions that occurred after this timestamp.
    The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute).

    """


class ListTransactionsRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    account: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $)."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination cursor, will return transactions after given txid (in descending order)."""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    destination: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions with postings involving given account at destination (regular expression placed between ^ and $)."""

    end_time: Annotated[
        Optional[datetime],
        pydantic.Field(alias="endTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions that occurred before this timestamp.
    The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute).

    """

    metadata: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below."""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 15
    r"""The maximum number of results to return per page.

    """

    reference: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Find transactions by reference field."""

    source: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions with postings involving given account at source (regular expression placed between ^ and $)."""

    start_time: Annotated[
        Optional[datetime],
        pydantic.Field(alias="startTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions that occurred after this timestamp.
    The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute).

    """


class ListTransactionsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    transactions_cursor_response: NotRequired[
        shared_transactionscursorresponse.TransactionsCursorResponseTypedDict
    ]
    r"""OK"""


class ListTransactionsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    transactions_cursor_response: Optional[
        shared_transactionscursorresponse.TransactionsCursorResponse
    ] = None
    r"""OK"""
