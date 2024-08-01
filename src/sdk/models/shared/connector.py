"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class Connector(str, Enum):
    STRIPE = 'STRIPE'
    DUMMY_PAY = 'DUMMY-PAY'
    WISE = 'WISE'
    MODULR = 'MODULR'
    CURRENCY_CLOUD = 'CURRENCY-CLOUD'
    BANKING_CIRCLE = 'BANKING-CIRCLE'
    MANGOPAY = 'MANGOPAY'
    MONEYCORP = 'MONEYCORP'
    ATLAR = 'ATLAR'
    ADYEN = 'ADYEN'
    GENERIC = 'GENERIC'
