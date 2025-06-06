"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DummyPayConfigTypedDict(TypedDict):
    directory: str
    name: str
    file_polling_period: NotRequired[str]
    r"""The frequency at which the connector will try to fetch new payment objects from the directory"""
    number_of_accounts_pre_generated: NotRequired[int]
    number_of_payments_pre_generated: NotRequired[int]
    prefix_file_to_ingest: NotRequired[str]
    provider: NotRequired[str]


class DummyPayConfig(BaseModel):
    directory: str

    name: str

    file_polling_period: Annotated[
        Optional[str], pydantic.Field(alias="filePollingPeriod")
    ] = "10s"
    r"""The frequency at which the connector will try to fetch new payment objects from the directory"""

    number_of_accounts_pre_generated: Annotated[
        Optional[int], pydantic.Field(alias="numberOfAccountsPreGenerated")
    ] = None

    number_of_payments_pre_generated: Annotated[
        Optional[int], pydantic.Field(alias="numberOfPaymentsPreGenerated")
    ] = None

    prefix_file_to_ingest: Annotated[
        Optional[str], pydantic.Field(alias="prefixFileToIngest")
    ] = None

    provider: Optional[str] = "Dummypay"
