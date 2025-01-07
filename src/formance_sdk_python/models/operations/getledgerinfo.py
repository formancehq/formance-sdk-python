"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    ledgerinforesponse as shared_ledgerinforesponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetLedgerInfoRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""


class GetLedgerInfoRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""


class GetLedgerInfoResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    ledger_info_response: NotRequired[
        shared_ledgerinforesponse.LedgerInfoResponseTypedDict
    ]
    r"""OK"""


class GetLedgerInfoResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    ledger_info_response: Optional[shared_ledgerinforesponse.LedgerInfoResponse] = None
    r"""OK"""