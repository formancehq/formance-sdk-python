"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import v2workflowinstancehistorystage as shared_v2workflowinstancehistorystage
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2GetWorkflowInstanceHistoryStageResponse:
    data: List[shared_v2workflowinstancehistorystage.V2WorkflowInstanceHistoryStage] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    
