"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Optional


class V2MigrationInfoState(str, Enum):
    TO_DO = 'TO DO'
    DONE = 'DONE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2MigrationInfo:
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    state: Optional[V2MigrationInfoState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    

