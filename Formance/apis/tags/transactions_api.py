# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: develop
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_ledger_ledger_transactions_txid_metadata.post import AddMetadataOnTransaction
from Formance.paths.api_ledger_ledger_transactions.head import CountTransactions
from Formance.paths.api_ledger_ledger_transactions.post import CreateTransaction
from Formance.paths.api_ledger_ledger_transactions_batch.post import CreateTransactions
from Formance.paths.api_ledger_ledger_transactions_txid.get import GetTransaction
from Formance.paths.api_ledger_ledger_transactions.get import ListTransactions
from Formance.paths.api_ledger_ledger_transactions_txid_revert.post import RevertTransaction


class TransactionsApi(
    AddMetadataOnTransaction,
    CountTransactions,
    CreateTransaction,
    CreateTransactions,
    GetTransaction,
    ListTransactions,
    RevertTransaction,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
