"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import mapping as shared_mapping
from ...models.shared import mappingresponse as shared_mappingresponse
from typing import Optional


@dataclasses.dataclass
class UpdateMappingRequest:
    mapping: Optional[shared_mapping.Mapping] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    



@dataclasses.dataclass
class UpdateMappingResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    mapping_response: Optional[shared_mappingresponse.MappingResponse] = dataclasses.field(default=None)
    r"""OK"""
    

