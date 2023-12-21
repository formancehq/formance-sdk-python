"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import v2bulkelementresult as shared_v2bulkelementresult
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2BulkResponse:
    data: List[Union[shared_v2bulkelementresult.V2BulkElementResultV2BulkElementResultCreateTransaction, shared_v2bulkelementresult.V2BulkElementResultV2BulkElementResultAddMetadata, shared_v2bulkelementresult.V2BulkElementResultV2BulkElementResultRevertTransaction, shared_v2bulkelementresult.V2BulkElementResultV2BulkElementResultDeleteMetadata, shared_v2bulkelementresult.V2BulkElementResultV2BulkElementResultError]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

