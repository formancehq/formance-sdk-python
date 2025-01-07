"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from formance_sdk_python import utils
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated


class SchemasWalletsErrorResponseErrorCode(str, Enum):
    VALIDATION = "VALIDATION"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INSUFFICIENT_FUND = "INSUFFICIENT_FUND"
    HOLD_CLOSED = "HOLD_CLOSED"


class WalletsErrorResponseData(BaseModel):
    error_code: Annotated[
        SchemasWalletsErrorResponseErrorCode, pydantic.Field(alias="errorCode")
    ]

    error_message: Annotated[str, pydantic.Field(alias="errorMessage")]


class WalletsErrorResponse(Exception):
    data: WalletsErrorResponseData

    def __init__(self, data: WalletsErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, WalletsErrorResponseData)