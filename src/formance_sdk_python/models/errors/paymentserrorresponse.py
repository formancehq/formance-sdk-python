"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python import utils
from formance_sdk_python.models.shared import (
    paymentserrorsenum as shared_paymentserrorsenum,
)
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated


class PaymentsErrorResponseData(BaseModel):
    error_code: Annotated[
        shared_paymentserrorsenum.PaymentsErrorsEnum, pydantic.Field(alias="errorCode")
    ]

    error_message: Annotated[str, pydantic.Field(alias="errorMessage")]


class PaymentsErrorResponse(Exception):
    r"""Error"""

    data: PaymentsErrorResponseData

    def __init__(self, data: PaymentsErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PaymentsErrorResponseData)
