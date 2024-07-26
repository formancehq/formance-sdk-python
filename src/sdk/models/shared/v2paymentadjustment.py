"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .v2paymentstatus import V2PaymentStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils


@dataclasses.dataclass
class V2PaymentAdjustmentRaw:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2PaymentAdjustment:
    absolute: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('absolute') }})
    amount: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    raw: V2PaymentAdjustmentRaw = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    status: V2PaymentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

