"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3adyenconfig import V3AdyenConfig, V3AdyenConfigTypedDict
from .v3atlarconfig import V3AtlarConfig, V3AtlarConfigTypedDict
from .v3bankingcircleconfig import V3BankingcircleConfig, V3BankingcircleConfigTypedDict
from .v3currencycloudconfig import V3CurrencycloudConfig, V3CurrencycloudConfigTypedDict
from .v3dummypayconfig import V3DummypayConfig, V3DummypayConfigTypedDict
from .v3genericconfig import V3GenericConfig, V3GenericConfigTypedDict
from .v3mangopayconfig import V3MangopayConfig, V3MangopayConfigTypedDict
from .v3modulrconfig import V3ModulrConfig, V3ModulrConfigTypedDict
from .v3moneycorpconfig import V3MoneycorpConfig, V3MoneycorpConfigTypedDict
from .v3stripeconfig import V3StripeConfig, V3StripeConfigTypedDict
from .v3wiseconfig import V3WiseConfig, V3WiseConfigTypedDict
from typing import Union
from typing_extensions import TypeAliasType


V3InstallConnectorRequestTypedDict = TypeAliasType(
    "V3InstallConnectorRequestTypedDict",
    Union[
        V3DummypayConfigTypedDict,
        V3StripeConfigTypedDict,
        V3GenericConfigTypedDict,
        V3WiseConfigTypedDict,
        V3AtlarConfigTypedDict,
        V3CurrencycloudConfigTypedDict,
        V3MangopayConfigTypedDict,
        V3ModulrConfigTypedDict,
        V3MoneycorpConfigTypedDict,
        V3AdyenConfigTypedDict,
        V3BankingcircleConfigTypedDict,
    ],
)


V3InstallConnectorRequest = TypeAliasType(
    "V3InstallConnectorRequest",
    Union[
        V3DummypayConfig,
        V3StripeConfig,
        V3GenericConfig,
        V3WiseConfig,
        V3AtlarConfig,
        V3CurrencycloudConfig,
        V3MangopayConfig,
        V3ModulrConfig,
        V3MoneycorpConfig,
        V3AdyenConfig,
        V3BankingcircleConfig,
    ],
)
