# formance-sdk-python

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk


s = sdk.SDK()


res = s.sdk.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [SDK](docs/sdks/sdk/README.md)

* [get_versions](docs/sdks/sdk/README.md#get_versions) - Show stack version information
* [get_api_auth_well_known_openid_configuration](docs/sdks/sdk/README.md#get_api_auth_well_known_openid_configuration)

### [auth](docs/sdks/auth/README.md)

* [create_client](docs/sdks/auth/README.md#create_client) - Create client
* [create_secret](docs/sdks/auth/README.md#create_secret) - Add a secret to a client
* [delete_client](docs/sdks/auth/README.md#delete_client) - Delete client
* [delete_secret](docs/sdks/auth/README.md#delete_secret) - Delete a secret from a client
* [get_server_info](docs/sdks/auth/README.md#get_server_info) - Get server info
* [list_clients](docs/sdks/auth/README.md#list_clients) - List clients
* [list_users](docs/sdks/auth/README.md#list_users) - List users
* [read_client](docs/sdks/auth/README.md#read_client) - Read client
* [read_user](docs/sdks/auth/README.md#read_user) - Read user
* [update_client](docs/sdks/auth/README.md#update_client) - Update client

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
* [v2_add_metadata_on_transaction](docs/sdks/ledger/README.md#v2_add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [v2_add_metadata_to_account](docs/sdks/ledger/README.md#v2_add_metadata_to_account) - Add metadata to an account
* [v2_count_accounts](docs/sdks/ledger/README.md#v2_count_accounts) - Count the accounts from a ledger
* [v2_count_transactions](docs/sdks/ledger/README.md#v2_count_transactions) - Count the transactions from a ledger
* [v2_create_bulk](docs/sdks/ledger/README.md#v2_create_bulk) - Bulk request
* [v2_create_ledger](docs/sdks/ledger/README.md#v2_create_ledger) - Create a ledger
* [v2_create_transaction](docs/sdks/ledger/README.md#v2_create_transaction) - Create a new transaction to a ledger
* [v2_delete_account_metadata](docs/sdks/ledger/README.md#v2_delete_account_metadata) - Delete metadata by key
* [v2_delete_transaction_metadata](docs/sdks/ledger/README.md#v2_delete_transaction_metadata) - Delete metadata by key
* [v2_get_account](docs/sdks/ledger/README.md#v2_get_account) - Get account by its address
* [v2_get_balances_aggregated](docs/sdks/ledger/README.md#v2_get_balances_aggregated) - Get the aggregated balances from selected accounts
* [v2_get_info](docs/sdks/ledger/README.md#v2_get_info) - Show server information
* [v2_get_ledger](docs/sdks/ledger/README.md#v2_get_ledger) - Get a ledger
* [v2_get_ledger_info](docs/sdks/ledger/README.md#v2_get_ledger_info) - Get information about a ledger
* [v2_get_transaction](docs/sdks/ledger/README.md#v2_get_transaction) - Get transaction from a ledger by its ID
* [v2_list_accounts](docs/sdks/ledger/README.md#v2_list_accounts) - List accounts from a ledger
* [v2_list_ledgers](docs/sdks/ledger/README.md#v2_list_ledgers) - List ledgers
* [v2_list_logs](docs/sdks/ledger/README.md#v2_list_logs) - List the logs from a ledger
* [v2_list_transactions](docs/sdks/ledger/README.md#v2_list_transactions) - List transactions from a ledger
* [v2_read_stats](docs/sdks/ledger/README.md#v2_read_stats) - Get statistics from a ledger
* [v2_revert_transaction](docs/sdks/ledger/README.md#v2_revert_transaction) - Revert a ledger transaction by its ID

### [orchestration](docs/sdks/orchestration/README.md)

* [cancel_event](docs/sdks/orchestration/README.md#cancel_event) - Cancel a running workflow
* [create_trigger](docs/sdks/orchestration/README.md#create_trigger) - Create trigger
* [create_workflow](docs/sdks/orchestration/README.md#create_workflow) - Create workflow
* [delete_trigger](docs/sdks/orchestration/README.md#delete_trigger) - Delete trigger
* [delete_workflow](docs/sdks/orchestration/README.md#delete_workflow) - Delete a flow by id
* [get_instance](docs/sdks/orchestration/README.md#get_instance) - Get a workflow instance by id
* [get_instance_history](docs/sdks/orchestration/README.md#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](docs/sdks/orchestration/README.md#get_instance_stage_history) - Get a workflow instance stage history
* [get_workflow](docs/sdks/orchestration/README.md#get_workflow) - Get a flow by id
* [list_instances](docs/sdks/orchestration/README.md#list_instances) - List instances of a workflow
* [list_triggers](docs/sdks/orchestration/README.md#list_triggers) - List triggers
* [list_triggers_occurrences](docs/sdks/orchestration/README.md#list_triggers_occurrences) - List triggers occurrences
* [list_workflows](docs/sdks/orchestration/README.md#list_workflows) - List registered workflows
* [orchestrationget_server_info](docs/sdks/orchestration/README.md#orchestrationget_server_info) - Get server info
* [read_trigger](docs/sdks/orchestration/README.md#read_trigger) - Read trigger
* [run_workflow](docs/sdks/orchestration/README.md#run_workflow) - Run workflow
* [send_event](docs/sdks/orchestration/README.md#send_event) - Send an event to a running workflow
* [v2_cancel_event](docs/sdks/orchestration/README.md#v2_cancel_event) - Cancel a running workflow
* [v2_create_trigger](docs/sdks/orchestration/README.md#v2_create_trigger) - Create trigger
* [v2_create_workflow](docs/sdks/orchestration/README.md#v2_create_workflow) - Create workflow
* [v2_delete_trigger](docs/sdks/orchestration/README.md#v2_delete_trigger) - Delete trigger
* [v2_delete_workflow](docs/sdks/orchestration/README.md#v2_delete_workflow) - Delete a flow by id
* [v2_get_instance](docs/sdks/orchestration/README.md#v2_get_instance) - Get a workflow instance by id
* [v2_get_instance_history](docs/sdks/orchestration/README.md#v2_get_instance_history) - Get a workflow instance history by id
* [v2_get_instance_stage_history](docs/sdks/orchestration/README.md#v2_get_instance_stage_history) - Get a workflow instance stage history
* [v2_get_server_info](docs/sdks/orchestration/README.md#v2_get_server_info) - Get server info
* [v2_get_workflow](docs/sdks/orchestration/README.md#v2_get_workflow) - Get a flow by id
* [v2_list_instances](docs/sdks/orchestration/README.md#v2_list_instances) - List instances of a workflow
* [v2_list_triggers](docs/sdks/orchestration/README.md#v2_list_triggers) - List triggers
* [v2_list_triggers_occurrences](docs/sdks/orchestration/README.md#v2_list_triggers_occurrences) - List triggers occurrences
* [v2_list_workflows](docs/sdks/orchestration/README.md#v2_list_workflows) - List registered workflows
* [v2_read_trigger](docs/sdks/orchestration/README.md#v2_read_trigger) - Read trigger
* [v2_run_workflow](docs/sdks/orchestration/README.md#v2_run_workflow) - Run workflow
* [v2_send_event](docs/sdks/orchestration/README.md#v2_send_event) - Send an event to a running workflow

### [reconciliation](docs/sdks/reconciliation/README.md)

* [create_policy](docs/sdks/reconciliation/README.md#create_policy) - Create a policy
* [delete_policy](docs/sdks/reconciliation/README.md#delete_policy) - Delete a policy
* [get_policy](docs/sdks/reconciliation/README.md#get_policy) - Get a policy
* [get_reconciliation](docs/sdks/reconciliation/README.md#get_reconciliation) - Get a reconciliation
* [list_policies](docs/sdks/reconciliation/README.md#list_policies) - List policies
* [list_reconciliations](docs/sdks/reconciliation/README.md#list_reconciliations) - List reconciliations
* [reconcile](docs/sdks/reconciliation/README.md#reconcile) - Reconcile using a policy
* [reconciliationget_server_info](docs/sdks/reconciliation/README.md#reconciliationget_server_info) - Get server info

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



<!-- Start Dev Containers -->



<!-- End Dev Containers -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://localhost` | None |

For example:


```python
import sdk


s = sdk.SDK(
    server_idx=0
)


res = s.sdk.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import sdk


s = sdk.SDK(
    server_url="http://localhost"
)


res = s.sdk.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
