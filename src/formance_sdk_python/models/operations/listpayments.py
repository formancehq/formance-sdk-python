"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import paymentscursor as shared_paymentscursor
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, QueryParamMetadata
import httpx
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListPaymentsRequestTypedDict(TypedDict):
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """
    query: NotRequired[str]
    r"""Filters used to filter resources.

    """
    sort: NotRequired[List[str]]
    r"""Fields used to sort payments (default is date:desc)."""


class ListPaymentsRequest(BaseModel):
    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 15
    r"""The maximum number of results to return per page.

    """

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filters used to filter resources.

    """

    sort: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Fields used to sort payments (default is date:desc)."""


class ListPaymentsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    payments_cursor: NotRequired[shared_paymentscursor.PaymentsCursorTypedDict]
    r"""OK"""


class ListPaymentsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    payments_cursor: Optional[shared_paymentscursor.PaymentsCursor] = None
    r"""OK"""
