# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v0.2.8
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_ledger_ledger_accounts_address_metadata.post import AddMetadataToAccount
from Formance.paths.api_ledger_ledger_accounts.head import CountAccounts
from Formance.paths.api_ledger_ledger_accounts_address.get import GetAccount
from Formance.paths.api_ledger_ledger_accounts.get import ListAccounts


class AccountsApi(
    AddMetadataToAccount,
    CountAccounts,
    GetAccount,
    ListAccounts,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
