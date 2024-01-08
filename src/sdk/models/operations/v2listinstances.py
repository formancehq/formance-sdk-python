"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import v2error as errors_v2error
from ...models.shared import v2listrunsresponse as shared_v2listrunsresponse
from typing import Optional


@dataclasses.dataclass
class V2ListInstancesRequest:
    running: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'running', 'style': 'form', 'explode': True }})
    r"""Filter running instances"""
    workflow_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workflowID', 'style': 'form', 'explode': True }})
    r"""A workflow id"""
    



@dataclasses.dataclass
class V2ListInstancesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    v2_error: Optional[errors_v2error.V2Error] = dataclasses.field(default=None)
    r"""General error"""
    v2_list_runs_response: Optional[shared_v2listrunsresponse.V2ListRunsResponse] = dataclasses.field(default=None)
    r"""List of workflow instances"""
    

