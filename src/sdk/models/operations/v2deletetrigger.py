"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import v2error as errors_v2error
from typing import Optional


@dataclasses.dataclass
class V2DeleteTriggerRequest:
    trigger_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'triggerID', 'style': 'simple', 'explode': False }})
    r"""The trigger id"""
    



@dataclasses.dataclass
class V2DeleteTriggerResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    v2_error: Optional[errors_v2error.V2Error] = dataclasses.field(default=None)
    r"""General error"""
    

