"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Any, Dict


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2TriggerOccurrence:
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    event: Dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event') }})
    trigger_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('triggerID') }})
    workflow_instance_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowInstanceID') }})
    

