"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .taskbankingcircle import TaskBankingCircle
from .taskcurrencycloud import TaskCurrencyCloud
from .taskdummypay import TaskDummyPay
from .taskmangopay import TaskMangoPay
from .taskmodulr import TaskModulr
from .taskmoneycorp import TaskMoneycorp
from .taskstripe import TaskStripe
from .taskwise import TaskWise
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TasksCursorCursor:
    data: List[Union[TaskStripe, TaskWise, TaskCurrencyCloud, TaskDummyPay, TaskModulr, TaskBankingCircle, TaskMangoPay, TaskMoneycorp]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasMore') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})
    next: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TasksCursor:
    cursor: TasksCursorCursor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor') }})
    

