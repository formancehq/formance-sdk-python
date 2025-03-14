# SDKV1
(*ledger.v1*)

## Overview

### Available Operations

* [create_transactions](#create_transactions) - Create a new batch of transactions to a ledger
* [add_metadata_on_transaction](#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [add_metadata_to_account](#add_metadata_to_account) - Add metadata to an account
* [count_accounts](#count_accounts) - Count the accounts from a ledger
* [count_transactions](#count_transactions) - Count the transactions from a ledger
* [create_transaction](#create_transaction) - Create a new transaction to a ledger
* [get_account](#get_account) - Get account by its address
* [get_balances](#get_balances) - Get the balances from a ledger's account
* [get_balances_aggregated](#get_balances_aggregated) - Get the aggregated balances from selected accounts
* [get_info](#get_info) - Show server information
* [get_ledger_info](#get_ledger_info) - Get information about a ledger
* [get_mapping](#get_mapping) - Get the mapping of a ledger
* [get_transaction](#get_transaction) - Get transaction from a ledger by its ID
* [list_accounts](#list_accounts) - List accounts from a ledger
* [list_logs](#list_logs) - List the logs from a ledger
* [list_transactions](#list_transactions) - List transactions from a ledger
* [read_stats](#read_stats) - Get statistics from a ledger
* [revert_transaction](#revert_transaction) - Revert a ledger transaction by its ID
* [~~run_script~~](#run_script) - Execute a Numscript :warning: **Deprecated**
* [update_mapping](#update_mapping) - Update the mapping of a ledger

## create_transactions

Create a new batch of transactions to a ledger

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

    res = sdk.ledger.v1.create_transactions(request={
        "transactions": {
            "transactions": [
                {
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
                        {
                            "amount": 100,
                            "asset": "COIN",
                            "destination": "users:002",
                            "source": "users:001",
                        },
                    ],
                    "reference": "ref:001",
                },
            ],
        },
        "ledger": "ledger001",
    })

    assert res.transactions_response is not None

    # Handle response
    print(res.transactions_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateTransactionsRequest](../../models/operations/createtransactionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateTransactionsResponse](../../models/operations/createtransactionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.add_metadata_on_transaction(request={
        "request_body": {
            "key": "<value>",
        },
        "ledger": "ledger001",
        "txid": 1234,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.AddMetadataOnTransactionRequest](../../models/operations/addmetadataontransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.AddMetadataOnTransactionResponse](../../models/operations/addmetadataontransactionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.add_metadata_to_account(request={
        "request_body": {
            "key": "<value>",
        },
        "address": "users:001",
        "ledger": "ledger001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.AddMetadataToAccountRequest](../../models/operations/addmetadatatoaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.AddMetadataToAccountResponse](../../models/operations/addmetadatatoaccountresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.count_accounts(request={
        "ledger": "ledger001",
        "address": "users:.+",
        "metadata": {
            "0": "m",
            "1": "e",
            "2": "t",
            "3": "a",
            "4": "d",
            "5": "a",
            "6": "t",
            "7": "a",
            "8": "[",
            "9": "k",
            "10": "e",
            "11": "y",
            "12": "]",
            "13": "=",
            "14": "v",
            "15": "a",
            "16": "l",
            "17": "u",
            "18": "e",
            "19": "1",
            "20": "&",
            "21": "m",
            "22": "e",
            "23": "t",
            "24": "a",
            "25": "d",
            "26": "a",
            "27": "t",
            "28": "a",
            "29": "[",
            "30": "a",
            "31": ".",
            "32": "n",
            "33": "e",
            "34": "s",
            "35": "t",
            "36": "e",
            "37": "d",
            "38": ".",
            "39": "k",
            "40": "e",
            "41": "y",
            "42": "]",
            "43": "=",
            "44": "v",
            "45": "a",
            "46": "l",
            "47": "u",
            "48": "e",
            "49": "2",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CountAccountsRequest](../../models/operations/countaccountsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CountAccountsResponse](../../models/operations/countaccountsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.count_transactions(request={
        "ledger": "ledger001",
        "account": "users:001",
        "destination": "users:001",
        "metadata": {},
        "reference": "ref:001",
        "source": "users:001",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CountTransactionsRequest](../../models/operations/counttransactionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CountTransactionsResponse](../../models/operations/counttransactionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.create_transaction(request={
        "post_transaction": {
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
                {
                    "amount": 100,
                    "asset": "COIN",
                    "destination": "users:002",
                    "source": "users:001",
                },
            ],
            "reference": "ref:001",
            "script": {
                "plain": ("vars {\n"
                "account $user\n"
                "}\n"
                "send [COIN 10] (\n"
                "	source = @world\n"
                "	destination = $user\n"
                ")\n"
                ""),
                "vars": {
                    "user": "users:042",
                },
            },
        },
        "ledger": "ledger001",
        "preview": True,
    })

    assert res.transactions_response is not None

    # Handle response
    print(res.transactions_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateTransactionRequest](../../models/operations/createtransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateTransactionResponse](../../models/operations/createtransactionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.get_account(request={
        "address": "users:001",
        "ledger": "ledger001",
    })

    assert res.account_response is not None

    # Handle response
    print(res.account_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAccountRequest](../../models/operations/getaccountrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetAccountResponse](../../models/operations/getaccountresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## get_balances

Get the balances from a ledger's account

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

    res = sdk.ledger.v1.get_balances(request={
        "ledger": "ledger001",
        "address": "users:001",
        "after": "users:003",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    })

    assert res.balances_cursor_response is not None

    # Handle response
    print(res.balances_cursor_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetBalancesRequest](../../models/operations/getbalancesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetBalancesResponse](../../models/operations/getbalancesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.get_balances_aggregated(request={
        "ledger": "ledger001",
        "address": "users:001",
    })

    assert res.aggregate_balances_response is not None

    # Handle response
    print(res.aggregate_balances_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetBalancesAggregatedRequest](../../models/operations/getbalancesaggregatedrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetBalancesAggregatedResponse](../../models/operations/getbalancesaggregatedresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.get_info()

    assert res.config_info_response is not None

    # Handle response
    print(res.config_info_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetInfoResponse](../../models/operations/getinforesponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.get_ledger_info(request={
        "ledger": "ledger001",
    })

    assert res.ledger_info_response is not None

    # Handle response
    print(res.ledger_info_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLedgerInfoRequest](../../models/operations/getledgerinforequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetLedgerInfoResponse](../../models/operations/getledgerinforesponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## get_mapping

Get the mapping of a ledger

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

    res = sdk.ledger.v1.get_mapping(request={
        "ledger": "ledger001",
    })

    assert res.mapping_response is not None

    # Handle response
    print(res.mapping_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetMappingRequest](../../models/operations/getmappingrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetMappingResponse](../../models/operations/getmappingresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.get_transaction(request={
        "ledger": "ledger001",
        "txid": 1234,
    })

    assert res.transaction_response is not None

    # Handle response
    print(res.transaction_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTransactionRequest](../../models/operations/gettransactionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetTransactionResponse](../../models/operations/gettransactionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.list_accounts(request={
        "ledger": "ledger001",
        "address": "users:.+",
        "after": "users:003",
        "balance": 2400,
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "metadata": {
            "0": "m",
            "1": "e",
            "2": "t",
            "3": "a",
            "4": "d",
            "5": "a",
            "6": "t",
            "7": "a",
            "8": "[",
            "9": "k",
            "10": "e",
            "11": "y",
            "12": "]",
            "13": "=",
            "14": "v",
            "15": "a",
            "16": "l",
            "17": "u",
            "18": "e",
            "19": "1",
            "20": "&",
            "21": "m",
            "22": "e",
            "23": "t",
            "24": "a",
            "25": "d",
            "26": "a",
            "27": "t",
            "28": "a",
            "29": "[",
            "30": "a",
            "31": ".",
            "32": "n",
            "33": "e",
            "34": "s",
            "35": "t",
            "36": "e",
            "37": "d",
            "38": ".",
            "39": "k",
            "40": "e",
            "41": "y",
            "42": "]",
            "43": "=",
            "44": "v",
            "45": "a",
            "46": "l",
            "47": "u",
            "48": "e",
            "49": "2",
        },
        "page_size": 100,
        "pagination_token": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    })

    assert res.accounts_cursor_response is not None

    # Handle response
    print(res.accounts_cursor_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListAccountsRequest](../../models/operations/listaccountsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListAccountsResponse](../../models/operations/listaccountsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.list_logs(request={
        "ledger": "ledger001",
        "after": "1234",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.logs_cursor_response is not None

    # Handle response
    print(res.logs_cursor_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListLogsRequest](../../models/operations/listlogsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.ListLogsResponse](../../models/operations/listlogsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## list_transactions

List transactions from a ledger, sorted by txid in descending order.

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

    res = sdk.ledger.v1.list_transactions(request={
        "ledger": "ledger001",
        "account": "users:001",
        "after": "1234",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "destination": "users:001",
        "page_size": 100,
        "reference": "ref:001",
        "source": "users:001",
    })

    assert res.transactions_cursor_response is not None

    # Handle response
    print(res.transactions_cursor_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTransactionsRequest](../../models/operations/listtransactionsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListTransactionsResponse](../../models/operations/listtransactionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.read_stats(request={
        "ledger": "ledger001",
    })

    assert res.stats_response is not None

    # Handle response
    print(res.stats_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ReadStatsRequest](../../models/operations/readstatsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.ReadStatsResponse](../../models/operations/readstatsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

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

    res = sdk.ledger.v1.revert_transaction(request={
        "ledger": "ledger001",
        "txid": 1234,
    })

    assert res.transaction_response is not None

    # Handle response
    print(res.transaction_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RevertTransactionRequest](../../models/operations/reverttransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RevertTransactionResponse](../../models/operations/reverttransactionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## ~~run_script~~

This route is deprecated, and has been merged into `POST /{ledger}/transactions`.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

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

    res = sdk.ledger.v1.run_script(request={
        "script": {
            "plain": ("vars {\n"
            "account $user\n"
            "}\n"
            "send [COIN 10] (\n"
            "	source = @world\n"
            "	destination = $user\n"
            ")\n"
            ""),
            "reference": "order_1234",
            "vars": {
                "user": "users:042",
            },
        },
        "ledger": "ledger001",
        "preview": True,
    })

    assert res.script_response is not None

    # Handle response
    print(res.script_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.RunScriptRequest](../../models/operations/runscriptrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.RunScriptResponse](../../models/operations/runscriptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_mapping

Update the mapping of a ledger

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

    res = sdk.ledger.v1.update_mapping(request={
        "mapping": {
            "contracts": [
                {
                    "expr": {},
                    "account": "users:001",
                },
                {
                    "expr": {},
                    "account": "users:001",
                },
            ],
        },
        "ledger": "ledger001",
    })

    assert res.mapping_response is not None

    # Handle response
    print(res.mapping_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateMappingRequest](../../models/operations/updatemappingrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateMappingResponse](../../models/operations/updatemappingresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |