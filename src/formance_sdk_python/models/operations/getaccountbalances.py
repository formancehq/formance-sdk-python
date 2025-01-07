"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.models.shared import balancescursor as shared_balancescursor
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import httpx
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAccountBalancesRequestTypedDict(TypedDict):
    account_id: str
    r"""The account ID."""
    asset: NotRequired[str]
    r"""Filter balances by currency.
    If not specified, all account's balances will be returned.

    """
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    from_: NotRequired[datetime]
    r"""Filter balances by date.
    If not specified, all account's balances will be returned.

    """
    limit: NotRequired[int]
    r"""The maximum number of results to return per page."""
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """
    sort: NotRequired[List[str]]
    r"""Fields used to sort payments (default is date:desc)."""
    to: NotRequired[datetime]
    r"""Filter balances by date.
    If not specified, default will be set to now.

    """


class GetAccountBalancesRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The account ID."""

    asset: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter balances by currency.
    If not specified, all account's balances will be returned.

    """

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    from_: Annotated[
        Optional[datetime],
        pydantic.Field(alias="from"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter balances by date.
    If not specified, all account's balances will be returned.

    """

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of results to return per page."""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 15
    r"""The maximum number of results to return per page.

    """

    sort: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Fields used to sort payments (default is date:desc)."""

    to: Annotated[
        Optional[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter balances by date.
    If not specified, default will be set to now.

    """


class GetAccountBalancesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    balances_cursor: NotRequired[shared_balancescursor.BalancesCursorTypedDict]
    r"""OK"""


class GetAccountBalancesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    balances_cursor: Optional[shared_balancescursor.BalancesCursor] = None
    r"""OK"""