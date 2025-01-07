"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    getwalletsummaryresponse as shared_getwalletsummaryresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetWalletSummaryRequestTypedDict(TypedDict):
    id: str


class GetWalletSummaryRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetWalletSummaryResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_wallet_summary_response: NotRequired[
        shared_getwalletsummaryresponse.GetWalletSummaryResponseTypedDict
    ]
    r"""Wallet summary"""


class GetWalletSummaryResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    get_wallet_summary_response: Optional[
        shared_getwalletsummaryresponse.GetWalletSummaryResponse
    ] = None
    r"""Wallet summary"""