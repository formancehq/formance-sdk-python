"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    balancescursorresponse as shared_balancescursorresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetBalancesRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    address: NotRequired[str]
    r"""Filter balances involving given account, either as source or destination."""
    after: NotRequired[str]
    r"""Pagination cursor, will return accounts after given address, in descending order."""
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """


class GetBalancesRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    address: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter balances involving given account, either as source or destination."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination cursor, will return accounts after given address, in descending order."""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 1000.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of results to return per page.

    """


class GetBalancesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    balances_cursor_response: NotRequired[
        shared_balancescursorresponse.BalancesCursorResponseTypedDict
    ]
    r"""OK"""


class GetBalancesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    balances_cursor_response: Optional[
        shared_balancescursorresponse.BalancesCursorResponse
    ] = None
    r"""OK"""
