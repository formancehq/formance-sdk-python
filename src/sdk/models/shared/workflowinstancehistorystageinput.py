"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import activityconfirmhold as shared_activityconfirmhold
from ..shared import activitycreatetransaction as shared_activitycreatetransaction
from ..shared import activitycreditwallet as shared_activitycreditwallet
from ..shared import activitydebitwallet as shared_activitydebitwallet
from ..shared import activitygetaccount as shared_activitygetaccount
from ..shared import activitygetpayment as shared_activitygetpayment
from ..shared import activitygetwallet as shared_activitygetwallet
from ..shared import activitylistwallets as shared_activitylistwallets
from ..shared import activityreverttransaction as shared_activityreverttransaction
from ..shared import activitystripetransfer as shared_activitystripetransfer
from ..shared import activityvoidhold as shared_activityvoidhold
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkflowInstanceHistoryStageInput:
    confirm_hold: Optional[shared_activityconfirmhold.ActivityConfirmHold] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ConfirmHold'), 'exclude': lambda f: f is None }})
    create_transaction: Optional[shared_activitycreatetransaction.ActivityCreateTransaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreateTransaction'), 'exclude': lambda f: f is None }})
    credit_wallet: Optional[shared_activitycreditwallet.ActivityCreditWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreditWallet'), 'exclude': lambda f: f is None }})
    debit_wallet: Optional[shared_activitydebitwallet.ActivityDebitWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DebitWallet'), 'exclude': lambda f: f is None }})
    get_account: Optional[shared_activitygetaccount.ActivityGetAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetAccount'), 'exclude': lambda f: f is None }})
    get_payment: Optional[shared_activitygetpayment.ActivityGetPayment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetPayment'), 'exclude': lambda f: f is None }})
    get_wallet: Optional[shared_activitygetwallet.ActivityGetWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetWallet'), 'exclude': lambda f: f is None }})
    list_wallets: Optional[shared_activitylistwallets.ActivityListWallets] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ListWallets'), 'exclude': lambda f: f is None }})
    revert_transaction: Optional[shared_activityreverttransaction.ActivityRevertTransaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RevertTransaction'), 'exclude': lambda f: f is None }})
    stripe_transfer: Optional[shared_activitystripetransfer.ActivityStripeTransfer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StripeTransfer'), 'exclude': lambda f: f is None }})
    void_hold: Optional[shared_activityvoidhold.ActivityVoidHold] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VoidHold'), 'exclude': lambda f: f is None }})
    

