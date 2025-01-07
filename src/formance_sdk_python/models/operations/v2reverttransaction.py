"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    v2reverttransactionresponse as shared_v2reverttransactionresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    validate_int,
)
import httpx
import pydantic
from pydantic.functional_validators import BeforeValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2RevertTransactionRequestTypedDict(TypedDict):
    id: int
    r"""Transaction ID."""
    ledger: str
    r"""Name of the ledger."""
    at_effective_date: NotRequired[bool]
    r"""Revert transaction at effective date of the original tx"""
    force: NotRequired[bool]
    r"""Force revert"""


class V2RevertTransactionRequest(BaseModel):
    id: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Transaction ID."""

    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    at_effective_date: Annotated[
        Optional[bool],
        pydantic.Field(alias="atEffectiveDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Revert transaction at effective date of the original tx"""

    force: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Force revert"""


class V2RevertTransactionResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_revert_transaction_response: NotRequired[
        shared_v2reverttransactionresponse.V2RevertTransactionResponseTypedDict
    ]
    r"""OK"""


class V2RevertTransactionResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v2_revert_transaction_response: Optional[
        shared_v2reverttransactionresponse.V2RevertTransactionResponse
    ] = None
    r"""OK"""