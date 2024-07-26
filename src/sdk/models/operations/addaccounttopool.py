"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import addaccounttopoolrequest as shared_addaccounttopoolrequest


@dataclasses.dataclass
class AddAccountToPoolRequest:
    add_account_to_pool_request: shared_addaccounttopoolrequest.AddAccountToPoolRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    pool_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'poolId', 'style': 'simple', 'explode': False }})
    r"""The pool ID."""
    



@dataclasses.dataclass
class AddAccountToPoolResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

