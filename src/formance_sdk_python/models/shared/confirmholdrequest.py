"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import validate_int
from pydantic.functional_validators import BeforeValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConfirmHoldRequestTypedDict(TypedDict):
    amount: NotRequired[int]
    r"""Define the amount to transfer."""
    final: NotRequired[bool]
    r"""Define a final confirmation. Remaining funds will be returned to the wallet."""


class ConfirmHoldRequest(BaseModel):
    amount: Annotated[Optional[int], BeforeValidator(validate_int)] = None
    r"""Define the amount to transfer."""

    final: Optional[bool] = None
    r"""Define a final confirmation. Remaining funds will be returned to the wallet."""
