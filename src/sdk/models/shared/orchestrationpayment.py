"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .orchestrationconnector import OrchestrationConnector
from .orchestrationpaymentadjustment import OrchestrationPaymentAdjustment
from .orchestrationpaymentmetadata import OrchestrationPaymentMetadata
from .orchestrationpaymentstatus import OrchestrationPaymentStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import List, Optional


@dataclasses.dataclass
class OrchestrationPaymentRaw:
    pass


class OrchestrationPaymentScheme(str, Enum):
    VISA = 'visa'
    MASTERCARD = 'mastercard'
    AMEX = 'amex'
    DINERS = 'diners'
    DISCOVER = 'discover'
    JCB = 'jcb'
    UNIONPAY = 'unionpay'
    SEPA_DEBIT = 'sepa debit'
    SEPA_CREDIT = 'sepa credit'
    SEPA = 'sepa'
    APPLE_PAY = 'apple pay'
    GOOGLE_PAY = 'google pay'
    A2A = 'a2a'
    ACH_DEBIT = 'ach debit'
    ACH = 'ach'
    RTP = 'rtp'
    UNKNOWN = 'unknown'
    OTHER = 'other'


class OrchestrationPaymentType(str, Enum):
    PAY_IN = 'PAY-IN'
    PAYOUT = 'PAYOUT'
    TRANSFER = 'TRANSFER'
    OTHER = 'OTHER'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrchestrationPayment:
    adjustments: List[OrchestrationPaymentAdjustment] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjustments') }})
    asset: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('asset') }})
    connector_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectorID') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    destination_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationAccountID') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    initial_amount: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initialAmount') }})
    metadata: Optional[OrchestrationPaymentMetadata] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    raw: Optional[OrchestrationPaymentRaw] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    scheme: OrchestrationPaymentScheme = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme') }})
    source_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAccountID') }})
    status: OrchestrationPaymentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    type: OrchestrationPaymentType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    provider: Optional[OrchestrationConnector] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    

