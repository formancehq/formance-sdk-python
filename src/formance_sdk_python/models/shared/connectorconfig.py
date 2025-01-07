"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .adyenconfig import AdyenConfig, AdyenConfigTypedDict
from .atlarconfig import AtlarConfig, AtlarConfigTypedDict
from .bankingcircleconfig import BankingCircleConfig, BankingCircleConfigTypedDict
from .currencycloudconfig import CurrencyCloudConfig, CurrencyCloudConfigTypedDict
from .dummypayconfig import DummyPayConfig, DummyPayConfigTypedDict
from .genericconfig import GenericConfig, GenericConfigTypedDict
from .mangopayconfig import MangoPayConfig, MangoPayConfigTypedDict
from .modulrconfig import ModulrConfig, ModulrConfigTypedDict
from .moneycorpconfig import MoneycorpConfig, MoneycorpConfigTypedDict
from .stripeconfig import StripeConfig, StripeConfigTypedDict
from .wiseconfig import WiseConfig, WiseConfigTypedDict
from typing import Union
from typing_extensions import TypeAliasType


ConnectorConfigTypedDict = TypeAliasType(
    "ConnectorConfigTypedDict",
    Union[
        WiseConfigTypedDict,
        StripeConfigTypedDict,
        GenericConfigTypedDict,
        ModulrConfigTypedDict,
        CurrencyCloudConfigTypedDict,
        MangoPayConfigTypedDict,
        MoneycorpConfigTypedDict,
        AdyenConfigTypedDict,
        DummyPayConfigTypedDict,
        AtlarConfigTypedDict,
        BankingCircleConfigTypedDict,
    ],
)


ConnectorConfig = TypeAliasType(
    "ConnectorConfig",
    Union[
        WiseConfig,
        StripeConfig,
        GenericConfig,
        ModulrConfig,
        CurrencyCloudConfig,
        MangoPayConfig,
        MoneycorpConfig,
        AdyenConfig,
        DummyPayConfig,
        AtlarConfig,
        BankingCircleConfig,
    ],
)