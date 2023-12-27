"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import v2error as shared_v2error
from ..shared import v2listworkflowsresponse as shared_v2listworkflowsresponse
from typing import Optional


@dataclasses.dataclass
class V2ListWorkflowsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_error: Optional[shared_v2error.V2Error] = dataclasses.field(default=None)
    r"""General error"""
    v2_list_workflows_response: Optional[shared_v2listworkflowsresponse.V2ListWorkflowsResponse] = dataclasses.field(default=None)
    r"""List of workflows"""
    
