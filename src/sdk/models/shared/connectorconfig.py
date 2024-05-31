"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .adyenconfig import AdyenConfig
from .atlarconfig import AtlarConfig
from .bankingcircleconfig import BankingCircleConfig
from .currencycloudconfig import CurrencyCloudConfig
from .dummypayconfig import DummyPayConfig
from .genericconfig import GenericConfig
from .mangopayconfig import MangoPayConfig
from .modulrconfig import ModulrConfig
from .moneycorpconfig import MoneycorpConfig
from .stripeconfig import StripeConfig
from .wiseconfig import WiseConfig
from typing import Union

ConnectorConfig = Union[StripeConfig, DummyPayConfig, WiseConfig, ModulrConfig, CurrencyCloudConfig, BankingCircleConfig, MangoPayConfig, MoneycorpConfig, AtlarConfig, AdyenConfig, GenericConfig]
