"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .v2ledgeraccountsubject import V2LedgerAccountSubject
from .v2monetary import V2Monetary
from .v2walletsubject import V2WalletSubject
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Dict, List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2DebitWalletRequest:
    amount: V2Monetary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    metadata: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""Metadata associated with the wallet."""
    balances: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balances'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    destination: Optional[Union[V2LedgerAccountSubject, V2WalletSubject]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination'), 'exclude': lambda f: f is None }})
    pending: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending'), 'exclude': lambda f: f is None }})
    r"""Set to true to create a pending hold. If false, the wallet will be debited immediately."""
    timestamp: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""cannot be used in conjunction with `pending` property"""
    

