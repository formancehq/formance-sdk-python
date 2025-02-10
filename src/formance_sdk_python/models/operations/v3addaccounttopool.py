"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import pydantic
from typing_extensions import Annotated, TypedDict


class V3AddAccountToPoolRequestTypedDict(TypedDict):
    account_id: str
    r"""The account ID"""
    pool_id: str
    r"""The pool ID"""


class V3AddAccountToPoolRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The account ID"""

    pool_id: Annotated[
        str,
        pydantic.Field(alias="poolID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The pool ID"""


class V3AddAccountToPoolResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class V3AddAccountToPoolResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
