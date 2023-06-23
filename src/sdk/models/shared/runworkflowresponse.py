"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import workflowinstance as shared_workflowinstance
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RunWorkflowResponse:
    r"""The workflow instance"""
    data: shared_workflowinstance.WorkflowInstance = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

