"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3connectorconfig import V3ConnectorConfig, V3ConnectorConfigTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class V3GetConnectorConfigResponseTypedDict(TypedDict):
    data: V3ConnectorConfigTypedDict


class V3GetConnectorConfigResponse(BaseModel):
    data: V3ConnectorConfig
