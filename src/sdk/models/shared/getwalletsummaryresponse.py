"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .balancewithassets import BalanceWithAssets
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Dict, List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWalletSummaryResponse:
    available_funds: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availableFunds') }})
    balances: List[BalanceWithAssets] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balances') }})
    expirable_funds: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expirableFunds') }})
    expired_funds: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiredFunds') }})
    hold_funds: Dict[str, int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('holdFunds') }})
    

