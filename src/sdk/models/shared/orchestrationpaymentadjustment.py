"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .orchestrationpaymentstatus import OrchestrationPaymentStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils


@dataclasses.dataclass
class OrchestrationPaymentAdjustmentRaw:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrchestrationPaymentAdjustment:
    absolute: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('absolute') }})
    amount: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    raw: OrchestrationPaymentAdjustmentRaw = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    status: OrchestrationPaymentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

