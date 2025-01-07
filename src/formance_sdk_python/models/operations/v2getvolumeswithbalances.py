"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.models.shared import (
    v2volumeswithbalancecursorresponse as shared_v2volumeswithbalancecursorresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import httpx
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2GetVolumesWithBalancesRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    request_body: NotRequired[Dict[str, Any]]
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    end_time: NotRequired[datetime]
    group_by: NotRequired[int]
    r"""Group volumes and balance by the level of the segment of the address"""
    insertion_date: NotRequired[bool]
    r"""Use insertion date instead of effective date"""
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """
    start_time: NotRequired[datetime]


class V2GetVolumesWithBalancesRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    request_body: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Maximum page size is set to 15.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    end_time: Annotated[
        Optional[datetime],
        pydantic.Field(alias="endTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    group_by: Annotated[
        Optional[int],
        pydantic.Field(alias="groupBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Group volumes and balance by the level of the segment of the address"""

    insertion_date: Annotated[
        Optional[bool],
        pydantic.Field(alias="insertionDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Use insertion date instead of effective date"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of results to return per page.

    """

    start_time: Annotated[
        Optional[datetime],
        pydantic.Field(alias="startTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class V2GetVolumesWithBalancesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_volumes_with_balance_cursor_response: NotRequired[
        shared_v2volumeswithbalancecursorresponse.V2VolumesWithBalanceCursorResponseTypedDict
    ]
    r"""OK"""


class V2GetVolumesWithBalancesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v2_volumes_with_balance_cursor_response: Optional[
        shared_v2volumeswithbalancecursorresponse.V2VolumesWithBalanceCursorResponse
    ] = None
    r"""OK"""