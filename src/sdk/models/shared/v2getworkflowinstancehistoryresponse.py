"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import v2workflowinstancehistory as shared_v2workflowinstancehistory
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2GetWorkflowInstanceHistoryResponse:
    data: List[shared_v2workflowinstancehistory.V2WorkflowInstanceHistory] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

