"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import policyresponse as shared_policyresponse
from ..shared import reconciliationerrorresponse as shared_reconciliationerrorresponse
from typing import Optional


@dataclasses.dataclass
class GetPolicyRequest:
    policy_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'policyID', 'style': 'simple', 'explode': False }})
    r"""The policy ID."""
    



@dataclasses.dataclass
class GetPolicyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    policy_response: Optional[shared_policyresponse.PolicyResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    reconciliation_error_response: Optional[shared_reconciliationerrorresponse.ReconciliationErrorResponse] = dataclasses.field(default=None)
    r"""Error response"""
    

