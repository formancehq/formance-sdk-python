"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class V3ConnectorSchemasConfigTypedDict(TypedDict):
    pass


class V3ConnectorSchemasConfig(BaseModel):
    pass


class V3ConnectorTypedDict(TypedDict):
    config: V3ConnectorSchemasConfigTypedDict
    created_at: datetime
    id: str
    name: str
    provider: str
    reference: str
    scheduled_for_deletion: bool


class V3Connector(BaseModel):
    config: V3ConnectorSchemasConfig

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    id: str

    name: str

    provider: str

    reference: str

    scheduled_for_deletion: Annotated[
        bool, pydantic.Field(alias="scheduledForDeletion")
    ]
