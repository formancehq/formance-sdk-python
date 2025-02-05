"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentstatus import PaymentStatus
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TaskDummyPayDescriptorTypedDict(TypedDict):
    file_name: NotRequired[str]
    key: NotRequired[str]
    name: NotRequired[str]


class TaskDummyPayDescriptor(BaseModel):
    file_name: Annotated[Optional[str], pydantic.Field(alias="fileName")] = None

    key: Optional[str] = None

    name: Optional[str] = None


class TaskDummyPayStateTypedDict(TypedDict):
    pass


class TaskDummyPayState(BaseModel):
    pass


class TaskDummyPayTypedDict(TypedDict):
    connector_id: str
    created_at: datetime
    descriptor: TaskDummyPayDescriptorTypedDict
    id: str
    state: TaskDummyPayStateTypedDict
    status: PaymentStatus
    updated_at: datetime
    error: NotRequired[str]


class TaskDummyPay(BaseModel):
    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    descriptor: TaskDummyPayDescriptor

    id: str

    state: TaskDummyPayState

    status: PaymentStatus

    updated_at: Annotated[datetime, pydantic.Field(alias="updatedAt")]

    error: Optional[str] = None
