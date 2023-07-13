# formance-sdk-python

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install formance-sdk-python
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)


res = s.get_versions()

if res.get_versions_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [SDK](docs/sdks/sdk/README.md)

* [get_versions](docs/sdks/sdk/README.md#get_versions) - Show stack version information

### [auth](docs/sdks/auth/README.md)

* [add_scope_to_client](docs/sdks/auth/README.md#add_scope_to_client) - Add scope to client
* [add_transient_scope](docs/sdks/auth/README.md#add_transient_scope) - Add a transient scope to a scope
* [create_client](docs/sdks/auth/README.md#create_client) - Create client
* [create_scope](docs/sdks/auth/README.md#create_scope) - Create scope
* [create_secret](docs/sdks/auth/README.md#create_secret) - Add a secret to a client
* [delete_client](docs/sdks/auth/README.md#delete_client) - Delete client
* [delete_scope](docs/sdks/auth/README.md#delete_scope) - Delete scope
* [delete_scope_from_client](docs/sdks/auth/README.md#delete_scope_from_client) - Delete scope from client
* [delete_secret](docs/sdks/auth/README.md#delete_secret) - Delete a secret from a client
* [delete_transient_scope](docs/sdks/auth/README.md#delete_transient_scope) - Delete a transient scope from a scope
* [get_server_info](docs/sdks/auth/README.md#get_server_info) - Get server info
* [list_clients](docs/sdks/auth/README.md#list_clients) - List clients
* [list_scopes](docs/sdks/auth/README.md#list_scopes) - List scopes
* [list_users](docs/sdks/auth/README.md#list_users) - List users
* [read_client](docs/sdks/auth/README.md#read_client) - Read client
* [read_scope](docs/sdks/auth/README.md#read_scope) - Read scope
* [read_user](docs/sdks/auth/README.md#read_user) - Read user
* [update_client](docs/sdks/auth/README.md#update_client) - Update client
* [update_scope](docs/sdks/auth/README.md#update_scope) - Update scope

### [flows](docs/sdks/flows/README.md)

* [flowsget_server_info](docs/sdks/flows/README.md#flowsget_server_info) - Get server info
* [cancel_event](docs/sdks/flows/README.md#cancel_event) - Cancel a running workflow
* [create_workflow](docs/sdks/flows/README.md#create_workflow) - Create workflow
* [get_instance](docs/sdks/flows/README.md#get_instance) - Get a workflow instance by id
* [get_instance_history](docs/sdks/flows/README.md#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](docs/sdks/flows/README.md#get_instance_stage_history) - Get a workflow instance stage history
* [get_workflow](docs/sdks/flows/README.md#get_workflow) - Get a flow by id
* [list_instances](docs/sdks/flows/README.md#list_instances) - List instances of a workflow
* [list_workflows](docs/sdks/flows/README.md#list_workflows) - List registered workflows
* [run_workflow](docs/sdks/flows/README.md#run_workflow) - Run workflow
* [send_event](docs/sdks/flows/README.md#send_event) - Send an event to a running workflow

### [ledger](docs/sdks/ledger/README.md)

* [create_transactions](docs/sdks/ledger/README.md#create_transactions) - Create a new batch of transactions to a ledger
* [add_metadata_on_transaction](docs/sdks/ledger/README.md#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](docs/sdks/ledger/README.md#add_metadata_to_account) - Add metadata to an account
* [count_accounts](docs/sdks/ledger/README.md#count_accounts) - Count the accounts from a ledger
* [count_transactions](docs/sdks/ledger/README.md#count_transactions) - Count the transactions from a ledger
* [create_transaction](docs/sdks/ledger/README.md#create_transaction) - Create a new transaction to a ledger
* [get_account](docs/sdks/ledger/README.md#get_account) - Get account by its address
* [get_balances](docs/sdks/ledger/README.md#get_balances) - Get the balances from a ledger's account
* [get_balances_aggregated](docs/sdks/ledger/README.md#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](docs/sdks/ledger/README.md#get_info) - Show server information
* [get_ledger_info](docs/sdks/ledger/README.md#get_ledger_info) - Get information about a ledger
* [get_mapping](docs/sdks/ledger/README.md#get_mapping) - Get the mapping of a ledger
* [get_transaction](docs/sdks/ledger/README.md#get_transaction) - Get transaction from a ledger by its ID
* [list_accounts](docs/sdks/ledger/README.md#list_accounts) - List accounts from a ledger
* [list_logs](docs/sdks/ledger/README.md#list_logs) - List the logs from a ledger
* [list_transactions](docs/sdks/ledger/README.md#list_transactions) - List transactions from a ledger
* [read_stats](docs/sdks/ledger/README.md#read_stats) - Get statistics from a ledger
* [revert_transaction](docs/sdks/ledger/README.md#revert_transaction) - Revert a ledger transaction by its ID
* [~~run_script~~](docs/sdks/ledger/README.md#run_script) - Execute a Numscript :warning: **Deprecated**
* [update_mapping](docs/sdks/ledger/README.md#update_mapping) - Update the mapping of a ledger

### [payments](docs/sdks/payments/README.md)

* [connectors_stripe_transfer](docs/sdks/payments/README.md#connectors_stripe_transfer) - Transfer funds between Stripe accounts
* [connectors_transfer](docs/sdks/payments/README.md#connectors_transfer) - Transfer funds between Connector accounts
* [get_connector_task](docs/sdks/payments/README.md#get_connector_task) - Read a specific task of the connector
* [get_payment](docs/sdks/payments/README.md#get_payment) - Get a payment
* [install_connector](docs/sdks/payments/README.md#install_connector) - Install a connector
* [list_all_connectors](docs/sdks/payments/README.md#list_all_connectors) - List all installed connectors
* [list_configs_available_connectors](docs/sdks/payments/README.md#list_configs_available_connectors) - List the configs of each available connector
* [list_connector_tasks](docs/sdks/payments/README.md#list_connector_tasks) - List tasks from a connector
* [list_connectors_transfers](docs/sdks/payments/README.md#list_connectors_transfers) - List transfers and their statuses
* [list_payments](docs/sdks/payments/README.md#list_payments) - List payments
* [paymentsget_server_info](docs/sdks/payments/README.md#paymentsget_server_info) - Get server info
* [paymentslist_accounts](docs/sdks/payments/README.md#paymentslist_accounts) - List accounts
* [read_connector_config](docs/sdks/payments/README.md#read_connector_config) - Read the config of a connector
* [reset_connector](docs/sdks/payments/README.md#reset_connector) - Reset a connector
* [uninstall_connector](docs/sdks/payments/README.md#uninstall_connector) - Uninstall a connector
* [update_metadata](docs/sdks/payments/README.md#update_metadata) - Update metadata

### [search](docs/sdks/search/README.md)

* [search](docs/sdks/search/README.md#search) - Search
* [searchget_server_info](docs/sdks/search/README.md#searchget_server_info) - Get server info

### [wallets](docs/sdks/wallets/README.md)

* [confirm_hold](docs/sdks/wallets/README.md#confirm_hold) - Confirm a hold
* [create_balance](docs/sdks/wallets/README.md#create_balance) - Create a balance
* [create_wallet](docs/sdks/wallets/README.md#create_wallet) - Create a new wallet
* [credit_wallet](docs/sdks/wallets/README.md#credit_wallet) - Credit a wallet
* [debit_wallet](docs/sdks/wallets/README.md#debit_wallet) - Debit a wallet
* [get_balance](docs/sdks/wallets/README.md#get_balance) - Get detailed balance
* [get_hold](docs/sdks/wallets/README.md#get_hold) - Get a hold
* [get_holds](docs/sdks/wallets/README.md#get_holds) - Get all holds for a wallet
* [get_transactions](docs/sdks/wallets/README.md#get_transactions)
* [get_wallet](docs/sdks/wallets/README.md#get_wallet) - Get a wallet
* [get_wallet_summary](docs/sdks/wallets/README.md#get_wallet_summary) - Get wallet summary
* [list_balances](docs/sdks/wallets/README.md#list_balances) - List balances of a wallet
* [list_wallets](docs/sdks/wallets/README.md#list_wallets) - List all wallets
* [update_wallet](docs/sdks/wallets/README.md#update_wallet) - Update a wallet
* [void_hold](docs/sdks/wallets/README.md#void_hold) - Cancel a hold
* [walletsget_server_info](docs/sdks/wallets/README.md#walletsget_server_info) - Get server info

### [webhooks](docs/sdks/webhooks/README.md)

* [activate_config](docs/sdks/webhooks/README.md#activate_config) - Activate one config
* [change_config_secret](docs/sdks/webhooks/README.md#change_config_secret) - Change the signing secret of a config
* [deactivate_config](docs/sdks/webhooks/README.md#deactivate_config) - Deactivate one config
* [delete_config](docs/sdks/webhooks/README.md#delete_config) - Delete one config
* [get_many_configs](docs/sdks/webhooks/README.md#get_many_configs) - Get many configs
* [insert_config](docs/sdks/webhooks/README.md#insert_config) - Insert a new config
* [test_config](docs/sdks/webhooks/README.md#test_config) - Test one config
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
