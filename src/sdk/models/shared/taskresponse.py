"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

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
from typing import Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskResponse:
    data: TaskResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    


TaskResponseData = Union[TaskStripe, TaskWise, TaskCurrencyCloud, TaskDummyPay, TaskModulr, TaskBankingCircle, TaskMangoPay, TaskMoneycorp]
