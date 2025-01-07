"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    connector as shared_connector,
    connectorconfigresponse as shared_connectorconfigresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReadConnectorConfigRequestTypedDict(TypedDict):
    connector: shared_connector.Connector
    r"""The name of the connector."""


class ReadConnectorConfigRequest(BaseModel):
    connector: Annotated[
        shared_connector.Connector,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The name of the connector."""


class ReadConnectorConfigResponseTypedDict(TypedDict):
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


class ReadConnectorConfigResponse(BaseModel):
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
