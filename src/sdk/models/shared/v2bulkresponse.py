"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .v2bulkelementresult import Schemas, V2BulkElementResultCreateTransactionSchemas, V2BulkElementResultDeleteMetadataSchemas, V2BulkElementResultErrorSchemas, V2BulkElementResultRevertTransactionSchemas
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class V2BulkResponse:
    data: List[Union[V2BulkElementResultCreateTransactionSchemas, Schemas, V2BulkElementResultRevertTransactionSchemas, V2BulkElementResultDeleteMetadataSchemas, V2BulkElementResultErrorSchemas]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

