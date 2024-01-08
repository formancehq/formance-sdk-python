"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .activitycreatetransactionoutput import ActivityCreateTransactionOutput
from .activitydebitwalletoutput import ActivityDebitWalletOutput
from .activitygetaccountoutput import ActivityGetAccountOutput
from .activitygetpaymentoutput import ActivityGetPaymentOutput
from .activitygetwalletoutput import ActivityGetWalletOutput
from .activityreverttransactionoutput import ActivityRevertTransactionOutput
from .orchestrationlistwalletsresponse import OrchestrationListWalletsResponse
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkflowInstanceHistoryStageOutput:
    create_transaction: Optional[ActivityCreateTransactionOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreateTransaction'), 'exclude': lambda f: f is None }})
    debit_wallet: Optional[ActivityDebitWalletOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DebitWallet'), 'exclude': lambda f: f is None }})
    get_account: Optional[ActivityGetAccountOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetAccount'), 'exclude': lambda f: f is None }})
    get_payment: Optional[ActivityGetPaymentOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetPayment'), 'exclude': lambda f: f is None }})
    get_wallet: Optional[ActivityGetWalletOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetWallet'), 'exclude': lambda f: f is None }})
    list_wallets: Optional[OrchestrationListWalletsResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ListWallets'), 'exclude': lambda f: f is None }})
    revert_transaction: Optional[ActivityRevertTransactionOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RevertTransaction'), 'exclude': lambda f: f is None }})
    

