"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentstatus import PaymentStatus
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TaskModulrDescriptorTypedDict(TypedDict):
    account_id: NotRequired[str]
    key: NotRequired[str]
    name: NotRequired[str]


class TaskModulrDescriptor(BaseModel):
    account_id: Annotated[Optional[str], pydantic.Field(alias="accountID")] = None

    key: Optional[str] = None

    name: Optional[str] = None


class TaskModulrStateTypedDict(TypedDict):
    pass


class TaskModulrState(BaseModel):
    pass


class TaskModulrTypedDict(TypedDict):
    connector_id: str
    created_at: datetime
    descriptor: TaskModulrDescriptorTypedDict
    id: str
    state: TaskModulrStateTypedDict
    status: PaymentStatus
    updated_at: datetime
    error: NotRequired[str]


class TaskModulr(BaseModel):
    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    descriptor: TaskModulrDescriptor

    id: str

    state: TaskModulrState

    status: PaymentStatus

    updated_at: Annotated[datetime, pydantic.Field(alias="updatedAt")]

    error: Optional[str] = None
