"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from formance_sdk_python.utils import validate_int
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import BeforeValidator
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BalanceWithAssetsTypedDict(TypedDict):
    assets: Dict[str, int]
    name: str
    expires_at: NotRequired[Nullable[datetime]]
    priority: NotRequired[int]


class BalanceWithAssets(BaseModel):
    assets: Dict[str, Annotated[int, BeforeValidator(validate_int)]]

    name: str

    expires_at: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="expiresAt")
    ] = UNSET

    priority: Annotated[Optional[int], BeforeValidator(validate_int)] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expiresAt", "priority"]
        nullable_fields = ["expiresAt"]
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
