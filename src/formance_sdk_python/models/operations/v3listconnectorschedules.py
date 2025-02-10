"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    v3connectorschedulescursorresponse as shared_v3connectorschedulescursorresponse,
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


class V3ListConnectorSchedulesRequestTypedDict(TypedDict):
    connector_id: str
    r"""The connector ID"""
    request_body: NotRequired[Dict[str, Any]]
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.

    """
    page_size: NotRequired[int]
    r"""The number of items to return"""


class V3ListConnectorSchedulesRequest(BaseModel):
    connector_id: Annotated[
        str,
        pydantic.Field(alias="connectorID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The connector ID"""

    request_body: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.

    """

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of items to return"""


class V3ListConnectorSchedulesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v3_connector_schedules_cursor_response: NotRequired[
        shared_v3connectorschedulescursorresponse.V3ConnectorSchedulesCursorResponseTypedDict
    ]
    r"""OK"""


class V3ListConnectorSchedulesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v3_connector_schedules_cursor_response: Optional[
        shared_v3connectorschedulescursorresponse.V3ConnectorSchedulesCursorResponse
    ] = None
    r"""OK"""
