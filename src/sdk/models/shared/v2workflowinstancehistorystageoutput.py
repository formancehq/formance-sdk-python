"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import v2activitycreatetransactionoutput as shared_v2activitycreatetransactionoutput
from ..shared import v2activitydebitwalletoutput as shared_v2activitydebitwalletoutput
from ..shared import v2activitygetaccountoutput as shared_v2activitygetaccountoutput
from ..shared import v2activitygetpaymentoutput as shared_v2activitygetpaymentoutput
from ..shared import v2activitygetwalletoutput as shared_v2activitygetwalletoutput
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2WorkflowInstanceHistoryStageOutput:
    create_transaction: Optional[shared_v2activitycreatetransactionoutput.V2ActivityCreateTransactionOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreateTransaction'), 'exclude': lambda f: f is None }})
    debit_wallet: Optional[shared_v2activitydebitwalletoutput.V2ActivityDebitWalletOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DebitWallet'), 'exclude': lambda f: f is None }})
    get_account: Optional[shared_v2activitygetaccountoutput.V2ActivityGetAccountOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetAccount'), 'exclude': lambda f: f is None }})
    get_payment: Optional[shared_v2activitygetpaymentoutput.V2ActivityGetPaymentOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetPayment'), 'exclude': lambda f: f is None }})
    get_wallet: Optional[shared_v2activitygetwalletoutput.V2ActivityGetWalletOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GetWallet'), 'exclude': lambda f: f is None }})
    

