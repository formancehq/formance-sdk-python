"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class ScriptTypedDict(TypedDict):
    plain: str
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    reference: NotRequired[str]
    r"""Reference to attach to the generated transaction"""
    vars: NotRequired[Dict[str, Any]]


class Script(BaseModel):
    plain: str

    metadata: OptionalNullable[Dict[str, Any]] = UNSET

    reference: Optional[str] = None
    r"""Reference to attach to the generated transaction"""

    vars: Optional[Dict[str, Any]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "reference", "vars"]
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