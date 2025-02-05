"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2workflowinstancehistorystageinput import (
    V2WorkflowInstanceHistoryStageInput,
    V2WorkflowInstanceHistoryStageInputTypedDict,
)
from .v2workflowinstancehistorystageoutput import (
    V2WorkflowInstanceHistoryStageOutput,
    V2WorkflowInstanceHistoryStageOutputTypedDict,
)
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2WorkflowInstanceHistoryStageTypedDict(TypedDict):
    attempt: int
    input: V2WorkflowInstanceHistoryStageInputTypedDict
    name: str
    started_at: datetime
    terminated: bool
    error: NotRequired[str]
    last_failure: NotRequired[str]
    next_execution: NotRequired[datetime]
    output: NotRequired[V2WorkflowInstanceHistoryStageOutputTypedDict]
    terminated_at: NotRequired[datetime]


class V2WorkflowInstanceHistoryStage(BaseModel):
    attempt: int

    input: V2WorkflowInstanceHistoryStageInput

    name: str

    started_at: Annotated[datetime, pydantic.Field(alias="startedAt")]

    terminated: bool

    error: Optional[str] = None

    last_failure: Annotated[Optional[str], pydantic.Field(alias="lastFailure")] = None

    next_execution: Annotated[
        Optional[datetime], pydantic.Field(alias="nextExecution")
    ] = None

    output: Optional[V2WorkflowInstanceHistoryStageOutput] = None

    terminated_at: Annotated[
        Optional[datetime], pydantic.Field(alias="terminatedAt")
    ] = None
