"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Dict


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PolicyRequest:
    ledger_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledgerName') }})
    ledger_query: Dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledgerQuery') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    payments_pool_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentsPoolID') }})
    

