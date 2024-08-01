"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import v2aggregatebalancesresponse as shared_v2aggregatebalancesresponse
from datetime import datetime
from typing import Any, Dict, Optional


@dataclasses.dataclass
class V2GetBalancesAggregatedRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    request_body: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    pit: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pit', 'style': 'form', 'explode': True }})
    use_insertion_date: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'useInsertionDate', 'style': 'form', 'explode': True }})
    r"""Use insertion date instead of effective date"""
    



@dataclasses.dataclass
class V2GetBalancesAggregatedResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_aggregate_balances_response: Optional[shared_v2aggregatebalancesresponse.V2AggregateBalancesResponse] = dataclasses.field(default=None)
    r"""OK"""
    

