"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .taskbankingcircle import TaskBankingCircle, TaskBankingCircleTypedDict
from .taskcurrencycloud import TaskCurrencyCloud, TaskCurrencyCloudTypedDict
from .taskdummypay import TaskDummyPay, TaskDummyPayTypedDict
from .taskmangopay import TaskMangoPay, TaskMangoPayTypedDict
from .taskmodulr import TaskModulr, TaskModulrTypedDict
from .taskmoneycorp import TaskMoneycorp, TaskMoneycorpTypedDict
from .taskstripe import TaskStripe, TaskStripeTypedDict
from .taskwise import TaskWise, TaskWiseTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


TasksCursorDataTypedDict = TypeAliasType(
    "TasksCursorDataTypedDict",
    Union[
        TaskStripeTypedDict,
        TaskWiseTypedDict,
        TaskCurrencyCloudTypedDict,
        TaskDummyPayTypedDict,
        TaskModulrTypedDict,
        TaskBankingCircleTypedDict,
        TaskMangoPayTypedDict,
        TaskMoneycorpTypedDict,
    ],
)


TasksCursorData = TypeAliasType(
    "TasksCursorData",
    Union[
        TaskStripe,
        TaskWise,
        TaskCurrencyCloud,
        TaskDummyPay,
        TaskModulr,
        TaskBankingCircle,
        TaskMangoPay,
        TaskMoneycorp,
    ],
)


class TasksCursorCursorTypedDict(TypedDict):
    data: List[TasksCursorDataTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class TasksCursorCursor(BaseModel):
    data: List[TasksCursorData]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class TasksCursorTypedDict(TypedDict):
    r"""OK"""

    cursor: TasksCursorCursorTypedDict


class TasksCursor(BaseModel):
    r"""OK"""

    cursor: TasksCursorCursor
