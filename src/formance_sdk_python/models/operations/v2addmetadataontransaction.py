"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
    validate_int,
)
import httpx
import pydantic
from pydantic.functional_validators import BeforeValidator
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2AddMetadataOnTransactionRequestTypedDict(TypedDict):
    id: int
    r"""Transaction ID."""
    ledger: str
    r"""Name of the ledger."""
    idempotency_key: NotRequired[str]
    r"""Use an idempotency key"""
    request_body: NotRequired[Dict[str, str]]
    r"""metadata"""
    dry_run: NotRequired[bool]
    r"""Set the dryRun mode. Dry run mode doesn't add the logs to the database or publish a message to the message broker."""


class V2AddMetadataOnTransactionRequest(BaseModel):
    id: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Transaction ID."""

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

    request_body: Annotated[
        Optional[Dict[str, str]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""metadata"""

    dry_run: Annotated[
        Optional[bool],
        pydantic.Field(alias="dryRun"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Set the dryRun mode. Dry run mode doesn't add the logs to the database or publish a message to the message broker."""


class V2AddMetadataOnTransactionResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class V2AddMetadataOnTransactionResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""