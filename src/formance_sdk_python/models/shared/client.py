"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .clientsecret import ClientSecret, ClientSecretTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ClientTypedDict(TypedDict):
    id: str
    name: str
    description: NotRequired[str]
    metadata: NotRequired[Dict[str, Any]]
    post_logout_redirect_uris: NotRequired[List[str]]
    public: NotRequired[bool]
    redirect_uris: NotRequired[List[str]]
    scopes: NotRequired[List[str]]
    secrets: NotRequired[List[ClientSecretTypedDict]]
    trusted: NotRequired[bool]


class Client(BaseModel):
    id: str

    name: str

    description: Optional[str] = None

    metadata: Optional[Dict[str, Any]] = None

    post_logout_redirect_uris: Annotated[
        Optional[List[str]], pydantic.Field(alias="postLogoutRedirectUris")
    ] = None

    public: Optional[bool] = None

    redirect_uris: Annotated[
        Optional[List[str]], pydantic.Field(alias="redirectUris")
    ] = None

    scopes: Optional[List[str]] = None

    secrets: Optional[List[ClientSecret]] = None

    trusted: Optional[bool] = None