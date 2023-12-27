"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import v2configinforesponse as shared_v2configinforesponse
from ..shared import v2errorresponse as shared_v2errorresponse
from typing import Optional


@dataclasses.dataclass
class V2GetInfoResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_config_info_response: Optional[shared_v2configinforesponse.V2ConfigInfoResponse] = dataclasses.field(default=None)
    r"""OK"""
    v2_error_response: Optional[shared_v2errorresponse.V2ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

