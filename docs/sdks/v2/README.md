# V2
(*ledger.v2*)

## Overview

### Available Operations

* [add_metadata_on_transaction](#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](#add_metadata_to_account) - Add metadata to an account
* [count_accounts](#count_accounts) - Count the accounts from a ledger
* [count_transactions](#count_transactions) - Count the transactions from a ledger
* [create_bulk](#create_bulk) - Bulk request
* [create_ledger](#create_ledger) - Create a ledger
* [create_transaction](#create_transaction) - Create a new transaction to a ledger
* [delete_account_metadata](#delete_account_metadata) - Delete metadata by key
* [delete_ledger_metadata](#delete_ledger_metadata) - Delete ledger metadata by key
* [delete_transaction_metadata](#delete_transaction_metadata) - Delete metadata by key
* [export_logs](#export_logs) - Export logs
* [get_account](#get_account) - Get account by its address
* [get_balances_aggregated](#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](#get_info) - Show server information
* [get_ledger](#get_ledger) - Get a ledger
* [get_ledger_info](#get_ledger_info) - Get information about a ledger
* [get_metrics](#get_metrics) - Read in memory metrics
* [get_transaction](#get_transaction) - Get transaction from a ledger by its ID
* [get_volumes_with_balances](#get_volumes_with_balances) - Get list of volumes with balances for (account/asset)
* [import_logs](#import_logs)
* [list_accounts](#list_accounts) - List accounts from a ledger
* [list_ledgers](#list_ledgers) - List ledgers
* [list_logs](#list_logs) - List the logs from a ledger
* [list_transactions](#list_transactions) - List transactions from a ledger
* [read_stats](#read_stats) - Get statistics from a ledger
* [revert_transaction](#revert_transaction) - Revert a ledger transaction by its ID
* [update_ledger_metadata](#update_ledger_metadata) - Update ledger metadata

## add_metadata_on_transaction

Set the metadata of a transaction by its ID

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.add_metadata_on_transaction(request={
        "id": 1234,
        "ledger": "ledger001",
        "request_body": {
            "admin": "true",
        },
        "dry_run": True,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V2AddMetadataOnTransactionRequest](../../models/operations/v2addmetadataontransactionrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.V2AddMetadataOnTransactionResponse](../../models/operations/v2addmetadataontransactionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## add_metadata_to_account

Add metadata to an account

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.add_metadata_to_account(request={
        "request_body": {
            "admin": "true",
        },
        "address": "users:001",
        "ledger": "ledger001",
        "dry_run": True,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V2AddMetadataToAccountRequest](../../models/operations/v2addmetadatatoaccountrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V2AddMetadataToAccountResponse](../../models/operations/v2addmetadatatoaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## count_accounts

Count the accounts from a ledger

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.count_accounts(request={
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2CountAccountsRequest](../../models/operations/v2countaccountsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V2CountAccountsResponse](../../models/operations/v2countaccountsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## count_transactions

Count the transactions from a ledger

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.count_transactions(request={
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V2CountTransactionsRequest](../../models/operations/v2counttransactionsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V2CountTransactionsResponse](../../models/operations/v2counttransactionsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_bulk

Bulk request

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.create_bulk(request={
        "ledger": "ledger001",
        "request_body": [
            {
                "action": "<value>",
            },
        ],
        "atomic": True,
        "continue_on_failure": True,
        "parallel": True,
    })

    assert res.v2_bulk_response is not None

    # Handle response
    print(res.v2_bulk_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V2CreateBulkRequest](../../models/operations/v2createbulkrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V2CreateBulkResponse](../../models/operations/v2createbulkresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_ledger

Create a ledger

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.create_ledger(request={
        "ledger": "ledger001",
        "v2_create_ledger_request": {
            "metadata": {
                "admin": "true",
            },
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V2CreateLedgerRequest](../../models/operations/v2createledgerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.V2CreateLedgerResponse](../../models/operations/v2createledgerresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_transaction

Create a new transaction to a ledger

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.create_transaction(request={
        "v2_post_transaction": {
            "metadata": {
                "admin": "true",
            },
            "postings": [
                {
                    "amount": 100,
                    "asset": "COIN",
                    "destination": "users:002",
                    "source": "users:001",
                },
                {
                    "amount": 100,
                    "asset": "COIN",
                    "destination": "users:002",
                    "source": "users:001",
                },
            ],
            "reference": "ref:001",
            "script": {
                "plain": "vars {\n" +
                "account $user\n" +
                "}\n" +
                "send [COIN 10] (\n" +
                "	source = @world\n" +
                "	destination = $user\n" +
                ")\n" +
                "",
                "vars": {
                    "user": "users:042",
                },
            },
        },
        "ledger": "ledger001",
        "dry_run": True,
        "force": True,
    })

    assert res.v2_create_transaction_response is not None

    # Handle response
    print(res.v2_create_transaction_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V2CreateTransactionRequest](../../models/operations/v2createtransactionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V2CreateTransactionResponse](../../models/operations/v2createtransactionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## delete_account_metadata

Delete metadata by key

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.delete_account_metadata(request={
        "address": "96609 Cummings Canyon",
        "key": "foo",
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V2DeleteAccountMetadataRequest](../../models/operations/v2deleteaccountmetadatarequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V2DeleteAccountMetadataResponse](../../models/operations/v2deleteaccountmetadataresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## delete_ledger_metadata

Delete ledger metadata by key

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.delete_ledger_metadata(request={
        "key": "foo",
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V2DeleteLedgerMetadataRequest](../../models/operations/v2deleteledgermetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V2DeleteLedgerMetadataResponse](../../models/operations/v2deleteledgermetadataresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## delete_transaction_metadata

Delete metadata by key

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.delete_transaction_metadata(request={
        "id": 1234,
        "key": "foo",
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.V2DeleteTransactionMetadataRequest](../../models/operations/v2deletetransactionmetadatarequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.V2DeleteTransactionMetadataResponse](../../models/operations/v2deletetransactionmetadataresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## export_logs

Export logs

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.export_logs(request={
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V2ExportLogsRequest](../../models/operations/v2exportlogsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V2ExportLogsResponse](../../models/operations/v2exportlogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_account

Get account by its address

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_account(request={
        "address": "users:001",
        "ledger": "ledger001",
    })

    assert res.v2_account_response is not None

    # Handle response
    print(res.v2_account_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V2GetAccountRequest](../../models/operations/v2getaccountrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V2GetAccountResponse](../../models/operations/v2getaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_balances_aggregated

Get the aggregated balances from selected accounts

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_balances_aggregated(request={
        "ledger": "ledger001",
    })

    assert res.v2_aggregate_balances_response is not None

    # Handle response
    print(res.v2_aggregate_balances_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V2GetBalancesAggregatedRequest](../../models/operations/v2getbalancesaggregatedrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V2GetBalancesAggregatedResponse](../../models/operations/v2getbalancesaggregatedresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_info

Show server information

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_info()

    assert res.v2_config_info_response is not None

    # Handle response
    print(res.v2_config_info_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.V2GetInfoResponse](../../models/operations/v2getinforesponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_ledger

Get a ledger

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_ledger(request={
        "ledger": "ledger001",
    })

    assert res.v2_get_ledger_response is not None

    # Handle response
    print(res.v2_get_ledger_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V2GetLedgerRequest](../../models/operations/v2getledgerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V2GetLedgerResponse](../../models/operations/v2getledgerresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_ledger_info

Get information about a ledger

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_ledger_info(request={
        "ledger": "ledger001",
    })

    assert res.v2_ledger_info_response is not None

    # Handle response
    print(res.v2_ledger_info_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2GetLedgerInfoRequest](../../models/operations/v2getledgerinforequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V2GetLedgerInfoResponse](../../models/operations/v2getledgerinforesponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_metrics

Read in memory metrics

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_metrics()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetMetricsResponse](../../models/operations/getmetricsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_transaction

Get transaction from a ledger by its ID

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_transaction(request={
        "id": 1234,
        "ledger": "ledger001",
    })

    assert res.v2_get_transaction_response is not None

    # Handle response
    print(res.v2_get_transaction_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V2GetTransactionRequest](../../models/operations/v2gettransactionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V2GetTransactionResponse](../../models/operations/v2gettransactionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_volumes_with_balances

Get list of volumes with balances for (account/asset)

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.get_volumes_with_balances(request={
        "ledger": "ledger001",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "group_by": 3,
        "page_size": 100,
    })

    assert res.v2_volumes_with_balance_cursor_response is not None

    # Handle response
    print(res.v2_volumes_with_balance_cursor_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V2GetVolumesWithBalancesRequest](../../models/operations/v2getvolumeswithbalancesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.V2GetVolumesWithBalancesResponse](../../models/operations/v2getvolumeswithbalancesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## import_logs

### Example Usage

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
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V2ImportLogsRequest](../../models/operations/v2importlogsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V2ImportLogsResponse](../../models/operations/v2importlogsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_accounts

List accounts from a ledger, sorted by address in descending order.

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.list_accounts(request={
        "ledger": "ledger001",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_accounts_cursor_response is not None

    # Handle response
    print(res.v2_accounts_cursor_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V2ListAccountsRequest](../../models/operations/v2listaccountsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.V2ListAccountsResponse](../../models/operations/v2listaccountsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_ledgers

List ledgers

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.list_ledgers(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_ledger_list_response is not None

    # Handle response
    print(res.v2_ledger_list_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2ListLedgersRequest](../../models/operations/v2listledgersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.V2ListLedgersResponse](../../models/operations/v2listledgersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_logs

List the logs from a ledger, sorted by ID in descending order.

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.list_logs(request={
        "ledger": "ledger001",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_logs_cursor_response is not None

    # Handle response
    print(res.v2_logs_cursor_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.V2ListLogsRequest](../../models/operations/v2listlogsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.V2ListLogsResponse](../../models/operations/v2listlogsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_transactions

List transactions from a ledger, sorted by id in descending order.

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.list_transactions(request={
        "ledger": "ledger001",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_transactions_cursor_response is not None

    # Handle response
    print(res.v2_transactions_cursor_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V2ListTransactionsRequest](../../models/operations/v2listtransactionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.V2ListTransactionsResponse](../../models/operations/v2listtransactionsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## read_stats

Get statistics from a ledger. (aggregate metrics on accounts and transactions)


### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.read_stats(request={
        "ledger": "ledger001",
    })

    assert res.v2_stats_response is not None

    # Handle response
    print(res.v2_stats_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V2ReadStatsRequest](../../models/operations/v2readstatsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V2ReadStatsResponse](../../models/operations/v2readstatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## revert_transaction

Revert a ledger transaction by its ID

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.revert_transaction(request={
        "id": 1234,
        "ledger": "ledger001",
        "dry_run": True,
    })

    assert res.v2_revert_transaction_response is not None

    # Handle response
    print(res.v2_revert_transaction_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V2RevertTransactionRequest](../../models/operations/v2reverttransactionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V2RevertTransactionResponse](../../models/operations/v2reverttransactionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## update_ledger_metadata

Update ledger metadata

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.v2.update_ledger_metadata(request={
        "ledger": "ledger001",
        "request_body": {
            "admin": "true",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V2UpdateLedgerMetadataRequest](../../models/operations/v2updateledgermetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V2UpdateLedgerMetadataResponse](../../models/operations/v2updateledgermetadataresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |