"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    connector as shared_connector,
    connectorconfigresponse as shared_connectorconfigresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReadConnectorConfigV1RequestTypedDict(TypedDict):
    connector: shared_connector.Connector
    r"""The name of the connector."""
    connector_id: str
    r"""The connector ID."""


class ReadConnectorConfigV1Request(BaseModel):
    connector: Annotated[
        shared_connector.Connector,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The name of the connector."""

    connector_id: Annotated[
        str,
        pydantic.Field(alias="connectorId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The connector ID."""


class ReadConnectorConfigV1ResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    connector_config_response: NotRequired[
        shared_connectorconfigresponse.ConnectorConfigResponseTypedDict
    ]
    r"""OK"""


class ReadConnectorConfigV1Response(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    connector_config_response: Optional[
        shared_connectorconfigresponse.ConnectorConfigResponse
    ] = None
    r"""OK"""