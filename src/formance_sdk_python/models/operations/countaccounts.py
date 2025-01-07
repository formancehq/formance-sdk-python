"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import httpx
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CountAccountsRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    address: NotRequired[str]
    r"""Filter accounts by address pattern (regular expression placed between ^ and $)."""
    metadata: NotRequired[Dict[str, Any]]
    r"""Filter accounts by metadata key value pairs. The filter can be used like this metadata[key]=value1&metadata[a.nested.key]=value2"""


class CountAccountsRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    address: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter accounts by address pattern (regular expression placed between ^ and $)."""

    metadata: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Filter accounts by metadata key value pairs. The filter can be used like this metadata[key]=value1&metadata[a.nested.key]=value2"""


class CountAccountsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]]
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class CountAccountsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    headers: Dict[str, List[str]]

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
