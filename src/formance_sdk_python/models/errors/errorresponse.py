"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python import utils
from formance_sdk_python.models.shared import errorsenum as shared_errorsenum
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class ErrorResponseData(BaseModel):
    error_code: Annotated[
        shared_errorsenum.ErrorsEnum, pydantic.Field(alias="errorCode")
    ]

    error_message: Annotated[str, pydantic.Field(alias="errorMessage")]

    details: Optional[str] = None


class ErrorResponse(Exception):
    data: ErrorResponseData

    def __init__(self, data: ErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorResponseData)