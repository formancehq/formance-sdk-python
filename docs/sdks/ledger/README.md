# Ledger
(*ledger*)

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
* [v2_add_metadata_on_transaction](#v2_add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [v2_add_metadata_to_account](#v2_add_metadata_to_account) - Add metadata to an account
* [v2_count_accounts](#v2_count_accounts) - Count the accounts from a ledger
* [v2_count_transactions](#v2_count_transactions) - Count the transactions from a ledger
* [v2_create_bulk](#v2_create_bulk) - Bulk request
* [v2_create_ledger](#v2_create_ledger) - Create a ledger
* [v2_create_transaction](#v2_create_transaction) - Create a new transaction to a ledger
* [v2_delete_account_metadata](#v2_delete_account_metadata) - Delete metadata by key
* [v2_delete_transaction_metadata](#v2_delete_transaction_metadata) - Delete metadata by key
* [v2_get_account](#v2_get_account) - Get account by its address
* [v2_get_balances_aggregated](#v2_get_balances_aggregated) - Get the aggregated balances from selected accounts
* [v2_get_info](#v2_get_info) - Show server information
* [v2_get_ledger](#v2_get_ledger) - Get a ledger
* [v2_get_ledger_info](#v2_get_ledger_info) - Get information about a ledger
* [v2_get_transaction](#v2_get_transaction) - Get transaction from a ledger by its ID
* [v2_list_accounts](#v2_list_accounts) - List accounts from a ledger
* [v2_list_ledgers](#v2_list_ledgers) - List ledgers
* [v2_list_logs](#v2_list_logs) - List the logs from a ledger
* [v2_list_transactions](#v2_list_transactions) - List transactions from a ledger
* [v2_read_stats](#v2_read_stats) - Get statistics from a ledger
* [v2_revert_transaction](#v2_revert_transaction) - Revert a ledger transaction by its ID

## create_transactions

Create a new batch of transactions to a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.CreateTransactionsRequest(
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
)

res = s.ledger.create_transactions(req)

if res.transactions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateTransactionsRequest](../../models/operations/createtransactionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateTransactionsResponse](../../models/operations/createtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_metadata_on_transaction

Set the metadata of a transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.AddMetadataOnTransactionRequest(
    ledger='ledger001',
    txid=1234,
)

res = s.ledger.add_metadata_on_transaction(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.AddMetadataOnTransactionRequest](../../models/operations/addmetadataontransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.AddMetadataOnTransactionResponse](../../models/operations/addmetadataontransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_metadata_to_account

Add metadata to an account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.AddMetadataToAccountRequest(
    request_body={
        'key': '<value>',
    },
    address='users:001',
    ledger='ledger001',
)

res = s.ledger.add_metadata_to_account(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.AddMetadataToAccountRequest](../../models/operations/addmetadatatoaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.AddMetadataToAccountResponse](../../models/operations/addmetadatatoaccountresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,404              | application/json     |
| errors.SDKError      | 4x-5xx               | */*                  |

## count_accounts

Count the accounts from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.CountAccountsRequest(
    ledger='ledger001',
    address='users:.+',
)

res = s.ledger.count_accounts(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CountAccountsRequest](../../models/operations/countaccountsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CountAccountsResponse](../../models/operations/countaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## count_transactions

Count the transactions from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.CountTransactionsRequest(
    ledger='ledger001',
    account='users:001',
    destination='users:001',
    reference='ref:001',
    source='users:001',
)

res = s.ledger.count_transactions(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CountTransactionsRequest](../../models/operations/counttransactionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CountTransactionsResponse](../../models/operations/counttransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_transaction

Create a new transaction to a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.CreateTransactionRequest(
    post_transaction=shared.PostTransaction(
        reference='ref:001',
    ),
    ledger='ledger001',
    preview=True,
)

res = s.ledger.create_transaction(req)

if res.transactions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateTransactionRequest](../../models/operations/createtransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateTransactionResponse](../../models/operations/createtransactionresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4x-5xx               | */*                  |

## get_account

Get account by its address

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetAccountRequest(
    address='users:001',
    ledger='ledger001',
)

res = s.ledger.get_account(req)

if res.account_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAccountRequest](../../models/operations/getaccountrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetAccountResponse](../../models/operations/getaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_balances

Get the balances from a ledger's account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetBalancesRequest(
    ledger='ledger001',
    address='users:001',
    after='users:003',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.get_balances(req)

if res.balances_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetBalancesRequest](../../models/operations/getbalancesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetBalancesResponse](../../models/operations/getbalancesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_balances_aggregated

Get the aggregated balances from selected accounts

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetBalancesAggregatedRequest(
    ledger='ledger001',
    address='users:001',
)

res = s.ledger.get_balances_aggregated(req)

if res.aggregate_balances_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetBalancesAggregatedRequest](../../models/operations/getbalancesaggregatedrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetBalancesAggregatedResponse](../../models/operations/getbalancesaggregatedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_info

Show server information

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.ledger.get_info()

if res.config_info_response is not None:
    # handle response
    pass

```


### Response

**[operations.GetInfoResponse](../../models/operations/getinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ledger_info

Get information about a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetLedgerInfoRequest(
    ledger='ledger001',
)

res = s.ledger.get_ledger_info(req)

if res.ledger_info_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLedgerInfoRequest](../../models/operations/getledgerinforequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetLedgerInfoResponse](../../models/operations/getledgerinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_mapping

Get the mapping of a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetMappingRequest(
    ledger='ledger001',
)

res = s.ledger.get_mapping(req)

if res.mapping_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetMappingRequest](../../models/operations/getmappingrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetMappingResponse](../../models/operations/getmappingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_transaction

Get transaction from a ledger by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetTransactionRequest(
    ledger='ledger001',
    txid=1234,
)

res = s.ledger.get_transaction(req)

if res.transaction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTransactionRequest](../../models/operations/gettransactionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTransactionResponse](../../models/operations/gettransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounts

List accounts from a ledger, sorted by address in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListAccountsRequest(
    ledger='ledger001',
    address='users:.+',
    after='users:003',
    balance=2400,
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    pagination_token='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.list_accounts(req)

if res.accounts_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListAccountsRequest](../../models/operations/listaccountsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListAccountsResponse](../../models/operations/listaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_logs

List the logs from a ledger, sorted by ID in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListLogsRequest(
    ledger='ledger001',
    after='1234',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.list_logs(req)

if res.logs_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListLogsRequest](../../models/operations/listlogsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListLogsResponse](../../models/operations/listlogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_transactions

List transactions from a ledger, sorted by txid in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListTransactionsRequest(
    ledger='ledger001',
    account='users:001',
    after='1234',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    destination='users:001',
    reference='ref:001',
    source='users:001',
)

res = s.ledger.list_transactions(req)

if res.transactions_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTransactionsRequest](../../models/operations/listtransactionsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListTransactionsResponse](../../models/operations/listtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## read_stats

Get statistics from a ledger. (aggregate metrics on accounts and transactions)


### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ReadStatsRequest(
    ledger='ledger001',
)

res = s.ledger.read_stats(req)

if res.stats_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ReadStatsRequest](../../models/operations/readstatsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ReadStatsResponse](../../models/operations/readstatsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## revert_transaction

Revert a ledger transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.RevertTransactionRequest(
    ledger='ledger001',
    txid=1234,
)

res = s.ledger.revert_transaction(req)

if res.transaction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RevertTransactionRequest](../../models/operations/reverttransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RevertTransactionResponse](../../models/operations/reverttransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~run_script~~

This route is deprecated, and has been merged into `POST /{ledger}/transactions`.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.RunScriptRequest(
    script=shared.Script(
        plain='vars {
    account $user
    }
    send [COIN 10] (
    	source = @world
    	destination = $user
    )
    ',
        reference='order_1234',
        vars={
            'user': 'users:042',
        },
    ),
    ledger='ledger001',
    preview=True,
)

res = s.ledger.run_script(req)

if res.script_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.RunScriptRequest](../../models/operations/runscriptrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.RunScriptResponse](../../models/operations/runscriptresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_mapping

Update the mapping of a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.UpdateMappingRequest(
    mapping=shared.Mapping(
        contracts=[
            shared.Contract(
                expr=shared.Expr(),
                account='users:001',
            ),
        ],
    ),
    ledger='ledger001',
)

res = s.ledger.update_mapping(req)

if res.mapping_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateMappingRequest](../../models/operations/updatemappingrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateMappingResponse](../../models/operations/updatemappingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_add_metadata_on_transaction

Set the metadata of a transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2AddMetadataOnTransactionRequest(
    id=1234,
    ledger='ledger001',
    request_body={
        'admin': 'true',
    },
    dry_run=True,
)

res = s.ledger.v2_add_metadata_on_transaction(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V2AddMetadataOnTransactionRequest](../../models/operations/v2addmetadataontransactionrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.V2AddMetadataOnTransactionResponse](../../models/operations/v2addmetadataontransactionresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400,404                | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_add_metadata_to_account

Add metadata to an account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2AddMetadataToAccountRequest(
    request_body={
        'admin': 'true',
    },
    address='users:001',
    ledger='ledger001',
    dry_run=True,
)

res = s.ledger.v2_add_metadata_to_account(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V2AddMetadataToAccountRequest](../../models/operations/v2addmetadatatoaccountrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.V2AddMetadataToAccountResponse](../../models/operations/v2addmetadatatoaccountresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400,404                | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_count_accounts

Count the accounts from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2CountAccountsRequest(
    ledger='ledger001',
)

res = s.ledger.v2_count_accounts(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2CountAccountsRequest](../../models/operations/v2countaccountsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.V2CountAccountsResponse](../../models/operations/v2countaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_count_transactions

Count the transactions from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2CountTransactionsRequest(
    ledger='ledger001',
)

res = s.ledger.v2_count_transactions(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V2CountTransactionsRequest](../../models/operations/v2counttransactionsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.V2CountTransactionsResponse](../../models/operations/v2counttransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_create_bulk

Bulk request

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2CreateBulkRequest(
    ledger='ledger001',
)

res = s.ledger.v2_create_bulk(req)

if res.v2_bulk_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V2CreateBulkRequest](../../models/operations/v2createbulkrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.V2CreateBulkResponse](../../models/operations/v2createbulkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_create_ledger

Create a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2CreateLedgerRequest(
    ledger='ledger001',
)

res = s.ledger.v2_create_ledger(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V2CreateLedgerRequest](../../models/operations/v2createledgerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.V2CreateLedgerResponse](../../models/operations/v2createledgerresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400                    | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_create_transaction

Create a new transaction to a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2CreateTransactionRequest(
    v2_post_transaction=shared.V2PostTransaction(
        metadata={
            'admin': 'true',
        },
        reference='ref:001',
    ),
    ledger='ledger001',
    dry_run=True,
)

res = s.ledger.v2_create_transaction(req)

if res.v2_create_transaction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V2CreateTransactionRequest](../../models/operations/v2createtransactionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.V2CreateTransactionResponse](../../models/operations/v2createtransactionresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400                    | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_delete_account_metadata

Delete metadata by key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2DeleteAccountMetadataRequest(
    address='3680 Emile Grove',
    key='foo',
    ledger='ledger001',
)

res = s.ledger.v2_delete_account_metadata(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V2DeleteAccountMetadataRequest](../../models/operations/v2deleteaccountmetadatarequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.V2DeleteAccountMetadataResponse](../../models/operations/v2deleteaccountmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_delete_transaction_metadata

Delete metadata by key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2DeleteTransactionMetadataRequest(
    id=1234,
    key='foo',
    ledger='ledger001',
)

res = s.ledger.v2_delete_transaction_metadata(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.V2DeleteTransactionMetadataRequest](../../models/operations/v2deletetransactionmetadatarequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.V2DeleteTransactionMetadataResponse](../../models/operations/v2deletetransactionmetadataresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400                    | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_get_account

Get account by its address

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetAccountRequest(
    address='users:001',
    ledger='ledger001',
)

res = s.ledger.v2_get_account(req)

if res.v2_account_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V2GetAccountRequest](../../models/operations/v2getaccountrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.V2GetAccountResponse](../../models/operations/v2getaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_balances_aggregated

Get the aggregated balances from selected accounts

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetBalancesAggregatedRequest(
    ledger='ledger001',
)

res = s.ledger.v2_get_balances_aggregated(req)

if res.v2_aggregate_balances_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V2GetBalancesAggregatedRequest](../../models/operations/v2getbalancesaggregatedrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.V2GetBalancesAggregatedResponse](../../models/operations/v2getbalancesaggregatedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_info

Show server information

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.ledger.v2_get_info()

if res.v2_config_info_response is not None:
    # handle response
    pass

```


### Response

**[operations.V2GetInfoResponse](../../models/operations/v2getinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_ledger

Get a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetLedgerRequest(
    ledger='ledger001',
)

res = s.ledger.v2_get_ledger(req)

if res.v2_ledger is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V2GetLedgerRequest](../../models/operations/v2getledgerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.V2GetLedgerResponse](../../models/operations/v2getledgerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_ledger_info

Get information about a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetLedgerInfoRequest(
    ledger='ledger001',
)

res = s.ledger.v2_get_ledger_info(req)

if res.v2_ledger_info_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2GetLedgerInfoRequest](../../models/operations/v2getledgerinforequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.V2GetLedgerInfoResponse](../../models/operations/v2getledgerinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_transaction

Get transaction from a ledger by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetTransactionRequest(
    id=1234,
    ledger='ledger001',
)

res = s.ledger.v2_get_transaction(req)

if res.v2_get_transaction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V2GetTransactionRequest](../../models/operations/v2gettransactionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.V2GetTransactionResponse](../../models/operations/v2gettransactionresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 404                    | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_list_accounts

List accounts from a ledger, sorted by address in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ListAccountsRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.v2_list_accounts(req)

if res.v2_accounts_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V2ListAccountsRequest](../../models/operations/v2listaccountsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.V2ListAccountsResponse](../../models/operations/v2listaccountsresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400                    | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_list_ledgers

List ledgers

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ListLedgersRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.v2_list_ledgers(req)

if res.v2_ledger_list_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2ListLedgersRequest](../../models/operations/v2listledgersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.V2ListLedgersResponse](../../models/operations/v2listledgersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_list_logs

List the logs from a ledger, sorted by ID in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ListLogsRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.v2_list_logs(req)

if res.v2_logs_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.V2ListLogsRequest](../../models/operations/v2listlogsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.V2ListLogsResponse](../../models/operations/v2listlogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_list_transactions

List transactions from a ledger, sorted by id in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ListTransactionsRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.ledger.v2_list_transactions(req)

if res.v2_transactions_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V2ListTransactionsRequest](../../models/operations/v2listtransactionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.V2ListTransactionsResponse](../../models/operations/v2listtransactionsresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400,404                | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |

## v2_read_stats

Get statistics from a ledger. (aggregate metrics on accounts and transactions)


### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ReadStatsRequest(
    ledger='ledger001',
)

res = s.ledger.v2_read_stats(req)

if res.v2_stats_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V2ReadStatsRequest](../../models/operations/v2readstatsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.V2ReadStatsResponse](../../models/operations/v2readstatsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_revert_transaction

Revert a ledger transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2RevertTransactionRequest(
    id=1234,
    ledger='ledger001',
)

res = s.ledger.v2_revert_transaction(req)

if res.v2_revert_transaction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V2RevertTransactionRequest](../../models/operations/v2reverttransactionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.V2RevertTransactionResponse](../../models/operations/v2reverttransactionresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | 400                    | application/json       |
| errors.SDKError        | 4x-5xx                 | */*                    |
