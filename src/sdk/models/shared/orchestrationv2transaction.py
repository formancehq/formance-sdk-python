"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .v2posting import V2Posting
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrchestrationV2Transaction:
    metadata: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    postings: List[V2Posting] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postings') }})
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    txid: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('txid') }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    

