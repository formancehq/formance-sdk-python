# formance-sdk-python

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

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
<!-- $toc-max-depth=2 -->
* [formance-sdk-python](https://github.com/formancehq/formance-sdk-python/blob/master/#formance-sdk-python)
  * [🏗 **Welcome to your new SDK!** 🏗](https://github.com/formancehq/formance-sdk-python/blob/master/#welcome-to-your-new-sdk)
* [Introduction](https://github.com/formancehq/formance-sdk-python/blob/master/#introduction)
* [Authentication](https://github.com/formancehq/formance-sdk-python/blob/master/#authentication)
  * [SDK Installation](https://github.com/formancehq/formance-sdk-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/formancehq/formance-sdk-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/formancehq/formance-sdk-python/blob/master/#sdk-example-usage)
  * [Available Resources and Operations](https://github.com/formancehq/formance-sdk-python/blob/master/#available-resources-and-operations)
  * [File uploads](https://github.com/formancehq/formance-sdk-python/blob/master/#file-uploads)
  * [Retries](https://github.com/formancehq/formance-sdk-python/blob/master/#retries)
  * [Error Handling](https://github.com/formancehq/formance-sdk-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/formancehq/formance-sdk-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/formancehq/formance-sdk-python/blob/master/#custom-http-client)
  * [Authentication](https://github.com/formancehq/formance-sdk-python/blob/master/#authentication-1)
  * [Resource Management](https://github.com/formancehq/formance-sdk-python/blob/master/#resource-management)
  * [Debugging](https://github.com/formancehq/formance-sdk-python/blob/master/#debugging)
* [Development](https://github.com/formancehq/formance-sdk-python/blob/master/#development)
  * [Maturity](https://github.com/formancehq/formance-sdk-python/blob/master/#maturity)
  * [Contributions](https://github.com/formancehq/formance-sdk-python/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install formance-sdk-python
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add formance-sdk-python
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from formance-sdk-python python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "formance-sdk-python",
# ]
# ///

from formance_sdk_python import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from formance_sdk_python import SDK
from formance_sdk_python.models import shared

async def main():

    async with SDK(
        security=shared.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:

        res = await sdk.get_versions_async()

        assert res.get_versions_response is not None

        # Handle response
        print(res.get_versions_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [auth](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/auth/README.md)


#### [auth.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md)

* [create_client](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#create_client) - Create client
* [create_secret](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#create_secret) - Add a secret to a client
* [delete_client](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#delete_client) - Delete client
* [delete_secret](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#delete_secret) - Delete a secret from a client
* [get_oidc_well_knowns](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#get_oidc_well_knowns) - Retrieve OpenID connect well-knowns.
* [get_server_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#get_server_info) - Get server info
* [list_clients](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#list_clients) - List clients
* [list_users](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#list_users) - List users
* [read_client](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#read_client) - Read client
* [read_user](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#read_user) - Read user
* [update_client](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v1/README.md#update_client) - Update client

### [ledger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/ledger/README.md)


#### [ledger.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md)

* [create_transactions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#create_transactions) - Create a new batch of transactions to a ledger
* [add_metadata_on_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#add_metadata_to_account) - Add metadata to an account
* [count_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#count_accounts) - Count the accounts from a ledger
* [count_transactions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#count_transactions) - Count the transactions from a ledger
* [create_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#create_transaction) - Create a new transaction to a ledger
* [get_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_account) - Get account by its address
* [get_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_balances) - Get the balances from a ledger's account
* [get_balances_aggregated](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_info) - Show server information
* [get_ledger_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_ledger_info) - Get information about a ledger
* [get_mapping](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_mapping) - Get the mapping of a ledger
* [get_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#get_transaction) - Get transaction from a ledger by its ID
* [list_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#list_accounts) - List accounts from a ledger
* [list_logs](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#list_logs) - List the logs from a ledger
* [list_transactions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#list_transactions) - List transactions from a ledger
* [read_stats](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#read_stats) - Get statistics from a ledger
* [revert_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#revert_transaction) - Revert a ledger transaction by its ID
* [~~run_script~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#run_script) - Execute a Numscript :warning: **Deprecated**
* [update_mapping](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv1/README.md#update_mapping) - Update the mapping of a ledger

#### [ledger.v2](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md)

* [add_metadata_on_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#add_metadata_to_account) - Add metadata to an account
* [count_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#count_accounts) - Count the accounts from a ledger
* [count_transactions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#count_transactions) - Count the transactions from a ledger
* [create_bulk](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#create_bulk) - Bulk request
* [create_ledger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#create_ledger) - Create a ledger
* [create_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#create_transaction) - Create a new transaction to a ledger
* [delete_account_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#delete_account_metadata) - Delete metadata by key
* [delete_ledger_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#delete_ledger_metadata) - Delete ledger metadata by key
* [delete_transaction_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#delete_transaction_metadata) - Delete metadata by key
* [export_logs](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#export_logs) - Export logs
* [get_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_account) - Get account by its address
* [get_balances_aggregated](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_info) - Show server information
* [get_ledger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_ledger) - Get a ledger
* [get_ledger_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_ledger_info) - Get information about a ledger
* [get_metrics](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_metrics) - Read in memory metrics
* [get_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_transaction) - Get transaction from a ledger by its ID
* [get_volumes_with_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#get_volumes_with_balances) - Get list of volumes with balances for (account/asset)
* [import_logs](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#import_logs)
* [list_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#list_accounts) - List accounts from a ledger
* [list_ledgers](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#list_ledgers) - List ledgers
* [list_logs](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#list_logs) - List the logs from a ledger
* [list_transactions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#list_transactions) - List transactions from a ledger
* [read_stats](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#read_stats) - Get statistics from a ledger
* [revert_transaction](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#revert_transaction) - Revert a ledger transaction by its ID
* [update_ledger_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v2/README.md#update_ledger_metadata) - Update ledger metadata

### [orchestration](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/orchestration/README.md)


#### [orchestration.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md)

* [cancel_event](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#cancel_event) - Cancel a running workflow
* [create_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#create_trigger) - Create trigger
* [create_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#create_workflow) - Create workflow
* [delete_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#delete_trigger) - Delete trigger
* [delete_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#delete_workflow) - Delete a flow by id
* [get_instance](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#get_instance) - Get a workflow instance by id
* [get_instance_history](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#get_instance_stage_history) - Get a workflow instance stage history
* [get_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#get_workflow) - Get a flow by id
* [list_instances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#list_instances) - List instances of a workflow
* [list_triggers](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#list_triggers) - List triggers
* [list_triggers_occurrences](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#list_triggers_occurrences) - List triggers occurrences
* [list_workflows](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#list_workflows) - List registered workflows
* [orchestrationget_server_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#orchestrationget_server_info) - Get server info
* [read_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#read_trigger) - Read trigger
* [run_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#run_workflow) - Run workflow
* [send_event](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkorchestrationv1/README.md#send_event) - Send an event to a running workflow

#### [orchestration.v2](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md)

* [cancel_event](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#cancel_event) - Cancel a running workflow
* [create_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#create_trigger) - Create trigger
* [create_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#create_workflow) - Create workflow
* [delete_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#delete_trigger) - Delete trigger
* [delete_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#delete_workflow) - Delete a flow by id
* [get_instance](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#get_instance) - Get a workflow instance by id
* [get_instance_history](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#get_instance_stage_history) - Get a workflow instance stage history
* [get_server_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#get_server_info) - Get server info
* [get_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#get_workflow) - Get a flow by id
* [list_instances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#list_instances) - List instances of a workflow
* [list_triggers](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#list_triggers) - List triggers
* [list_triggers_occurrences](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#list_triggers_occurrences) - List triggers occurrences
* [list_workflows](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#list_workflows) - List registered workflows
* [read_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#read_trigger) - Read trigger
* [run_workflow](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#run_workflow) - Run workflow
* [send_event](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#send_event) - Send an event to a running workflow
* [test_trigger](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkv2/README.md#test_trigger) - Test trigger

### [payments](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/payments/README.md)


#### [payments.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md)

* [add_account_to_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#add_account_to_pool) - Add an account to a pool
* [connectors_transfer](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#connectors_transfer) - Transfer funds between Connector accounts
* [create_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#create_account) - Create an account
* [create_bank_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#create_bank_account) - Create a BankAccount in Payments and on the PSP
* [create_payment](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#create_payment) - Create a payment
* [create_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#create_pool) - Create a Pool
* [create_transfer_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#create_transfer_initiation) - Create a TransferInitiation
* [delete_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#delete_pool) - Delete a Pool
* [delete_transfer_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#delete_transfer_initiation) - Delete a transfer initiation
* [forward_bank_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#forward_bank_account) - Forward a bank account to a connector
* [get_account_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_account_balances) - Get account balances
* [get_bank_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_bank_account) - Get a bank account created by user on Formance
* [~~get_connector_task~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_connector_task) - Read a specific task of the connector :warning: **Deprecated**
* [get_connector_task_v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_connector_task_v1) - Read a specific task of the connector
* [get_payment](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_payment) - Get a payment
* [get_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_pool) - Get a Pool
* [get_pool_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_pool_balances) - Get pool balances
* [get_transfer_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#get_transfer_initiation) - Get a transfer initiation
* [install_connector](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#install_connector) - Install a connector
* [list_all_connectors](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_all_connectors) - List all installed connectors
* [list_bank_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_bank_accounts) - List bank accounts created by user on Formance
* [list_configs_available_connectors](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_configs_available_connectors) - List the configs of each available connector
* [~~list_connector_tasks~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_connector_tasks) - List tasks from a connector :warning: **Deprecated**
* [list_connector_tasks_v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_connector_tasks_v1) - List tasks from a connector
* [list_payments](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_payments) - List payments
* [list_pools](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_pools) - List Pools
* [list_transfer_initiations](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#list_transfer_initiations) - List Transfer Initiations
* [paymentsget_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#paymentsget_account) - Get an account
* [paymentsget_server_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#paymentsget_server_info) - Get server info
* [paymentslist_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#paymentslist_accounts) - List accounts
* [~~read_connector_config~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#read_connector_config) - Read the config of a connector :warning: **Deprecated**
* [read_connector_config_v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#read_connector_config_v1) - Read the config of a connector
* [remove_account_from_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#remove_account_from_pool) - Remove an account from a pool
* [~~reset_connector~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#reset_connector) - Reset a connector :warning: **Deprecated**
* [reset_connector_v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#reset_connector_v1) - Reset a connector
* [retry_transfer_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#retry_transfer_initiation) - Retry a failed transfer initiation
* [reverse_transfer_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#reverse_transfer_initiation) - Reverse a transfer initiation
* [udpate_transfer_initiation_status](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#udpate_transfer_initiation_status) - Update the status of a transfer initiation
* [~~uninstall_connector~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#uninstall_connector) - Uninstall a connector :warning: **Deprecated**
* [uninstall_connector_v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#uninstall_connector_v1) - Uninstall a connector
* [update_bank_account_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#update_bank_account_metadata) - Update metadata of a bank account
* [update_connector_config_v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#update_connector_config_v1) - Update the config of a connector
* [update_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkpaymentsv1/README.md#update_metadata) - Update metadata

#### [payments.v3](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md)

* [add_account_to_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#add_account_to_pool) - Add an account to a pool
* [approve_payment_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#approve_payment_initiation) - Approve a payment initiation
* [create_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#create_account) - Create a formance account object. This object will not be forwarded to the connector. It is only used for internal purposes.

* [create_bank_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#create_bank_account) - Create a formance bank account object. This object will not be forwarded to the connector until you called the forwardBankAccount method.

* [create_payment](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#create_payment) - Create a formance payment object. This object will not be forwarded to the connector. It is only used for internal purposes.

* [create_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#create_pool) - Create a formance pool object
* [delete_payment_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#delete_payment_initiation) - Delete a payment initiation by ID
* [delete_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#delete_pool) - Delete a pool by ID
* [forward_bank_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#forward_bank_account) - Forward a Bank Account to a PSP for creation
* [get_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_account) - Get an account by ID
* [get_account_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_account_balances) - Get account balances
* [get_bank_account](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_bank_account) - Get a Bank Account by ID
* [get_connector_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_connector_config) - Get a connector configuration by ID
* [get_connector_schedule](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_connector_schedule) - Get a connector schedule by ID
* [get_payment](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_payment) - Get a payment by ID
* [get_payment_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_payment_initiation) - Get a payment initiation by ID
* [get_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_pool) - Get a pool by ID
* [get_pool_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_pool_balances) - Get pool balances
* [get_task](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#get_task) - Get a task and its result by ID
* [initiate_payment](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#initiate_payment) - Initiate a payment
* [install_connector](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#install_connector) - Install a connector
* [list_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_accounts) - List all accounts
* [list_bank_accounts](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_bank_accounts) - List all bank accounts
* [list_connector_configs](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_connector_configs) - List all connector configurations
* [list_connector_schedule_instances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_connector_schedule_instances) - List all connector schedule instances
* [list_connector_schedules](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_connector_schedules) - List all connector schedules
* [list_connectors](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_connectors) - List all connectors
* [list_payment_initiation_adjustments](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_payment_initiation_adjustments) - List all payment initiation adjustments
* [list_payment_initiation_related_payments](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_payment_initiation_related_payments) - List all payments related to a payment initiation
* [list_payment_initiations](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_payment_initiations) - List all payment initiations
* [list_payments](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_payments) - List all payments
* [list_pools](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#list_pools) - List all pools
* [reject_payment_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#reject_payment_initiation) - Reject a payment initiation
* [remove_account_from_pool](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#remove_account_from_pool) - Remove an account from a pool
* [reset_connector](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#reset_connector) - Reset a connector. Be aware that this will delete all data and stop all existing tasks like payment initiations and bank account creations.
* [retry_payment_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#retry_payment_initiation) - Retry a payment initiation
* [reverse_payment_initiation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#reverse_payment_initiation) - Reverse a payment initiation
* [uninstall_connector](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#uninstall_connector) - Uninstall a connector
* [update_bank_account_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#update_bank_account_metadata) - Update a bank account's metadata
* [update_payment_metadata](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/v3/README.md#update_payment_metadata) - Update a payment's metadata

### [reconciliation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/reconciliation/README.md)


#### [reconciliation.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md)

* [create_policy](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#create_policy) - Create a policy
* [delete_policy](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#delete_policy) - Delete a policy
* [get_policy](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#get_policy) - Get a policy
* [get_reconciliation](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#get_reconciliation) - Get a reconciliation
* [list_policies](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#list_policies) - List policies
* [list_reconciliations](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#list_reconciliations) - List reconciliations
* [reconcile](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#reconcile) - Reconcile using a policy
* [reconciliationget_server_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkreconciliationv1/README.md#reconciliationget_server_info) - Get server info

### [SDK](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdk/README.md)

* [get_versions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdk/README.md#get_versions) - Show stack version information

### [~~search~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/search/README.md)


#### [~~search.v1~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdksearchv1/README.md)

* [~~search~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdksearchv1/README.md#search) - search.v1 :warning: **Deprecated**
* [~~searchget_server_info~~](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdksearchv1/README.md#searchget_server_info) - Get server info :warning: **Deprecated**

### [wallets](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/wallets/README.md)


#### [wallets.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md)

* [confirm_hold](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#confirm_hold) - Confirm a hold
* [create_balance](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#create_balance) - Create a balance
* [create_wallet](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#create_wallet) - Create a new wallet
* [credit_wallet](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#credit_wallet) - Credit a wallet
* [debit_wallet](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#debit_wallet) - Debit a wallet
* [get_balance](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#get_balance) - Get detailed balance
* [get_hold](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#get_hold) - Get a hold
* [get_holds](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#get_holds) - Get all holds for a wallet
* [get_transactions](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#get_transactions)
* [get_wallet](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#get_wallet) - Get a wallet
* [get_wallet_summary](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#get_wallet_summary) - Get wallet summary
* [list_balances](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#list_balances) - List balances of a wallet
* [list_wallets](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#list_wallets) - List all wallets
* [update_wallet](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#update_wallet) - Update a wallet
* [void_hold](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#void_hold) - Cancel a hold
* [walletsget_server_info](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwalletsv1/README.md#walletsget_server_info) - Get server info

### [webhooks](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/webhooks/README.md)


#### [webhooks.v1](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md)

* [activate_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#activate_config) - Activate one config
* [change_config_secret](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#change_config_secret) - Change the signing secret of a config
* [deactivate_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#deactivate_config) - Deactivate one config
* [delete_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#delete_config) - Delete one config
* [get_many_configs](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#get_many_configs) - Get many configs
* [insert_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#insert_config) - Insert a new config
* [test_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#test_config) - Test one config
* [update_config](https://github.com/formancehq/formance-sdk-python/blob/master/docs/sdks/sdkwebhooksv1/README.md#update_config) - Update one config

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.import_logs(request={
        "v2_import_logs_request": open("example.file", "rb"),
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
from formance_sdk_python.utils import BackoffStrategy, RetryConfig


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.get_versions(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
from formance_sdk_python.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `add_metadata_on_transaction_async` method may raise the following exceptions:

| Error Type             | Status Code | Content Type     |
| ---------------------- | ----------- | ---------------- |
| errors.V2ErrorResponse | default     | application/json |
| errors.SDKError        | 4XX, 5XX    | \*/\*            |

### Example

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import errors, shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:
    res = None
    try:

        res = sdk.ledger.v2.add_metadata_on_transaction(request={
            "request_body": {
                "admin": "true",
            },
            "id": 1234,
            "ledger": "ledger001",
            "dry_run": True,
        })

        assert res is not None

        # Handle response
        print(res)

    except errors.V2ErrorResponse as e:
        # handle e.data: errors.V2ErrorResponseData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                                                | Variables                        | Description                                |
| --- | ----------------------------------------------------- | -------------------------------- | ------------------------------------------ |
| 0   | `http://localhost`                                    |                                  | local server                               |
| 1   | `https://{organization}.{environment}.formance.cloud` | `environment`<br/>`organization` | A per-organization and per-environment API |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable       | Parameter                               | Supported Values                                                           | Default           | Description                                                   |
| -------------- | --------------------------------------- | -------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------- |
| `environment`  | `environment: models.ServerEnvironment` | - `"eu.sandbox"`<br/>- `"sandbox"`<br/>- `"eu-west-1"`<br/>- `"us-east-1"` | `"eu.sandbox"`    | The environment name. Defaults to the production environment. |
| `organization` | `organization: str`                     | str                                                                        | `"orgID-stackID"` | The organization name. Defaults to a generic organization.    |

#### Example

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    server_idx=1,
    environment="us-east-1"
    organization="<value>"
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    server_url="http://localhost",
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from formance_sdk_python import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from formance_sdk_python import SDK
from formance_sdk_python.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                            | Type   | Scheme                         |
| ------------------------------- | ------ | ------------------------------ |
| `client_id`<br/>`client_secret` | oauth2 | OAuth2 Client Credentials Flow |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
def main():

    with SDK(
        security=shared.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        security=shared.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from formance_sdk_python import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("formance_sdk_python"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
