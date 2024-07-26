"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .posting import Posting
from .volume import Volume
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Transaction:
    UNSET='__SPEAKEASY_UNSET__'
    postings: List[Posting] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postings') }})
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    txid: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('txid') }})
    metadata: Optional[Dict[str, Any]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is Transaction.UNSET }})
    post_commit_volumes: Optional[Dict[str, Dict[str, Volume]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postCommitVolumes'), 'exclude': lambda f: f is None }})
    pre_commit_volumes: Optional[Dict[str, Dict[str, Volume]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preCommitVolumes'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    

