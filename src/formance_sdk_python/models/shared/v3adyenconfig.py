"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3AdyenConfigTypedDict(TypedDict):
    api_key: str
    company_id: str
    name: str
    live_endpoint_prefix: NotRequired[str]
    page_size: NotRequired[int]
    polling_period: NotRequired[str]
    webhook_password: NotRequired[str]
    webhook_username: NotRequired[str]


class V3AdyenConfig(BaseModel):
    api_key: Annotated[str, pydantic.Field(alias="apiKey")]

    company_id: Annotated[str, pydantic.Field(alias="companyID")]

    name: str

    live_endpoint_prefix: Annotated[
        Optional[str], pydantic.Field(alias="liveEndpointPrefix")
    ] = None

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = 25

    polling_period: Annotated[Optional[str], pydantic.Field(alias="pollingPeriod")] = (
        "2m"
    )

    webhook_password: Annotated[
        Optional[str], pydantic.Field(alias="webhookPassword")
    ] = None

    webhook_username: Annotated[
        Optional[str], pydantic.Field(alias="webhookUsername")
    ] = None
