"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import getworkflowinstancehistorystageresponse as shared_getworkflowinstancehistorystageresponse
from typing import Optional


@dataclasses.dataclass
class GetInstanceStageHistoryRequest:
    instance_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'instanceID', 'style': 'simple', 'explode': False }})
    r"""The instance id"""
    number: int = dataclasses.field(metadata={'path_param': { 'field_name': 'number', 'style': 'simple', 'explode': False }})
    r"""The stage number"""
    



@dataclasses.dataclass
class GetInstanceStageHistoryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""General error"""
    get_workflow_instance_history_stage_response: Optional[shared_getworkflowinstancehistorystageresponse.GetWorkflowInstanceHistoryStageResponse] = dataclasses.field(default=None)
    r"""The workflow instance stage history"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

