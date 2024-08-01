"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .v2targetid import V2TargetID
from .v2targettype import V2TargetType
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2BulkElementDeleteMetadataData:
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    target_id: V2TargetID = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targetId') }})
    target_type: V2TargetType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targetType') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2BulkElementDeleteMetadata:
    action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    data: Optional[V2BulkElementDeleteMetadataData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    ik: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ik'), 'exclude': lambda f: f is None }})
    

