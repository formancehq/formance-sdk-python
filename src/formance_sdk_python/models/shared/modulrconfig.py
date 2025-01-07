"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ModulrConfigTypedDict(TypedDict):
    api_key: str
    api_secret: str
    name: str
    endpoint: NotRequired[str]
    polling_period: NotRequired[str]
    r"""The frequency at which the connector will try to fetch new BalanceTransaction objects from Modulr API.

    """


class ModulrConfig(BaseModel):
    api_key: Annotated[str, pydantic.Field(alias="apiKey")]

    api_secret: Annotated[str, pydantic.Field(alias="apiSecret")]

    name: str

    endpoint: Optional[str] = None

    polling_period: Annotated[Optional[str], pydantic.Field(alias="pollingPeriod")] = (
        "120s"
    )
    r"""The frequency at which the connector will try to fetch new BalanceTransaction objects from Modulr API.

    """
