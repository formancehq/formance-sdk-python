"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subject import Subject, SubjectTypedDict
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import validate_int
import pydantic
from pydantic.functional_validators import BeforeValidator
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ExpandedDebitHoldTypedDict(TypedDict):
    description: str
    id: str
    r"""The unique ID of the hold."""
    metadata: Dict[str, str]
    r"""Metadata associated with the hold."""
    original_amount: int
    r"""Original amount on hold"""
    remaining: int
    r"""Remaining amount on hold"""
    wallet_id: str
    r"""The ID of the wallet the hold is associated with."""
    destination: NotRequired[SubjectTypedDict]


class ExpandedDebitHold(BaseModel):
    description: str

    id: str
    r"""The unique ID of the hold."""

    metadata: Dict[str, str]
    r"""Metadata associated with the hold."""

    original_amount: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        pydantic.Field(alias="originalAmount"),
    ]
    r"""Original amount on hold"""

    remaining: Annotated[int, BeforeValidator(validate_int)]
    r"""Remaining amount on hold"""

    wallet_id: Annotated[str, pydantic.Field(alias="walletID")]
    r"""The ID of the wallet the hold is associated with."""

    destination: Optional[Subject] = None