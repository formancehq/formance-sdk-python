"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .version import Version
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetVersionsResponse:
    env: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('env') }})
    region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    versions: List[Version] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('versions') }})
    

