"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .workflowinstance import WorkflowInstance, WorkflowInstanceTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TriggerOccurrenceTypedDict(TypedDict):
    date_: datetime
    event: Dict[str, Any]
    trigger_id: str
    error: NotRequired[str]
    workflow_instance: NotRequired[WorkflowInstanceTypedDict]
    workflow_instance_id: NotRequired[str]


class TriggerOccurrence(BaseModel):
    date_: Annotated[datetime, pydantic.Field(alias="date")]

    event: Dict[str, Any]

    trigger_id: Annotated[str, pydantic.Field(alias="triggerID")]

    error: Optional[str] = None

    workflow_instance: Annotated[
        Optional[WorkflowInstance], pydantic.Field(alias="workflowInstance")
    ] = None

    workflow_instance_id: Annotated[
        Optional[str], pydantic.Field(alias="workflowInstanceID")
    ] = None
