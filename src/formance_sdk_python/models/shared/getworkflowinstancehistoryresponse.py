"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .workflowinstancehistory import (
    WorkflowInstanceHistory,
    WorkflowInstanceHistoryTypedDict,
)
from formance_sdk_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class GetWorkflowInstanceHistoryResponseTypedDict(TypedDict):
    data: List[WorkflowInstanceHistoryTypedDict]


class GetWorkflowInstanceHistoryResponse(BaseModel):
    data: List[WorkflowInstanceHistory]
