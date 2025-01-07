"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    createworkflowresponse as shared_createworkflowresponse,
)
from formance_sdk_python.types import BaseModel
import httpx
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateWorkflowResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    create_workflow_response: NotRequired[
        shared_createworkflowresponse.CreateWorkflowResponseTypedDict
    ]
    r"""Created workflow"""


class CreateWorkflowResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    create_workflow_response: Optional[
        shared_createworkflowresponse.CreateWorkflowResponse
    ] = None
    r"""Created workflow"""