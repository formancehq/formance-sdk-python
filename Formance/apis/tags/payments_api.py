# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_payments_connectors.get import GetAllConnectors
from Formance.paths.api_payments_connectors_configs.get import GetAllConnectorsConfigs
from Formance.paths.api_payments_connectors_connector_tasks_task_id.get import GetConnectorTask
from Formance.paths.api_payments_payments_payment_id.get import GetPayment
from Formance.paths.api_payments_connectors_connector.post import InstallConnector
from Formance.paths.api_payments_connectors_connector_tasks.get import ListConnectorTasks
from Formance.paths.api_payments_payments.get import ListPayments
from Formance.paths.api_payments_connectors_connector_config.get import ReadConnectorConfig
from Formance.paths.api_payments_connectors_connector_reset.post import ResetConnector
from Formance.paths.api_payments_connectors_connector.delete import UninstallConnector


class PaymentsApi(
    GetAllConnectors,
    GetAllConnectorsConfigs,
    GetConnectorTask,
    GetPayment,
    InstallConnector,
    ListConnectorTasks,
    ListPayments,
    ReadConnectorConfig,
    ResetConnector,
    UninstallConnector,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
