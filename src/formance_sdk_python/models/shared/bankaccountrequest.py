"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountRequestTypedDict(TypedDict):
    country: str
    name: str
    account_number: NotRequired[str]
    connector_id: NotRequired[str]
    iban: NotRequired[str]
    metadata: NotRequired[Nullable[Dict[str, str]]]
    swift_bic_code: NotRequired[str]


class BankAccountRequest(BaseModel):
    country: str

    name: str

    account_number: Annotated[Optional[str], pydantic.Field(alias="accountNumber")] = (
        None
    )

    connector_id: Annotated[Optional[str], pydantic.Field(alias="connectorID")] = None

    iban: Optional[str] = None

    metadata: OptionalNullable[Dict[str, str]] = UNSET

    swift_bic_code: Annotated[Optional[str], pydantic.Field(alias="swiftBicCode")] = (
        None
    )

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "accountNumber",
            "connectorID",
            "iban",
            "metadata",
            "swiftBicCode",
        ]
        nullable_fields = ["metadata"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
