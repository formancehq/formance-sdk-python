"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import webhookserrorsenum as shared_webhookserrorsenum
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebhooksErrorResponse:
    error_code: shared_webhookserrorsenum.WebhooksErrorsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorCode') }})
    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage') }})
    details: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    

