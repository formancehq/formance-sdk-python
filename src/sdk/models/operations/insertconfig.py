"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import configresponse as shared_configresponse
from ..shared import webhookserrorresponse as shared_webhookserrorresponse
from typing import Optional


@dataclasses.dataclass
class InsertConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    r"""Config created successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhooks_error_response: Optional[shared_webhookserrorresponse.WebhooksErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

