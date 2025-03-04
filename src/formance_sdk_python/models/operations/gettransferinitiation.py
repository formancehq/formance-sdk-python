"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    transferinitiationresponse as shared_transferinitiationresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetTransferInitiationRequestTypedDict(TypedDict):
    transfer_id: str
    r"""The transfer ID."""


class GetTransferInitiationRequest(BaseModel):
    transfer_id: Annotated[
        str,
        pydantic.Field(alias="transferId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The transfer ID."""


class GetTransferInitiationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    transfer_initiation_response: NotRequired[
        shared_transferinitiationresponse.TransferInitiationResponseTypedDict
    ]
    r"""OK"""


class GetTransferInitiationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    transfer_initiation_response: Optional[
        shared_transferinitiationresponse.TransferInitiationResponse
    ] = None
    r"""OK"""
