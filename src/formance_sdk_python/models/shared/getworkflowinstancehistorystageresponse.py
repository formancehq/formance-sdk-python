"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .workflowinstancehistorystage import (
    WorkflowInstanceHistoryStage,
    WorkflowInstanceHistoryStageTypedDict,
)
from formance_sdk_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class GetWorkflowInstanceHistoryStageResponseTypedDict(TypedDict):
    data: List[WorkflowInstanceHistoryStageTypedDict]


class GetWorkflowInstanceHistoryStageResponse(BaseModel):
    data: List[WorkflowInstanceHistoryStage]