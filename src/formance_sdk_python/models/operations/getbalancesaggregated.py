"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    aggregatebalancesresponse as shared_aggregatebalancesresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetBalancesAggregatedRequestTypedDict(TypedDict):
    ledger: str
    r"""Name of the ledger."""
    address: NotRequired[str]
    r"""Filter balances involving given account, either as source or destination."""
    use_insertion_date: NotRequired[bool]
    r"""Use insertion date instead of effective date"""


class GetBalancesAggregatedRequest(BaseModel):
    ledger: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the ledger."""

    address: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter balances involving given account, either as source or destination."""

    use_insertion_date: Annotated[
        Optional[bool],
        pydantic.Field(alias="useInsertionDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Use insertion date instead of effective date"""


class GetBalancesAggregatedResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    aggregate_balances_response: NotRequired[
        shared_aggregatebalancesresponse.AggregateBalancesResponseTypedDict
    ]
    r"""OK"""


class GetBalancesAggregatedResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    aggregate_balances_response: Optional[
        shared_aggregatebalancesresponse.AggregateBalancesResponse
    ] = None
    r"""OK"""
