"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class V3RetryPaymentInitiationResponseDataTypedDict(TypedDict):
    task_id: str
    r"""Since this call is asynchronous, the response will contain the ID of the task that was created to retry the payment initiation to the PSP. You can use the task API to check the status of the task and get the resulting payment ID.

    """


class V3RetryPaymentInitiationResponseData(BaseModel):
    task_id: Annotated[str, pydantic.Field(alias="taskID")]
    r"""Since this call is asynchronous, the response will contain the ID of the task that was created to retry the payment initiation to the PSP. You can use the task API to check the status of the task and get the resulting payment ID.

    """


class V3RetryPaymentInitiationResponseTypedDict(TypedDict):
    data: V3RetryPaymentInitiationResponseDataTypedDict


class V3RetryPaymentInitiationResponse(BaseModel):
    data: V3RetryPaymentInitiationResponseData
