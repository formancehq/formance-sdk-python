# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0-rc.5
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_ledger_ledger_balances.get import GetBalances
from Formance.paths.api_ledger_ledger_aggregate_balances.get import GetBalancesAggregated


class BalancesApi(
    GetBalances,
    GetBalancesAggregated,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
