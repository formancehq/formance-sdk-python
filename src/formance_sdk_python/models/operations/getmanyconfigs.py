"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import configsresponse as shared_configsresponse
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, QueryParamMetadata
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetManyConfigsRequestTypedDict(TypedDict):
    endpoint: NotRequired[str]
    r"""Optional filter by endpoint URL"""
    id: NotRequired[str]
    r"""Optional filter by Config ID"""


class GetManyConfigsRequest(BaseModel):
    endpoint: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional filter by endpoint URL"""

    id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional filter by Config ID"""


class GetManyConfigsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    configs_response: NotRequired[shared_configsresponse.ConfigsResponseTypedDict]
    r"""OK"""


class GetManyConfigsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    configs_response: Optional[shared_configsresponse.ConfigsResponse] = None
    r"""OK"""