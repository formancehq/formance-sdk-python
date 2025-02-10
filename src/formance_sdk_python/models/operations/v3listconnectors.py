"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    v3connectorscursorresponse as shared_v3connectorscursorresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
import httpx
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3ListConnectorsRequestTypedDict(TypedDict):
    request_body: NotRequired[Dict[str, Any]]
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.

    """
    page_size: NotRequired[int]
    r"""The number of items to return"""


class V3ListConnectorsRequest(BaseModel):
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


class V3ListConnectorsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v3_connectors_cursor_response: NotRequired[
        shared_v3connectorscursorresponse.V3ConnectorsCursorResponseTypedDict
    ]
    r"""OK"""


class V3ListConnectorsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v3_connectors_cursor_response: Optional[
        shared_v3connectorscursorresponse.V3ConnectorsCursorResponse
    ] = None
    r"""OK"""
