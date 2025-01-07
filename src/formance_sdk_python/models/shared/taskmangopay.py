"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentstatus import PaymentStatus
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TaskMangoPayDescriptorTypedDict(TypedDict):
    key: NotRequired[str]
    name: NotRequired[str]
    user_id: NotRequired[str]


class TaskMangoPayDescriptor(BaseModel):
    key: Optional[str] = None

    name: Optional[str] = None

    user_id: Annotated[Optional[str], pydantic.Field(alias="userID")] = None


class TaskMangoPayStateTypedDict(TypedDict):
    pass


class TaskMangoPayState(BaseModel):
    pass


class TaskMangoPayTypedDict(TypedDict):
    connector_id: str
    created_at: datetime
    descriptor: TaskMangoPayDescriptorTypedDict
    id: str
    state: TaskMangoPayStateTypedDict
    status: PaymentStatus
    updated_at: datetime
    error: NotRequired[str]


class TaskMangoPay(BaseModel):
    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    descriptor: TaskMangoPayDescriptor

    id: str

    state: TaskMangoPayState

    status: PaymentStatus

    updated_at: Annotated[datetime, pydantic.Field(alias="updatedAt")]

    error: Optional[str] = None