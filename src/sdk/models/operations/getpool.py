"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import poolresponse as shared_poolresponse
from typing import Optional


@dataclasses.dataclass
class GetPoolRequest:
    pool_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'poolId', 'style': 'simple', 'explode': False }})
    r"""The pool ID."""
    



@dataclasses.dataclass
class GetPoolResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    pool_response: Optional[shared_poolresponse.PoolResponse] = dataclasses.field(default=None)
    r"""OK"""
    

