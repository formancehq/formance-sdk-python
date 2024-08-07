"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import v2listtriggersoccurrencesresponse as shared_v2listtriggersoccurrencesresponse
from typing import Optional


@dataclasses.dataclass
class V2ListTriggersOccurrencesRequest:
    trigger_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'triggerID', 'style': 'simple', 'explode': False }})
    r"""The trigger id"""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when this parameter is set.
    """
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page."""
    



@dataclasses.dataclass
class V2ListTriggersOccurrencesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_list_triggers_occurrences_response: Optional[shared_v2listtriggersoccurrencesresponse.V2ListTriggersOccurrencesResponse] = dataclasses.field(default=None)
    r"""List of triggers occurrences"""
    

