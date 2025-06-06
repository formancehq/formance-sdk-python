"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import io
from typing import IO, Union
from typing_extensions import Annotated, TypedDict


class V2ImportLogsRequestTypedDict(TypedDict):
    v2_import_logs_request: Union[bytes, IO[bytes], io.BufferedReader]
    ledger: str
    r"""Name of the ledger."""


class V2ImportLogsRequest(BaseModel):
    v2_import_logs_request: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader], FieldMetadata(request=True)
    ]

    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""


class V2ImportLogsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class V2ImportLogsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
