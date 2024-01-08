"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .orchestrationposttransaction import OrchestrationPostTransaction
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityCreateTransaction:
    data: Optional[OrchestrationPostTransaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    ledger: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledger'), 'exclude': lambda f: f is None }})
    

