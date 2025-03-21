"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class StripeConfigTypedDict(TypedDict):
    api_key: str
    name: str
    page_size: NotRequired[int]
    r"""Number of BalanceTransaction to fetch at each polling interval.

    """
    polling_period: NotRequired[str]
    r"""The frequency at which the connector will try to fetch new BalanceTransaction objects from Stripe API.

    """
    provider: NotRequired[str]


class StripeConfig(BaseModel):
    api_key: Annotated[str, pydantic.Field(alias="apiKey")]

    name: str

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = 10
    r"""Number of BalanceTransaction to fetch at each polling interval.

    """

    polling_period: Annotated[Optional[str], pydantic.Field(alias="pollingPeriod")] = (
        "120s"
    )
    r"""The frequency at which the connector will try to fetch new BalanceTransaction objects from Stripe API.

    """

    provider: Optional[str] = "Stripe"
