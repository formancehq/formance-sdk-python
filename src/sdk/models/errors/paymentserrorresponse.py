"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.shared import paymentserrorsenum as shared_paymentserrorsenum
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PaymentsErrorResponse(Exception):
    r"""Error"""
    error_code: shared_paymentserrorsenum.PaymentsErrorsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorCode') }})
    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage') }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
