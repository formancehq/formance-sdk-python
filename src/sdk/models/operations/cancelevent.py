"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class CancelEventRequest:
    instance_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'instanceID', 'style': 'simple', 'explode': False }})
    r"""The instance id"""
    



@dataclasses.dataclass
class CancelEventResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""General error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

