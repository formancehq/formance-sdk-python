"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    accountscursorresponse as shared_accountscursorresponse,
    errorresponse as shared_errorresponse,
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


class ListAccountsRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    address: NotRequired[str]
    r"""Filter accounts by address pattern (regular expression placed between ^ and $)."""
    after: NotRequired[str]
    r"""Pagination cursor, will return accounts after given address, in descending order."""
    balance: NotRequired[int]
    r"""Filter accounts by their balance (default operator is gte)"""
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    metadata: NotRequired[Dict[str, Any]]
    r"""Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below."""
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """
    pagination_token: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    Deprecated, please use `cursor` instead.

    """


class ListAccountsRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    address: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter accounts by address pattern (regular expression placed between ^ and $)."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination cursor, will return accounts after given address, in descending order."""

    balance: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter accounts by their balance (default operator is gte)"""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    metadata: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below."""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of results to return per page.

    """

    pagination_token: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    Deprecated, please use `cursor` instead.

    """


class ListAccountsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    accounts_cursor_response: NotRequired[
        shared_accountscursorresponse.AccountsCursorResponseTypedDict
    ]
    r"""OK"""
    error_response: NotRequired[shared_errorresponse.ErrorResponseTypedDict]
    r"""Not found"""


class ListAccountsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    accounts_cursor_response: Optional[
        shared_accountscursorresponse.AccountsCursorResponse
    ] = None
    r"""OK"""

    error_response: Optional[shared_errorresponse.ErrorResponse] = None
    r"""Not found"""
