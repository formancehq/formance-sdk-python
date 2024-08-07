"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from datetime import datetime
from typing import Dict, List, Optional


@dataclasses.dataclass
class Metadata:
    r"""Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below."""
    



@dataclasses.dataclass
class CountTransactionsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    account: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'account', 'style': 'form', 'explode': True }})
    r"""Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $)."""
    destination: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'destination', 'style': 'form', 'explode': True }})
    r"""Filter transactions with postings involving given account at destination (regular expression placed between ^ and $)."""
    end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'endTime', 'style': 'form', 'explode': True }})
    r"""Filter transactions that occurred before this timestamp.
    The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute).
    """
    metadata: Optional[Metadata] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    r"""Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below."""
    reference: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'reference', 'style': 'form', 'explode': True }})
    r"""Filter transactions by reference field."""
    source: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'source', 'style': 'form', 'explode': True }})
    r"""Filter transactions with postings involving given account at source (regular expression placed between ^ and $)."""
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'startTime', 'style': 'form', 'explode': True }})
    r"""Filter transactions that occurred after this timestamp.
    The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute).
    """
    



@dataclasses.dataclass
class CountTransactionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

