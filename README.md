# formance-sdk-python

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary

Formance Stack API: Open, modular foundation for unique payments flows

# Introduction
This API is documented in **OpenAPI format**.

# Authentication
Formance Stack offers one forms of authentication:
  - OAuth2
OAuth2 - an open protocol to allow secure authorization in a simple
and standard method from web, mobile and desktop applications.
<SecurityDefinitions />
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed using the *pip* package manager, with dependencies and metadata stored in the `setup.py` file.

```bash
pip install formance-sdk-python
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [auth](docs/sdks/auth/README.md)


#### [auth.v1](docs/sdks/v1/README.md)

* [create_client](docs/sdks/v1/README.md#create_client) - Create client
* [create_secret](docs/sdks/v1/README.md#create_secret) - Add a secret to a client
* [delete_client](docs/sdks/v1/README.md#delete_client) - Delete client
* [delete_secret](docs/sdks/v1/README.md#delete_secret) - Delete a secret from a client
* [get_oidc_well_knowns](docs/sdks/v1/README.md#get_oidc_well_knowns) - Retrieve OpenID connect well-knowns.
* [get_server_info](docs/sdks/v1/README.md#get_server_info) - Get server info
* [list_clients](docs/sdks/v1/README.md#list_clients) - List clients
* [list_users](docs/sdks/v1/README.md#list_users) - List users
* [read_client](docs/sdks/v1/README.md#read_client) - Read client
* [read_user](docs/sdks/v1/README.md#read_user) - Read user
* [update_client](docs/sdks/v1/README.md#update_client) - Update client

### [ledger](docs/sdks/ledger/README.md)


#### [ledger.v1](docs/sdks/sdkv1/README.md)

* [create_transactions](docs/sdks/sdkv1/README.md#create_transactions) - Create a new batch of transactions to a ledger
* [add_metadata_on_transaction](docs/sdks/sdkv1/README.md#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](docs/sdks/sdkv1/README.md#add_metadata_to_account) - Add metadata to an account
* [count_accounts](docs/sdks/sdkv1/README.md#count_accounts) - Count the accounts from a ledger
* [count_transactions](docs/sdks/sdkv1/README.md#count_transactions) - Count the transactions from a ledger
* [create_transaction](docs/sdks/sdkv1/README.md#create_transaction) - Create a new transaction to a ledger
* [get_account](docs/sdks/sdkv1/README.md#get_account) - Get account by its address
* [get_balances](docs/sdks/sdkv1/README.md#get_balances) - Get the balances from a ledger's account
* [get_balances_aggregated](docs/sdks/sdkv1/README.md#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](docs/sdks/sdkv1/README.md#get_info) - Show server information
* [get_ledger_info](docs/sdks/sdkv1/README.md#get_ledger_info) - Get information about a ledger
* [get_mapping](docs/sdks/sdkv1/README.md#get_mapping) - Get the mapping of a ledger
* [get_transaction](docs/sdks/sdkv1/README.md#get_transaction) - Get transaction from a ledger by its ID
* [list_accounts](docs/sdks/sdkv1/README.md#list_accounts) - List accounts from a ledger
* [list_logs](docs/sdks/sdkv1/README.md#list_logs) - List the logs from a ledger
* [list_transactions](docs/sdks/sdkv1/README.md#list_transactions) - List transactions from a ledger
* [read_stats](docs/sdks/sdkv1/README.md#read_stats) - Get statistics from a ledger
* [revert_transaction](docs/sdks/sdkv1/README.md#revert_transaction) - Revert a ledger transaction by its ID
* [~~run_script~~](docs/sdks/sdkv1/README.md#run_script) - Execute a Numscript :warning: **Deprecated**
* [update_mapping](docs/sdks/sdkv1/README.md#update_mapping) - Update the mapping of a ledger

#### [ledger.v2](docs/sdks/v2/README.md)

* [add_metadata_on_transaction](docs/sdks/v2/README.md#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](docs/sdks/v2/README.md#add_metadata_to_account) - Add metadata to an account
* [count_accounts](docs/sdks/v2/README.md#count_accounts) - Count the accounts from a ledger
* [count_transactions](docs/sdks/v2/README.md#count_transactions) - Count the transactions from a ledger
* [create_bulk](docs/sdks/v2/README.md#create_bulk) - Bulk request
* [create_ledger](docs/sdks/v2/README.md#create_ledger) - Create a ledger
* [create_transaction](docs/sdks/v2/README.md#create_transaction) - Create a new transaction to a ledger
* [delete_account_metadata](docs/sdks/v2/README.md#delete_account_metadata) - Delete metadata by key
* [delete_ledger_metadata](docs/sdks/v2/README.md#delete_ledger_metadata) - Delete ledger metadata by key
* [delete_transaction_metadata](docs/sdks/v2/README.md#delete_transaction_metadata) - Delete metadata by key
* [export_logs](docs/sdks/v2/README.md#export_logs) - Export logs
* [get_account](docs/sdks/v2/README.md#get_account) - Get account by its address
* [get_balances_aggregated](docs/sdks/v2/README.md#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](docs/sdks/v2/README.md#get_info) - Show server information
* [get_ledger](docs/sdks/v2/README.md#get_ledger) - Get a ledger
* [get_ledger_info](docs/sdks/v2/README.md#get_ledger_info) - Get information about a ledger
* [get_transaction](docs/sdks/v2/README.md#get_transaction) - Get transaction from a ledger by its ID
* [get_volumes_with_balances](docs/sdks/v2/README.md#get_volumes_with_balances) - Get list of volumes with balances for (account/asset)
* [import_logs](docs/sdks/v2/README.md#import_logs)
* [list_accounts](docs/sdks/v2/README.md#list_accounts) - List accounts from a ledger
* [list_ledgers](docs/sdks/v2/README.md#list_ledgers) - List ledgers
* [list_logs](docs/sdks/v2/README.md#list_logs) - List the logs from a ledger
* [list_transactions](docs/sdks/v2/README.md#list_transactions) - List transactions from a ledger
* [read_stats](docs/sdks/v2/README.md#read_stats) - Get statistics from a ledger
* [revert_transaction](docs/sdks/v2/README.md#revert_transaction) - Revert a ledger transaction by its ID
* [update_ledger_metadata](docs/sdks/v2/README.md#update_ledger_metadata) - Update ledger metadata

### [orchestration](docs/sdks/orchestration/README.md)


#### [orchestration.v1](docs/sdks/sdkorchestrationv1/README.md)

* [cancel_event](docs/sdks/sdkorchestrationv1/README.md#cancel_event) - Cancel a running workflow
* [create_trigger](docs/sdks/sdkorchestrationv1/README.md#create_trigger) - Create trigger
* [create_workflow](docs/sdks/sdkorchestrationv1/README.md#create_workflow) - Create workflow
* [delete_trigger](docs/sdks/sdkorchestrationv1/README.md#delete_trigger) - Delete trigger
* [delete_workflow](docs/sdks/sdkorchestrationv1/README.md#delete_workflow) - Delete a flow by id
* [get_instance](docs/sdks/sdkorchestrationv1/README.md#get_instance) - Get a workflow instance by id
* [get_instance_history](docs/sdks/sdkorchestrationv1/README.md#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](docs/sdks/sdkorchestrationv1/README.md#get_instance_stage_history) - Get a workflow instance stage history
* [get_workflow](docs/sdks/sdkorchestrationv1/README.md#get_workflow) - Get a flow by id
* [list_instances](docs/sdks/sdkorchestrationv1/README.md#list_instances) - List instances of a workflow
* [list_triggers](docs/sdks/sdkorchestrationv1/README.md#list_triggers) - List triggers
* [list_triggers_occurrences](docs/sdks/sdkorchestrationv1/README.md#list_triggers_occurrences) - List triggers occurrences
* [list_workflows](docs/sdks/sdkorchestrationv1/README.md#list_workflows) - List registered workflows
* [orchestrationget_server_info](docs/sdks/sdkorchestrationv1/README.md#orchestrationget_server_info) - Get server info
* [read_trigger](docs/sdks/sdkorchestrationv1/README.md#read_trigger) - Read trigger
* [run_workflow](docs/sdks/sdkorchestrationv1/README.md#run_workflow) - Run workflow
* [send_event](docs/sdks/sdkorchestrationv1/README.md#send_event) - Send an event to a running workflow

#### [orchestration.v2](docs/sdks/sdkv2/README.md)

* [cancel_event](docs/sdks/sdkv2/README.md#cancel_event) - Cancel a running workflow
* [create_trigger](docs/sdks/sdkv2/README.md#create_trigger) - Create trigger
* [create_workflow](docs/sdks/sdkv2/README.md#create_workflow) - Create workflow
* [delete_trigger](docs/sdks/sdkv2/README.md#delete_trigger) - Delete trigger
* [delete_workflow](docs/sdks/sdkv2/README.md#delete_workflow) - Delete a flow by id
* [get_instance](docs/sdks/sdkv2/README.md#get_instance) - Get a workflow instance by id
* [get_instance_history](docs/sdks/sdkv2/README.md#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](docs/sdks/sdkv2/README.md#get_instance_stage_history) - Get a workflow instance stage history
* [get_server_info](docs/sdks/sdkv2/README.md#get_server_info) - Get server info
* [get_workflow](docs/sdks/sdkv2/README.md#get_workflow) - Get a flow by id
* [list_instances](docs/sdks/sdkv2/README.md#list_instances) - List instances of a workflow
* [list_triggers](docs/sdks/sdkv2/README.md#list_triggers) - List triggers
* [list_triggers_occurrences](docs/sdks/sdkv2/README.md#list_triggers_occurrences) - List triggers occurrences
* [list_workflows](docs/sdks/sdkv2/README.md#list_workflows) - List registered workflows
* [read_trigger](docs/sdks/sdkv2/README.md#read_trigger) - Read trigger
* [run_workflow](docs/sdks/sdkv2/README.md#run_workflow) - Run workflow
* [send_event](docs/sdks/sdkv2/README.md#send_event) - Send an event to a running workflow
* [test_trigger](docs/sdks/sdkv2/README.md#test_trigger) - Test trigger

### [payments](docs/sdks/payments/README.md)


#### [payments.v1](docs/sdks/sdkpaymentsv1/README.md)

* [add_account_to_pool](docs/sdks/sdkpaymentsv1/README.md#add_account_to_pool) - Add an account to a pool
* [connectors_transfer](docs/sdks/sdkpaymentsv1/README.md#connectors_transfer) - Transfer funds between Connector accounts
* [create_account](docs/sdks/sdkpaymentsv1/README.md#create_account) - Create an account
* [create_bank_account](docs/sdks/sdkpaymentsv1/README.md#create_bank_account) - Create a BankAccount in Payments and on the PSP
* [create_payment](docs/sdks/sdkpaymentsv1/README.md#create_payment) - Create a payment
* [create_pool](docs/sdks/sdkpaymentsv1/README.md#create_pool) - Create a Pool
* [create_transfer_initiation](docs/sdks/sdkpaymentsv1/README.md#create_transfer_initiation) - Create a TransferInitiation
* [delete_pool](docs/sdks/sdkpaymentsv1/README.md#delete_pool) - Delete a Pool
* [delete_transfer_initiation](docs/sdks/sdkpaymentsv1/README.md#delete_transfer_initiation) - Delete a transfer initiation
* [forward_bank_account](docs/sdks/sdkpaymentsv1/README.md#forward_bank_account) - Forward a bank account to a connector
* [get_account_balances](docs/sdks/sdkpaymentsv1/README.md#get_account_balances) - Get account balances
* [get_bank_account](docs/sdks/sdkpaymentsv1/README.md#get_bank_account) - Get a bank account created by user on Formance
* [~~get_connector_task~~](docs/sdks/sdkpaymentsv1/README.md#get_connector_task) - Read a specific task of the connector :warning: **Deprecated**
* [get_connector_task_v1](docs/sdks/sdkpaymentsv1/README.md#get_connector_task_v1) - Read a specific task of the connector
* [get_payment](docs/sdks/sdkpaymentsv1/README.md#get_payment) - Get a payment
* [get_pool](docs/sdks/sdkpaymentsv1/README.md#get_pool) - Get a Pool
* [get_pool_balances](docs/sdks/sdkpaymentsv1/README.md#get_pool_balances) - Get pool balances
* [get_transfer_initiation](docs/sdks/sdkpaymentsv1/README.md#get_transfer_initiation) - Get a transfer initiation
* [install_connector](docs/sdks/sdkpaymentsv1/README.md#install_connector) - Install a connector
* [list_all_connectors](docs/sdks/sdkpaymentsv1/README.md#list_all_connectors) - List all installed connectors
* [list_bank_accounts](docs/sdks/sdkpaymentsv1/README.md#list_bank_accounts) - List bank accounts created by user on Formance
* [list_configs_available_connectors](docs/sdks/sdkpaymentsv1/README.md#list_configs_available_connectors) - List the configs of each available connector
* [~~list_connector_tasks~~](docs/sdks/sdkpaymentsv1/README.md#list_connector_tasks) - List tasks from a connector :warning: **Deprecated**
* [list_connector_tasks_v1](docs/sdks/sdkpaymentsv1/README.md#list_connector_tasks_v1) - List tasks from a connector
* [list_payments](docs/sdks/sdkpaymentsv1/README.md#list_payments) - List payments
* [list_pools](docs/sdks/sdkpaymentsv1/README.md#list_pools) - List Pools
* [list_transfer_initiations](docs/sdks/sdkpaymentsv1/README.md#list_transfer_initiations) - List Transfer Initiations
* [paymentsget_account](docs/sdks/sdkpaymentsv1/README.md#paymentsget_account) - Get an account
* [paymentsget_server_info](docs/sdks/sdkpaymentsv1/README.md#paymentsget_server_info) - Get server info
* [paymentslist_accounts](docs/sdks/sdkpaymentsv1/README.md#paymentslist_accounts) - List accounts
* [~~read_connector_config~~](docs/sdks/sdkpaymentsv1/README.md#read_connector_config) - Read the config of a connector :warning: **Deprecated**
* [read_connector_config_v1](docs/sdks/sdkpaymentsv1/README.md#read_connector_config_v1) - Read the config of a connector
* [remove_account_from_pool](docs/sdks/sdkpaymentsv1/README.md#remove_account_from_pool) - Remove an account from a pool
* [~~reset_connector~~](docs/sdks/sdkpaymentsv1/README.md#reset_connector) - Reset a connector :warning: **Deprecated**
* [reset_connector_v1](docs/sdks/sdkpaymentsv1/README.md#reset_connector_v1) - Reset a connector
* [retry_transfer_initiation](docs/sdks/sdkpaymentsv1/README.md#retry_transfer_initiation) - Retry a failed transfer initiation
* [reverse_transfer_initiation](docs/sdks/sdkpaymentsv1/README.md#reverse_transfer_initiation) - Reverse a transfer initiation
* [udpate_transfer_initiation_status](docs/sdks/sdkpaymentsv1/README.md#udpate_transfer_initiation_status) - Update the status of a transfer initiation
* [~~uninstall_connector~~](docs/sdks/sdkpaymentsv1/README.md#uninstall_connector) - Uninstall a connector :warning: **Deprecated**
* [uninstall_connector_v1](docs/sdks/sdkpaymentsv1/README.md#uninstall_connector_v1) - Uninstall a connector
* [update_bank_account_metadata](docs/sdks/sdkpaymentsv1/README.md#update_bank_account_metadata) - Update metadata of a bank account
* [update_connector_config_v1](docs/sdks/sdkpaymentsv1/README.md#update_connector_config_v1) - Update the config of a connector
* [update_metadata](docs/sdks/sdkpaymentsv1/README.md#update_metadata) - Update metadata

### [reconciliation](docs/sdks/reconciliation/README.md)


#### [reconciliation.v1](docs/sdks/sdkreconciliationv1/README.md)

* [create_policy](docs/sdks/sdkreconciliationv1/README.md#create_policy) - Create a policy
* [delete_policy](docs/sdks/sdkreconciliationv1/README.md#delete_policy) - Delete a policy
* [get_policy](docs/sdks/sdkreconciliationv1/README.md#get_policy) - Get a policy
* [get_reconciliation](docs/sdks/sdkreconciliationv1/README.md#get_reconciliation) - Get a reconciliation
* [list_policies](docs/sdks/sdkreconciliationv1/README.md#list_policies) - List policies
* [list_reconciliations](docs/sdks/sdkreconciliationv1/README.md#list_reconciliations) - List reconciliations
* [reconcile](docs/sdks/sdkreconciliationv1/README.md#reconcile) - Reconcile using a policy
* [reconciliationget_server_info](docs/sdks/sdkreconciliationv1/README.md#reconciliationget_server_info) - Get server info

### [SDK](docs/sdks/sdk/README.md)

* [get_versions](docs/sdks/sdk/README.md#get_versions) - Show stack version information

### [search](docs/sdks/search/README.md)


#### [search.v1](docs/sdks/sdksearchv1/README.md)

* [search](docs/sdks/sdksearchv1/README.md#search) - search.v1
* [searchget_server_info](docs/sdks/sdksearchv1/README.md#searchget_server_info) - Get server info

### [wallets](docs/sdks/wallets/README.md)


#### [wallets.v1](docs/sdks/sdkwalletsv1/README.md)

* [confirm_hold](docs/sdks/sdkwalletsv1/README.md#confirm_hold) - Confirm a hold
* [create_balance](docs/sdks/sdkwalletsv1/README.md#create_balance) - Create a balance
* [create_wallet](docs/sdks/sdkwalletsv1/README.md#create_wallet) - Create a new wallet
* [credit_wallet](docs/sdks/sdkwalletsv1/README.md#credit_wallet) - Credit a wallet
* [debit_wallet](docs/sdks/sdkwalletsv1/README.md#debit_wallet) - Debit a wallet
* [get_balance](docs/sdks/sdkwalletsv1/README.md#get_balance) - Get detailed balance
* [get_hold](docs/sdks/sdkwalletsv1/README.md#get_hold) - Get a hold
* [get_holds](docs/sdks/sdkwalletsv1/README.md#get_holds) - Get all holds for a wallet
* [get_transactions](docs/sdks/sdkwalletsv1/README.md#get_transactions)
* [get_wallet](docs/sdks/sdkwalletsv1/README.md#get_wallet) - Get a wallet
* [get_wallet_summary](docs/sdks/sdkwalletsv1/README.md#get_wallet_summary) - Get wallet summary
* [list_balances](docs/sdks/sdkwalletsv1/README.md#list_balances) - List balances of a wallet
* [list_wallets](docs/sdks/sdkwalletsv1/README.md#list_wallets) - List all wallets
* [update_wallet](docs/sdks/sdkwalletsv1/README.md#update_wallet) - Update a wallet
* [void_hold](docs/sdks/sdkwalletsv1/README.md#void_hold) - Cancel a hold
* [walletsget_server_info](docs/sdks/sdkwalletsv1/README.md#walletsget_server_info) - Get server info

### [webhooks](docs/sdks/webhooks/README.md)


#### [webhooks.v1](docs/sdks/sdkwebhooksv1/README.md)

* [activate_config](docs/sdks/sdkwebhooksv1/README.md#activate_config) - Activate one config
* [change_config_secret](docs/sdks/sdkwebhooksv1/README.md#change_config_secret) - Change the signing secret of a config
* [deactivate_config](docs/sdks/sdkwebhooksv1/README.md#deactivate_config) - Deactivate one config
* [delete_config](docs/sdks/sdkwebhooksv1/README.md#delete_config) - Delete one config
* [get_many_configs](docs/sdks/sdkwebhooksv1/README.md#get_many_configs) - Get many configs
* [insert_config](docs/sdks/sdkwebhooksv1/README.md#insert_config) - Insert a new config
* [test_config](docs/sdks/sdkwebhooksv1/README.md#test_config) - Test one config

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

### Example

```python
import sdk
from sdk.models import errors, operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)

res = None
try:
    res = s.ledger.v1.create_transactions(request=operations.CreateTransactionsRequest(
    transactions=shared.Transactions(
        transactions=[
            shared.TransactionData(
                postings=[
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                ],
                reference='ref:001',
            ),
        ],
    ),
    ledger='ledger001',
))

except errors.ErrorResponse as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.transactions_response is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://localhost` | None |

#### Example

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    server_idx=0,
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    server_url="http://localhost",
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                           | Type                           | Scheme                         |
| ------------------------------ | ------------------------------ | ------------------------------ |
| `client_id` `client_secret`    | oauth2                         | OAuth2 Client Credentials Flow |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
