# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: develop
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_wallets_holds_hold_id_confirm.post import ConfirmHold
from Formance.paths.api_wallets_wallets.post import CreateWallet
from Formance.paths.api_wallets_wallets_id_credit.post import CreditWallet
from Formance.paths.api_wallets_wallets_id_debit.post import DebitWallet
from Formance.paths.api_wallets_holds_hold_id.get import GetHold
from Formance.paths.api_wallets_holds.get import GetHolds
from Formance.paths.api_wallets_transactions.get import GetTransactions
from Formance.paths.api_wallets_wallets_id.get import GetWallet
from Formance.paths.api_wallets_wallets.get import ListWallets
from Formance.paths.api_wallets_wallets_id.patch import UpdateWallet
from Formance.paths.api_wallets_holds_hold_id_void.post import VoidHold


class WalletsApi(
    ConfirmHold,
    CreateWallet,
    CreditWallet,
    DebitWallet,
    GetHold,
    GetHolds,
    GetTransactions,
    GetWallet,
    ListWallets,
    UpdateWallet,
    VoidHold,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
