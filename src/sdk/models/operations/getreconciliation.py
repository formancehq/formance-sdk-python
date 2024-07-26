"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import reconciliationresponse as shared_reconciliationresponse
from typing import Optional


@dataclasses.dataclass
class GetReconciliationRequest:
    reconciliation_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'reconciliationID', 'style': 'simple', 'explode': False }})
    r"""The reconciliation ID."""
    



@dataclasses.dataclass
class GetReconciliationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    reconciliation_response: Optional[shared_reconciliationresponse.ReconciliationResponse] = dataclasses.field(default=None)
    r"""OK"""
    

