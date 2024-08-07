"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReconciliationRequest:
    reconciled_at_ledger: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reconciledAtLedger'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    reconciled_at_payments: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reconciledAtPayments'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    

