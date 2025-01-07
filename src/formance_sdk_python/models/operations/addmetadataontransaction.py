"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
    validate_int,
)
import httpx
from pydantic import model_serializer
from pydantic.functional_validators import BeforeValidator
from typing import Any, Dict
from typing_extensions import Annotated, NotRequired, TypedDict


class AddMetadataOnTransactionRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    txid: int
    r"""Transaction ID."""
    request_body: NotRequired[Nullable[Dict[str, Any]]]
    r"""metadata"""


class AddMetadataOnTransactionRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    txid: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Transaction ID."""

    request_body: Annotated[
        OptionalNullable[Dict[str, Any]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = UNSET
    r"""metadata"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["RequestBody"]
        nullable_fields = ["RequestBody"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class AddMetadataOnTransactionResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class AddMetadataOnTransactionResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""