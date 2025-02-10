"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2posting import V2Posting, V2PostingTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class OrchestrationV2PostTransactionScriptTypedDict(TypedDict):
    plain: str
    vars: NotRequired[Dict[str, Any]]


class OrchestrationV2PostTransactionScript(BaseModel):
    plain: str

    vars: Optional[Dict[str, Any]] = None


class OrchestrationV2PostTransactionTypedDict(TypedDict):
    metadata: Dict[str, str]
    postings: NotRequired[List[V2PostingTypedDict]]
    reference: NotRequired[str]
    script: NotRequired[OrchestrationV2PostTransactionScriptTypedDict]
    timestamp: NotRequired[datetime]


class OrchestrationV2PostTransaction(BaseModel):
    metadata: Dict[str, str]

    postings: Optional[List[V2Posting]] = None

    reference: Optional[str] = None

    script: Optional[OrchestrationV2PostTransactionScript] = None

    timestamp: Optional[datetime] = None
