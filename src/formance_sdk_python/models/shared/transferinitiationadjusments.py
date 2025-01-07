"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transferinitiationstatus import TransferInitiationStatus
from datetime import datetime
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Dict
from typing_extensions import Annotated, NotRequired, TypedDict


class TransferInitiationAdjusmentsTypedDict(TypedDict):
    adjustment_id: str
    created_at: datetime
    error: str
    status: TransferInitiationStatus
    metadata: NotRequired[Nullable[Dict[str, str]]]


class TransferInitiationAdjusments(BaseModel):
    adjustment_id: Annotated[str, pydantic.Field(alias="adjustmentID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    error: str

    status: TransferInitiationStatus

    metadata: OptionalNullable[Dict[str, str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata"]
        nullable_fields = ["metadata"]
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
