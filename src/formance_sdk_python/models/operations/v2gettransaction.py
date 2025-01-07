"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.models.shared import (
    v2gettransactionresponse as shared_v2gettransactionresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    validate_int,
)
import httpx
from pydantic.functional_validators import BeforeValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2GetTransactionRequestTypedDict(TypedDict):
    id: int
    r"""Transaction ID."""
    ledger: str
    r"""Name of the ledger."""
    expand: NotRequired[str]
    pit: NotRequired[datetime]


class V2GetTransactionRequest(BaseModel):
    id: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Transaction ID."""

    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    expand: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    pit: Annotated[
        Optional[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class V2GetTransactionResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_get_transaction_response: NotRequired[
        shared_v2gettransactionresponse.V2GetTransactionResponseTypedDict
    ]
    r"""OK"""


class V2GetTransactionResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v2_get_transaction_response: Optional[
        shared_v2gettransactionresponse.V2GetTransactionResponse
    ] = None
    r"""OK"""
