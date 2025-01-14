"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .workflowinstance import WorkflowInstance, WorkflowInstanceTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class RunWorkflowResponseTypedDict(TypedDict):
    data: WorkflowInstanceTypedDict


class RunWorkflowResponse(BaseModel):
    data: WorkflowInstance
