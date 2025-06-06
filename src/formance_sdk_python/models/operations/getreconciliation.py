"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    reconciliationresponse as shared_reconciliationresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetReconciliationRequestTypedDict(TypedDict):
    reconciliation_id: str
    r"""The reconciliation ID."""


class GetReconciliationRequest(BaseModel):
    reconciliation_id: Annotated[
        str,
        pydantic.Field(alias="reconciliationID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The reconciliation ID."""


class GetReconciliationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    reconciliation_response: NotRequired[
        shared_reconciliationresponse.ReconciliationResponseTypedDict
    ]
    r"""OK"""


class GetReconciliationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    reconciliation_response: Optional[
        shared_reconciliationresponse.ReconciliationResponse
    ] = None
    r"""OK"""
