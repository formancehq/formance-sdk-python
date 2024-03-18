"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import errorresponse as errors_errorresponse
from ...models.shared import configinforesponse as shared_configinforesponse
from typing import Optional


@dataclasses.dataclass
class GetInfoResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    config_info_response: Optional[shared_configinforesponse.ConfigInfoResponse] = dataclasses.field(default=None)
    r"""OK"""
    error_response: Optional[errors_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

