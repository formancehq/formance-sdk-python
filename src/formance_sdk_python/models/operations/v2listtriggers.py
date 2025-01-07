"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    v2listtriggersresponse as shared_v2listtriggersresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, QueryParamMetadata
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2ListTriggersRequestTypedDict(TypedDict):
    cursor: NotRequired[str]
    r"""Parameter used in pagination requests.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """
    name: NotRequired[str]
    r"""search by name"""
    page_size: NotRequired[int]
    r"""The maximum number of results to return per page.

    """


class V2ListTriggersRequest(BaseModel):
    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter used in pagination requests.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.

    """

    name: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""search by name"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of results to return per page.

    """


class V2ListTriggersResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_list_triggers_response: NotRequired[
        shared_v2listtriggersresponse.V2ListTriggersResponseTypedDict
    ]
    r"""List of triggers"""


class V2ListTriggersResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v2_list_triggers_response: Optional[
        shared_v2listtriggersresponse.V2ListTriggersResponse
    ] = None
    r"""List of triggers"""
