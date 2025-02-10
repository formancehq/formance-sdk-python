"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2posting import V2Posting, V2PostingTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class V2PostTransactionScriptTypedDict(TypedDict):
    plain: str
    vars: NotRequired[Dict[str, str]]


class V2PostTransactionScript(BaseModel):
    plain: str

    vars: Optional[Dict[str, str]] = None


class V2PostTransactionTypedDict(TypedDict):
    metadata: Dict[str, str]
    postings: NotRequired[List[V2PostingTypedDict]]
    reference: NotRequired[str]
    script: NotRequired[V2PostTransactionScriptTypedDict]
    timestamp: NotRequired[datetime]


class V2PostTransaction(BaseModel):
    metadata: Dict[str, str]

    postings: Optional[List[V2Posting]] = None

    reference: Optional[str] = None

    script: Optional[V2PostTransactionScript] = None

    timestamp: Optional[datetime] = None
