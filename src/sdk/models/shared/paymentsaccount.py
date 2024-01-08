"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Dict, List, Optional


@dataclasses.dataclass
class PaymentsAccountRaw:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentsAccount:
    account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName') }})
    connector_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectorID') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    default_asset: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultAsset') }})
    default_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultCurrency') }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    metadata: Optional[Dict[str, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    raw: Optional[PaymentsAccountRaw] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    pools: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pools'), 'exclude': lambda f: f is None }})
    

