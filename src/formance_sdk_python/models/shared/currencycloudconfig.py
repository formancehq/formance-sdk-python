"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CurrencyCloudConfigTypedDict(TypedDict):
    api_key: str
    login_id: str
    r"""Username of the API Key holder"""
    name: str
    endpoint: NotRequired[str]
    r"""The endpoint to use for the API. Defaults to https://devapi.currencycloud.com"""
    polling_period: NotRequired[str]
    r"""The frequency at which the connector will fetch transactions"""
    provider: NotRequired[str]


class CurrencyCloudConfig(BaseModel):
    api_key: Annotated[str, pydantic.Field(alias="apiKey")]

    login_id: Annotated[str, pydantic.Field(alias="loginID")]
    r"""Username of the API Key holder"""

    name: str

    endpoint: Optional[str] = None
    r"""The endpoint to use for the API. Defaults to https://devapi.currencycloud.com"""

    polling_period: Annotated[Optional[str], pydantic.Field(alias="pollingPeriod")] = (
        "120s"
    )
    r"""The frequency at which the connector will fetch transactions"""

    provider: Optional[str] = "Currencycloud"
