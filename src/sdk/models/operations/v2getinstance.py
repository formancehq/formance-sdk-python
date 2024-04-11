"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import v2getworkflowinstanceresponse as shared_v2getworkflowinstanceresponse
from typing import Optional


@dataclasses.dataclass
class V2GetInstanceRequest:
    instance_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'instanceID', 'style': 'simple', 'explode': False }})
    r"""The instance id"""
    



@dataclasses.dataclass
class V2GetInstanceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_get_workflow_instance_response: Optional[shared_v2getworkflowinstanceresponse.V2GetWorkflowInstanceResponse] = dataclasses.field(default=None)
    r"""The workflow instance"""
    

