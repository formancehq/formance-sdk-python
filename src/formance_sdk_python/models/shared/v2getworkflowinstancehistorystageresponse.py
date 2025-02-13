"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2workflowinstancehistorystage import (
    V2WorkflowInstanceHistoryStage,
    V2WorkflowInstanceHistoryStageTypedDict,
)
from formance_sdk_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class V2GetWorkflowInstanceHistoryStageResponseTypedDict(TypedDict):
    data: List[V2WorkflowInstanceHistoryStageTypedDict]


class V2GetWorkflowInstanceHistoryStageResponse(BaseModel):
    data: List[V2WorkflowInstanceHistoryStage]
