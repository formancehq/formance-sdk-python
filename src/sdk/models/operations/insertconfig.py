"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import webhookserrorresponse as errors_webhookserrorresponse
from ...models.shared import configresponse as shared_configresponse
from typing import Optional


@dataclasses.dataclass
class InsertConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    r"""Config created successfully."""
    webhooks_error_response: Optional[errors_webhookserrorresponse.WebhooksErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

