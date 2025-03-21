"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3BankingcircleConfigTypedDict(TypedDict):
    authorization_endpoint: str
    endpoint: str
    name: str
    password: str
    user_certificate: str
    user_certificate_key: str
    username: str
    page_size: NotRequired[int]
    polling_period: NotRequired[str]
    provider: NotRequired[str]


class V3BankingcircleConfig(BaseModel):
    authorization_endpoint: Annotated[
        str, pydantic.Field(alias="authorizationEndpoint")
    ]

    endpoint: str

    name: str

    password: str

    user_certificate: Annotated[str, pydantic.Field(alias="userCertificate")]

    user_certificate_key: Annotated[str, pydantic.Field(alias="userCertificateKey")]

    username: str

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = 25

    polling_period: Annotated[Optional[str], pydantic.Field(alias="pollingPeriod")] = (
        "2m"
    )

    provider: Optional[str] = "Bankingcircle"
