"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils


class SchemasWalletsErrorResponseErrorCode(str, Enum):
    VALIDATION = 'VALIDATION'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    INSUFFICIENT_FUND = 'INSUFFICIENT_FUND'
    HOLD_CLOSED = 'HOLD_CLOSED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WalletsErrorResponse(Exception):
    error_code: SchemasWalletsErrorResponseErrorCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorCode') }})
    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage') }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
