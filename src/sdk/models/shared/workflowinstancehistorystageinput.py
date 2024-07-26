"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .activityaddaccountmetadata import ActivityAddAccountMetadata
from .activityconfirmhold import ActivityConfirmHold
from .activitycreatetransaction import ActivityCreateTransaction
from .activitycreditwallet import ActivityCreditWallet
from .activitydebitwallet import ActivityDebitWallet
from .activitygetaccount import ActivityGetAccount
from .activitygetpayment import ActivityGetPayment
from .activitygetwallet import ActivityGetWallet
from .activitylistwallets import ActivityListWallets
from .activityreverttransaction import ActivityRevertTransaction
from .activitystripetransfer import ActivityStripeTransfer
from .activityvoidhold import ActivityVoidHold
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkflowInstanceHistoryStageInput:
    add_account_metadata: Optional[ActivityAddAccountMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AddAccountMetadata'), 'exclude': lambda f: f is None }})
    confirm_hold: Optional[ActivityConfirmHold] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ConfirmHold'), 'exclude': lambda f: f is None }})
    create_transaction: Optional[ActivityCreateTransaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreateTransaction'), 'exclude': lambda f: f is None }})
    credit_wallet: Optional[ActivityCreditWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreditWallet'), 'exclude': lambda f: f is None }})
    debit_wallet: Optional[ActivityDebitWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DebitWallet'), 'exclude': lambda f: f is None }})
    get_account: Optional[ActivityGetAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetAccount'), 'exclude': lambda f: f is None }})
    get_payment: Optional[ActivityGetPayment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetPayment'), 'exclude': lambda f: f is None }})
    get_wallet: Optional[ActivityGetWallet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetWallet'), 'exclude': lambda f: f is None }})
    list_wallets: Optional[ActivityListWallets] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ListWallets'), 'exclude': lambda f: f is None }})
    revert_transaction: Optional[ActivityRevertTransaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RevertTransaction'), 'exclude': lambda f: f is None }})
    stripe_transfer: Optional[ActivityStripeTransfer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StripeTransfer'), 'exclude': lambda f: f is None }})
    void_hold: Optional[ActivityVoidHold] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VoidHold'), 'exclude': lambda f: f is None }})
    

