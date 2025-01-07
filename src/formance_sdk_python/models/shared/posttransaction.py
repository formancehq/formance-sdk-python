"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .posting import Posting, PostingTypedDict
from datetime import datetime
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class PostTransactionScriptTypedDict(TypedDict):
    plain: str
    vars: NotRequired[Dict[str, Any]]


class PostTransactionScript(BaseModel):
    plain: str

    vars: Optional[Dict[str, Any]] = None


class PostTransactionTypedDict(TypedDict):
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    postings: NotRequired[List[PostingTypedDict]]
    reference: NotRequired[str]
    script: NotRequired[PostTransactionScriptTypedDict]
    timestamp: NotRequired[datetime]


class PostTransaction(BaseModel):
    metadata: OptionalNullable[Dict[str, Any]] = UNSET

    postings: Optional[List[Posting]] = None

    reference: Optional[str] = None

    script: Optional[PostTransactionScript] = None

    timestamp: Optional[datetime] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "postings", "reference", "script", "timestamp"]
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
