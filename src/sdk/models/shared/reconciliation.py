"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Reconciliation:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    drift_balances: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('driftBalances') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    ledger_balances: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledgerBalances') }})
    payments_balances: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentsBalances') }})
    policy_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyID') }})
    reconciled_at_ledger: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reconciledAtLedger'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    reconciled_at_payments: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reconciledAtPayments'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    

