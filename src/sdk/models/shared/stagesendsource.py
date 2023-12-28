"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import stagesendsourceaccount as shared_stagesendsourceaccount
from ..shared import stagesendsourcepayment as shared_stagesendsourcepayment
from ..shared import stagesendsourcewallet as shared_stagesendsourcewallet
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StageSendSource:
    account: Optional[shared_stagesendsourceaccount.StageSendSourceAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account'), 'exclude': lambda f: f is None }})
    payment: Optional[shared_stagesendsourcepayment.StageSendSourcePayment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment'), 'exclude': lambda f: f is None }})
    wallet: Optional[shared_stagesendsourcewallet.StageSendSourceWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet'), 'exclude': lambda f: f is None }})
    

