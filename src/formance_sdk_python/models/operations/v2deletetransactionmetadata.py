"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    validate_int,
)
import httpx
import pydantic
from pydantic.functional_validators import BeforeValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2DeleteTransactionMetadataRequestTypedDict(TypedDict):
    id: int
    r"""Transaction ID."""
    key: str
    r"""The key to remove."""
    ledger: str
    r"""Name of the ledger."""
    idempotency_key: NotRequired[str]
    r"""Use an idempotency key"""


class V2DeleteTransactionMetadataRequest(BaseModel):
    id: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Transaction ID."""

    key: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The key to remove."""

    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Use an idempotency key"""


class V2DeleteTransactionMetadataResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class V2DeleteTransactionMetadataResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
