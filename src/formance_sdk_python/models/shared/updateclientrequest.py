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
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateClientRequestTypedDict(TypedDict):
    name: str
    description: NotRequired[str]
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    post_logout_redirect_uris: NotRequired[List[str]]
    public: NotRequired[bool]
    redirect_uris: NotRequired[List[str]]
    scopes: NotRequired[List[str]]
    trusted: NotRequired[bool]


class UpdateClientRequest(BaseModel):
    name: str

    description: Optional[str] = None

    metadata: OptionalNullable[Dict[str, Any]] = UNSET

    post_logout_redirect_uris: Annotated[
        Optional[List[str]], pydantic.Field(alias="postLogoutRedirectUris")
    ] = None

    public: Optional[bool] = None

    redirect_uris: Annotated[
        Optional[List[str]], pydantic.Field(alias="redirectUris")
    ] = None

    scopes: Optional[List[str]] = None

    trusted: Optional[bool] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "metadata",
            "postLogoutRedirectUris",
            "public",
            "redirectUris",
            "scopes",
            "trusted",
        ]
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
