# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from Formance.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_AUTH_CLIENTS = "/api/auth/clients"
    API_AUTH_CLIENTS_CLIENT_ID = "/api/auth/clients/{clientId}"
    API_AUTH_CLIENTS_CLIENT_ID_SECRETS = "/api/auth/clients/{clientId}/secrets"
    API_AUTH_CLIENTS_CLIENT_ID_SECRETS_SECRET_ID = "/api/auth/clients/{clientId}/secrets/{secretId}"
    API_AUTH_CLIENTS_CLIENT_ID_SCOPES_SCOPE_ID = "/api/auth/clients/{clientId}/scopes/{scopeId}"
    API_AUTH_SCOPES = "/api/auth/scopes"
    API_AUTH_SCOPES_SCOPE_ID = "/api/auth/scopes/{scopeId}"
    API_AUTH_SCOPES_SCOPE_ID_TRANSIENT_TRANSIENT_SCOPE_ID = "/api/auth/scopes/{scopeId}/transient/{transientScopeId}"
    API_AUTH_USERS = "/api/auth/users"
    API_AUTH_USERS_USER_ID = "/api/auth/users/{userId}"
    API_LEDGER__INFO = "/api/ledger/_info"
    API_LEDGER_LEDGER_ACCOUNTS = "/api/ledger/{ledger}/accounts"
    API_LEDGER_LEDGER_ACCOUNTS_ADDRESS = "/api/ledger/{ledger}/accounts/{address}"
    API_LEDGER_LEDGER_ACCOUNTS_ADDRESS_METADATA = "/api/ledger/{ledger}/accounts/{address}/metadata"
    API_LEDGER_LEDGER_MAPPING = "/api/ledger/{ledger}/mapping"
    API_LEDGER_LEDGER_SCRIPT = "/api/ledger/{ledger}/script"
    API_LEDGER_LEDGER_STATS = "/api/ledger/{ledger}/stats"
    API_LEDGER_LEDGER_TRANSACTIONS = "/api/ledger/{ledger}/transactions"
    API_LEDGER_LEDGER_TRANSACTIONS_TXID = "/api/ledger/{ledger}/transactions/{txid}"
    API_LEDGER_LEDGER_TRANSACTIONS_TXID_METADATA = "/api/ledger/{ledger}/transactions/{txid}/metadata"
    API_LEDGER_LEDGER_TRANSACTIONS_TXID_REVERT = "/api/ledger/{ledger}/transactions/{txid}/revert"
    API_LEDGER_LEDGER_TRANSACTIONS_BATCH = "/api/ledger/{ledger}/transactions/batch"
    API_LEDGER_LEDGER_BALANCES = "/api/ledger/{ledger}/balances"
    API_LEDGER_LEDGER_AGGREGATE_BALANCES = "/api/ledger/{ledger}/aggregate/balances"
    API_PAYMENTS_PAYMENTS = "/api/payments/payments"
    API_PAYMENTS_PAYMENTS_PAYMENT_ID = "/api/payments/payments/{paymentId}"
    API_PAYMENTS_CONNECTORS = "/api/payments/connectors"
    API_PAYMENTS_CONNECTORS_CONFIGS = "/api/payments/connectors/configs"
    API_PAYMENTS_CONNECTORS_CONNECTOR = "/api/payments/connectors/{connector}"
    API_PAYMENTS_CONNECTORS_CONNECTOR_CONFIG = "/api/payments/connectors/{connector}/config"
    API_PAYMENTS_CONNECTORS_CONNECTOR_RESET = "/api/payments/connectors/{connector}/reset"
    API_PAYMENTS_CONNECTORS_CONNECTOR_TASKS = "/api/payments/connectors/{connector}/tasks"
    API_PAYMENTS_CONNECTORS_CONNECTOR_TASKS_TASK_ID = "/api/payments/connectors/{connector}/tasks/{taskId}"
    API_PAYMENTS_CONNECTORS_STRIPE_TRANSFER = "/api/payments/connectors/stripe/transfer"
    API_SEARCH__INFO = "/api/search/_info"
    API_SEARCH_ = "/api/search/"
    API_WEBHOOKS_CONFIGS = "/api/webhooks/configs"
    API_WEBHOOKS_CONFIGS_ID = "/api/webhooks/configs/{id}"
    API_WEBHOOKS_CONFIGS_ID_TEST = "/api/webhooks/configs/{id}/test"
    API_WEBHOOKS_CONFIGS_ID_ACTIVATE = "/api/webhooks/configs/{id}/activate"
    API_WEBHOOKS_CONFIGS_ID_DEACTIVATE = "/api/webhooks/configs/{id}/deactivate"
    API_WEBHOOKS_CONFIGS_ID_SECRET_CHANGE = "/api/webhooks/configs/{id}/secret/change"
