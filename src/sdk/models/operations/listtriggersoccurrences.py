"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import listtriggersoccurrencesresponse as shared_listtriggersoccurrencesresponse
from typing import Optional


@dataclasses.dataclass
class ListTriggersOccurrencesRequest:
    trigger_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'triggerID', 'style': 'simple', 'explode': False }})
    r"""The trigger id"""
    



@dataclasses.dataclass
class ListTriggersOccurrencesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""General error"""
    list_triggers_occurrences_response: Optional[shared_listtriggersoccurrencesresponse.ListTriggersOccurrencesResponse] = dataclasses.field(default=None)
    r"""List of triggers occurrences"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
