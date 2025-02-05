"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2posting import V2Posting, V2PostingTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import validate_int
from pydantic.functional_validators import BeforeValidator
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2TransactionTypedDict(TypedDict):
    id: int
    metadata: Dict[str, str]
    postings: List[V2PostingTypedDict]
    reverted: bool
    timestamp: datetime
    reference: NotRequired[str]


class V2Transaction(BaseModel):
    id: Annotated[int, BeforeValidator(validate_int)]

    metadata: Dict[str, str]

    postings: List[V2Posting]

    reverted: bool

    timestamp: datetime

    reference: Optional[str] = None
