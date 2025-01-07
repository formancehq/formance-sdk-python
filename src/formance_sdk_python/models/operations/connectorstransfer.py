"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    connector as shared_connector,
    transferrequest as shared_transferrequest,
    transferresponse as shared_transferresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConnectorsTransferRequestTypedDict(TypedDict):
    transfer_request: shared_transferrequest.TransferRequestTypedDict
    connector: shared_connector.Connector
    r"""The name of the connector."""


class ConnectorsTransferRequest(BaseModel):
    transfer_request: Annotated[
        shared_transferrequest.TransferRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connector: Annotated[
        shared_connector.Connector,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The name of the connector."""


class ConnectorsTransferResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    transfer_response: NotRequired[shared_transferresponse.TransferResponseTypedDict]
    r"""OK"""


class ConnectorsTransferResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    transfer_response: Optional[shared_transferresponse.TransferResponse] = None
    r"""OK"""