"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .v2assetholder import V2AssetHolder
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Dict


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Balances:
    main: V2AssetHolder = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('main') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2WalletWithBalances:
    balances: Balances = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balances') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the wallet."""
    ledger: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledger') }})
    metadata: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""Metadata associated with the wallet."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    

