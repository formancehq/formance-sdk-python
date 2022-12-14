import typing_extensions

from Formance.paths import PathValues
from Formance.apis.paths.api_auth_clients import ApiAuthClients
from Formance.apis.paths.api_auth_clients_client_id import ApiAuthClientsClientId
from Formance.apis.paths.api_auth_clients_client_id_secrets import ApiAuthClientsClientIdSecrets
from Formance.apis.paths.api_auth_clients_client_id_secrets_secret_id import ApiAuthClientsClientIdSecretsSecretId
from Formance.apis.paths.api_auth_clients_client_id_scopes_scope_id import ApiAuthClientsClientIdScopesScopeId
from Formance.apis.paths.api_auth_scopes import ApiAuthScopes
from Formance.apis.paths.api_auth_scopes_scope_id import ApiAuthScopesScopeId
from Formance.apis.paths.api_auth_scopes_scope_id_transient_transient_scope_id import ApiAuthScopesScopeIdTransientTransientScopeId
from Formance.apis.paths.api_auth_users import ApiAuthUsers
from Formance.apis.paths.api_auth_users_user_id import ApiAuthUsersUserId
from Formance.apis.paths.api_ledger__info import ApiLedgerInfo
from Formance.apis.paths.api_ledger_ledger_accounts import ApiLedgerLedgerAccounts
from Formance.apis.paths.api_ledger_ledger_accounts_address import ApiLedgerLedgerAccountsAddress
from Formance.apis.paths.api_ledger_ledger_accounts_address_metadata import ApiLedgerLedgerAccountsAddressMetadata
from Formance.apis.paths.api_ledger_ledger_mapping import ApiLedgerLedgerMapping
from Formance.apis.paths.api_ledger_ledger_script import ApiLedgerLedgerScript
from Formance.apis.paths.api_ledger_ledger_stats import ApiLedgerLedgerStats
from Formance.apis.paths.api_ledger_ledger_transactions import ApiLedgerLedgerTransactions
from Formance.apis.paths.api_ledger_ledger_transactions_txid import ApiLedgerLedgerTransactionsTxid
from Formance.apis.paths.api_ledger_ledger_transactions_txid_metadata import ApiLedgerLedgerTransactionsTxidMetadata
from Formance.apis.paths.api_ledger_ledger_transactions_txid_revert import ApiLedgerLedgerTransactionsTxidRevert
from Formance.apis.paths.api_ledger_ledger_transactions_batch import ApiLedgerLedgerTransactionsBatch
from Formance.apis.paths.api_ledger_ledger_balances import ApiLedgerLedgerBalances
from Formance.apis.paths.api_ledger_ledger_aggregate_balances import ApiLedgerLedgerAggregateBalances
from Formance.apis.paths.api_payments_payments import ApiPaymentsPayments
from Formance.apis.paths.api_payments_payments_payment_id import ApiPaymentsPaymentsPaymentId
from Formance.apis.paths.api_payments_connectors import ApiPaymentsConnectors
from Formance.apis.paths.api_payments_connectors_configs import ApiPaymentsConnectorsConfigs
from Formance.apis.paths.api_payments_connectors_connector import ApiPaymentsConnectorsConnector
from Formance.apis.paths.api_payments_connectors_connector_config import ApiPaymentsConnectorsConnectorConfig
from Formance.apis.paths.api_payments_connectors_connector_reset import ApiPaymentsConnectorsConnectorReset
from Formance.apis.paths.api_payments_connectors_connector_tasks import ApiPaymentsConnectorsConnectorTasks
from Formance.apis.paths.api_payments_connectors_connector_tasks_task_id import ApiPaymentsConnectorsConnectorTasksTaskId
from Formance.apis.paths.api_payments_connectors_stripe_transfer import ApiPaymentsConnectorsStripeTransfer
from Formance.apis.paths.api_search__info import ApiSearchInfo
from Formance.apis.paths.api_search_ import ApiSearch
from Formance.apis.paths.api_webhooks_configs import ApiWebhooksConfigs
from Formance.apis.paths.api_webhooks_configs_id import ApiWebhooksConfigsId
from Formance.apis.paths.api_webhooks_configs_id_test import ApiWebhooksConfigsIdTest
from Formance.apis.paths.api_webhooks_configs_id_activate import ApiWebhooksConfigsIdActivate
from Formance.apis.paths.api_webhooks_configs_id_deactivate import ApiWebhooksConfigsIdDeactivate
from Formance.apis.paths.api_webhooks_configs_id_secret_change import ApiWebhooksConfigsIdSecretChange

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_AUTH_CLIENTS: ApiAuthClients,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID: ApiAuthClientsClientId,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID_SECRETS: ApiAuthClientsClientIdSecrets,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID_SECRETS_SECRET_ID: ApiAuthClientsClientIdSecretsSecretId,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID_SCOPES_SCOPE_ID: ApiAuthClientsClientIdScopesScopeId,
        PathValues.API_AUTH_SCOPES: ApiAuthScopes,
        PathValues.API_AUTH_SCOPES_SCOPE_ID: ApiAuthScopesScopeId,
        PathValues.API_AUTH_SCOPES_SCOPE_ID_TRANSIENT_TRANSIENT_SCOPE_ID: ApiAuthScopesScopeIdTransientTransientScopeId,
        PathValues.API_AUTH_USERS: ApiAuthUsers,
        PathValues.API_AUTH_USERS_USER_ID: ApiAuthUsersUserId,
        PathValues.API_LEDGER__INFO: ApiLedgerInfo,
        PathValues.API_LEDGER_LEDGER_ACCOUNTS: ApiLedgerLedgerAccounts,
        PathValues.API_LEDGER_LEDGER_ACCOUNTS_ADDRESS: ApiLedgerLedgerAccountsAddress,
        PathValues.API_LEDGER_LEDGER_ACCOUNTS_ADDRESS_METADATA: ApiLedgerLedgerAccountsAddressMetadata,
        PathValues.API_LEDGER_LEDGER_MAPPING: ApiLedgerLedgerMapping,
        PathValues.API_LEDGER_LEDGER_SCRIPT: ApiLedgerLedgerScript,
        PathValues.API_LEDGER_LEDGER_STATS: ApiLedgerLedgerStats,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS: ApiLedgerLedgerTransactions,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_TXID: ApiLedgerLedgerTransactionsTxid,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_TXID_METADATA: ApiLedgerLedgerTransactionsTxidMetadata,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_TXID_REVERT: ApiLedgerLedgerTransactionsTxidRevert,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_BATCH: ApiLedgerLedgerTransactionsBatch,
        PathValues.API_LEDGER_LEDGER_BALANCES: ApiLedgerLedgerBalances,
        PathValues.API_LEDGER_LEDGER_AGGREGATE_BALANCES: ApiLedgerLedgerAggregateBalances,
        PathValues.API_PAYMENTS_PAYMENTS: ApiPaymentsPayments,
        PathValues.API_PAYMENTS_PAYMENTS_PAYMENT_ID: ApiPaymentsPaymentsPaymentId,
        PathValues.API_PAYMENTS_CONNECTORS: ApiPaymentsConnectors,
        PathValues.API_PAYMENTS_CONNECTORS_CONFIGS: ApiPaymentsConnectorsConfigs,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR: ApiPaymentsConnectorsConnector,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_CONFIG: ApiPaymentsConnectorsConnectorConfig,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_RESET: ApiPaymentsConnectorsConnectorReset,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_TASKS: ApiPaymentsConnectorsConnectorTasks,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_TASKS_TASK_ID: ApiPaymentsConnectorsConnectorTasksTaskId,
        PathValues.API_PAYMENTS_CONNECTORS_STRIPE_TRANSFER: ApiPaymentsConnectorsStripeTransfer,
        PathValues.API_SEARCH__INFO: ApiSearchInfo,
        PathValues.API_SEARCH_: ApiSearch,
        PathValues.API_WEBHOOKS_CONFIGS: ApiWebhooksConfigs,
        PathValues.API_WEBHOOKS_CONFIGS_ID: ApiWebhooksConfigsId,
        PathValues.API_WEBHOOKS_CONFIGS_ID_TEST: ApiWebhooksConfigsIdTest,
        PathValues.API_WEBHOOKS_CONFIGS_ID_ACTIVATE: ApiWebhooksConfigsIdActivate,
        PathValues.API_WEBHOOKS_CONFIGS_ID_DEACTIVATE: ApiWebhooksConfigsIdDeactivate,
        PathValues.API_WEBHOOKS_CONFIGS_ID_SECRET_CHANGE: ApiWebhooksConfigsIdSecretChange,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_AUTH_CLIENTS: ApiAuthClients,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID: ApiAuthClientsClientId,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID_SECRETS: ApiAuthClientsClientIdSecrets,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID_SECRETS_SECRET_ID: ApiAuthClientsClientIdSecretsSecretId,
        PathValues.API_AUTH_CLIENTS_CLIENT_ID_SCOPES_SCOPE_ID: ApiAuthClientsClientIdScopesScopeId,
        PathValues.API_AUTH_SCOPES: ApiAuthScopes,
        PathValues.API_AUTH_SCOPES_SCOPE_ID: ApiAuthScopesScopeId,
        PathValues.API_AUTH_SCOPES_SCOPE_ID_TRANSIENT_TRANSIENT_SCOPE_ID: ApiAuthScopesScopeIdTransientTransientScopeId,
        PathValues.API_AUTH_USERS: ApiAuthUsers,
        PathValues.API_AUTH_USERS_USER_ID: ApiAuthUsersUserId,
        PathValues.API_LEDGER__INFO: ApiLedgerInfo,
        PathValues.API_LEDGER_LEDGER_ACCOUNTS: ApiLedgerLedgerAccounts,
        PathValues.API_LEDGER_LEDGER_ACCOUNTS_ADDRESS: ApiLedgerLedgerAccountsAddress,
        PathValues.API_LEDGER_LEDGER_ACCOUNTS_ADDRESS_METADATA: ApiLedgerLedgerAccountsAddressMetadata,
        PathValues.API_LEDGER_LEDGER_MAPPING: ApiLedgerLedgerMapping,
        PathValues.API_LEDGER_LEDGER_SCRIPT: ApiLedgerLedgerScript,
        PathValues.API_LEDGER_LEDGER_STATS: ApiLedgerLedgerStats,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS: ApiLedgerLedgerTransactions,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_TXID: ApiLedgerLedgerTransactionsTxid,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_TXID_METADATA: ApiLedgerLedgerTransactionsTxidMetadata,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_TXID_REVERT: ApiLedgerLedgerTransactionsTxidRevert,
        PathValues.API_LEDGER_LEDGER_TRANSACTIONS_BATCH: ApiLedgerLedgerTransactionsBatch,
        PathValues.API_LEDGER_LEDGER_BALANCES: ApiLedgerLedgerBalances,
        PathValues.API_LEDGER_LEDGER_AGGREGATE_BALANCES: ApiLedgerLedgerAggregateBalances,
        PathValues.API_PAYMENTS_PAYMENTS: ApiPaymentsPayments,
        PathValues.API_PAYMENTS_PAYMENTS_PAYMENT_ID: ApiPaymentsPaymentsPaymentId,
        PathValues.API_PAYMENTS_CONNECTORS: ApiPaymentsConnectors,
        PathValues.API_PAYMENTS_CONNECTORS_CONFIGS: ApiPaymentsConnectorsConfigs,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR: ApiPaymentsConnectorsConnector,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_CONFIG: ApiPaymentsConnectorsConnectorConfig,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_RESET: ApiPaymentsConnectorsConnectorReset,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_TASKS: ApiPaymentsConnectorsConnectorTasks,
        PathValues.API_PAYMENTS_CONNECTORS_CONNECTOR_TASKS_TASK_ID: ApiPaymentsConnectorsConnectorTasksTaskId,
        PathValues.API_PAYMENTS_CONNECTORS_STRIPE_TRANSFER: ApiPaymentsConnectorsStripeTransfer,
        PathValues.API_SEARCH__INFO: ApiSearchInfo,
        PathValues.API_SEARCH_: ApiSearch,
        PathValues.API_WEBHOOKS_CONFIGS: ApiWebhooksConfigs,
        PathValues.API_WEBHOOKS_CONFIGS_ID: ApiWebhooksConfigsId,
        PathValues.API_WEBHOOKS_CONFIGS_ID_TEST: ApiWebhooksConfigsIdTest,
        PathValues.API_WEBHOOKS_CONFIGS_ID_ACTIVATE: ApiWebhooksConfigsIdActivate,
        PathValues.API_WEBHOOKS_CONFIGS_ID_DEACTIVATE: ApiWebhooksConfigsIdDeactivate,
        PathValues.API_WEBHOOKS_CONFIGS_ID_SECRET_CHANGE: ApiWebhooksConfigsIdSecretChange,
    }
)
