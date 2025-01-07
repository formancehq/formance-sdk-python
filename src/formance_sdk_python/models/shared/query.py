"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class QueryRawTypedDict(TypedDict):
    pass


class QueryRaw(BaseModel):
    pass


class QueryTypedDict(TypedDict):
    after: NotRequired[List[str]]
    cursor: NotRequired[str]
    ledgers: NotRequired[List[str]]
    page_size: NotRequired[int]
    policy: NotRequired[str]
    raw: NotRequired[QueryRawTypedDict]
    sort: NotRequired[str]
    target: NotRequired[str]
    terms: NotRequired[List[str]]


class Query(BaseModel):
    after: Optional[List[str]] = None

    cursor: Optional[str] = None

    ledgers: Optional[List[str]] = None

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None

    policy: Optional[str] = None

    raw: Optional[QueryRaw] = None

    sort: Optional[str] = None

    target: Optional[str] = None

    terms: Optional[List[str]] = None
