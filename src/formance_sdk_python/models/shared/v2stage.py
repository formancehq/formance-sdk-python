"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2stagedelay import V2StageDelay, V2StageDelayTypedDict
from .v2stagesend import V2StageSend, V2StageSendTypedDict
from .v2stagewaitevent import V2StageWaitEvent, V2StageWaitEventTypedDict
from .v2update import V2Update, V2UpdateTypedDict
from typing import Union
from typing_extensions import TypeAliasType


V2StageTypedDict = TypeAliasType(
    "V2StageTypedDict",
    Union[
        V2StageWaitEventTypedDict,
        V2UpdateTypedDict,
        V2StageDelayTypedDict,
        V2StageSendTypedDict,
    ],
)


V2Stage = TypeAliasType(
    "V2Stage", Union[V2StageWaitEvent, V2Update, V2StageDelay, V2StageSend]
)
