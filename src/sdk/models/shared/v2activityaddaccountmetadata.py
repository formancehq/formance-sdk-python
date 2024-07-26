"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Dict


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2ActivityAddAccountMetadata:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    ledger: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledger') }})
    metadata: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    

