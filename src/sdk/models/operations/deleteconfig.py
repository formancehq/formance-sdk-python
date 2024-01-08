"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import webhookserrorresponse as errors_webhookserrorresponse
from typing import Optional


@dataclasses.dataclass
class DeleteConfigRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Config ID"""
    



@dataclasses.dataclass
class DeleteConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    webhooks_error_response: Optional[errors_webhookserrorresponse.WebhooksErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

