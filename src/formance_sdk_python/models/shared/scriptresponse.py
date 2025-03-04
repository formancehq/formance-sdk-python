"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .errorsenum import ErrorsEnum
from .transaction import Transaction, TransactionTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ScriptResponseTypedDict(TypedDict):
    details: NotRequired[str]
    error_code: NotRequired[ErrorsEnum]
    error_message: NotRequired[str]
    transaction: NotRequired[TransactionTypedDict]


class ScriptResponse(BaseModel):
    details: Optional[str] = None

    error_code: Annotated[Optional[ErrorsEnum], pydantic.Field(alias="errorCode")] = (
        None
    )

    error_message: Annotated[Optional[str], pydantic.Field(alias="errorMessage")] = None

    transaction: Optional[Transaction] = None
