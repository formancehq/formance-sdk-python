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
* [v2_delete_ledger_metadata](#v2_delete_ledger_metadata) - Delete ledger metadata by key
* [v2_delete_transaction_metadata](#v2_delete_transaction_metadata) - Delete metadata by key
* [v2_get_account](#v2_get_account) - Get account by its address
* [v2_get_balances_aggregated](#v2_get_balances_aggregated) - Get the aggregated balances from selected accounts
* [v2_get_info](#v2_get_info) - Show server information
* [v2_get_ledger](#v2_get_ledger) - Get a ledger
* [v2_get_ledger_info](#v2_get_ledger_info) - Get information about a ledger
* [v2_get_transaction](#v2_get_transaction) - Get transaction from a ledger by its ID
* [v2_get_volumes_with_balances](#v2_get_volumes_with_balances) - Get list of volumes with balances for (account/asset)
* [v2_list_accounts](#v2_list_accounts) - List accounts from a ledger
* [v2_list_ledgers](#v2_list_ledgers) - List ledgers
* [v2_list_logs](#v2_list_logs) - List the logs from a ledger
* [v2_list_transactions](#v2_list_transactions) - List transactions from a ledger
* [v2_read_stats](#v2_read_stats) - Get statistics from a ledger
* [v2_revert_transaction](#v2_revert_transaction) - Revert a ledger transaction by its ID
* [v2_update_ledger_metadata](#v2_update_ledger_metadata) - Update ledger metadata

## create_transactions

Create a new batch of transactions to a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.create_transactions(request=operations.CreateTransactionsRequest(
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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## add_metadata_on_transaction

Set the metadata of a transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.add_metadata_on_transaction(request=operations.AddMetadataOnTransactionRequest(
    ledger='ledger001',
    txid=1234,
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## add_metadata_to_account

Add metadata to an account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.add_metadata_to_account(request=operations.AddMetadataToAccountRequest(
    request_body={
        'key': '<value>',
    },
    address='users:001',
    ledger='ledger001',
))

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
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## count_accounts

Count the accounts from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.count_accounts(request=operations.CountAccountsRequest(
    ledger='ledger001',
    address='users:.+',
    metadata={
        '0': 'm',
        '1': 'e',
        '2': 't',
        '3': 'a',
        '4': 'd',
        '5': 'a',
        '6': 't',
        '7': 'a',
        '8': '[',
        '9': 'k',
        '10': 'e',
        '11': 'y',
        '12': ']',
        '13': '=',
        '14': 'v',
        '15': 'a',
        '16': 'l',
        '17': 'u',
        '18': 'e',
        '19': '1',
        '20': '&',
        '21': 'm',
        '22': 'e',
        '23': 't',
        '24': 'a',
        '25': 'd',
        '26': 'a',
        '27': 't',
        '28': 'a',
        '29': '[',
        '30': 'a',
        '31': '.',
        '32': 'n',
        '33': 'e',
        '34': 's',
        '35': 't',
        '36': 'e',
        '37': 'd',
        '38': '.',
        '39': 'k',
        '40': 'e',
        '41': 'y',
        '42': ']',
        '43': '=',
        '44': 'v',
        '45': 'a',
        '46': 'l',
        '47': 'u',
        '48': 'e',
        '49': '2',
    },
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## count_transactions

Count the transactions from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.count_transactions(request=operations.CountTransactionsRequest(
    ledger='ledger001',
    account='users:001',
    destination='users:001',
    metadata=operations.Metadata(),
    reference='ref:001',
    source='users:001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## create_transaction

Create a new transaction to a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.create_transaction(request=operations.CreateTransactionRequest(
    post_transaction=shared.PostTransaction(
        postings=[
            shared.Posting(
                amount=100,
                asset='COIN',
                destination='users:002',
                source='users:001',
            ),
        ],
        reference='ref:001',
        script=shared.PostTransactionScript(
            plain='vars {
        account $user
        }
        send [COIN 10] (
        	source = @world
        	destination = $user
        )
        ',
            vars={
                'user': 'users:042',
            },
        ),
    ),
    ledger='ledger001',
    preview=True,
))

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
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_account

Get account by its address

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_account(request=operations.GetAccountRequest(
    address='users:001',
    ledger='ledger001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_balances

Get the balances from a ledger's account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_balances(request=operations.GetBalancesRequest(
    ledger='ledger001',
    address='users:001',
    after='users:003',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_balances_aggregated

Get the aggregated balances from selected accounts

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_balances_aggregated(request=operations.GetBalancesAggregatedRequest(
    ledger='ledger001',
    address='users:001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_info

Show server information

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_info()

if res.config_info_response is not None:
    # handle response
    pass

```


### Response

**[operations.GetInfoResponse](../../models/operations/getinforesponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_ledger_info

Get information about a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_ledger_info(request=operations.GetLedgerInfoRequest(
    ledger='ledger001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_mapping

Get the mapping of a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_mapping(request=operations.GetMappingRequest(
    ledger='ledger001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_transaction

Get transaction from a ledger by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.get_transaction(request=operations.GetTransactionRequest(
    ledger='ledger001',
    txid=1234,
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## list_accounts

List accounts from a ledger, sorted by address in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.list_accounts(request=operations.ListAccountsRequest(
    ledger='ledger001',
    address='users:.+',
    after='users:003',
    balance=2400,
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    metadata={
        '0': 'm',
        '1': 'e',
        '2': 't',
        '3': 'a',
        '4': 'd',
        '5': 'a',
        '6': 't',
        '7': 'a',
        '8': '[',
        '9': 'k',
        '10': 'e',
        '11': 'y',
        '12': ']',
        '13': '=',
        '14': 'v',
        '15': 'a',
        '16': 'l',
        '17': 'u',
        '18': 'e',
        '19': '1',
        '20': '&',
        '21': 'm',
        '22': 'e',
        '23': 't',
        '24': 'a',
        '25': 'd',
        '26': 'a',
        '27': 't',
        '28': 'a',
        '29': '[',
        '30': 'a',
        '31': '.',
        '32': 'n',
        '33': 'e',
        '34': 's',
        '35': 't',
        '36': 'e',
        '37': 'd',
        '38': '.',
        '39': 'k',
        '40': 'e',
        '41': 'y',
        '42': ']',
        '43': '=',
        '44': 'v',
        '45': 'a',
        '46': 'l',
        '47': 'u',
        '48': 'e',
        '49': '2',
    },
    page_size=100,
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## list_logs

List the logs from a ledger, sorted by ID in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.list_logs(request=operations.ListLogsRequest(
    ledger='ledger001',
    after='1234',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## list_transactions

List transactions from a ledger, sorted by txid in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.list_transactions(request=operations.ListTransactionsRequest(
    ledger='ledger001',
    account='users:001',
    after='1234',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    destination='users:001',
    page_size=100,
    reference='ref:001',
    source='users:001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## read_stats

Get statistics from a ledger. (aggregate metrics on accounts and transactions)


### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.read_stats(request=operations.ReadStatsRequest(
    ledger='ledger001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## revert_transaction

Revert a ledger transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.revert_transaction(request=operations.RevertTransactionRequest(
    ledger='ledger001',
    txid=1234,
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## ~~run_script~~

This route is deprecated, and has been merged into `POST /{ledger}/transactions`.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.run_script(request=operations.RunScriptRequest(
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
))

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
| errors.SDKError | 4xx-5xx         | */*             |

## update_mapping

Update the mapping of a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.update_mapping(request=operations.UpdateMappingRequest(
    mapping=shared.Mapping(
        contracts=[
            shared.Contract(
                expr=shared.Expr(),
                account='users:001',
            ),
        ],
    ),
    ledger='ledger001',
))

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

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | default              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## v2_add_metadata_on_transaction

Set the metadata of a transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_add_metadata_on_transaction(request=operations.V2AddMetadataOnTransactionRequest(
    id=1234,
    ledger='ledger001',
    request_body={
        'admin': 'true',
    },
    dry_run=True,
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_add_metadata_to_account

Add metadata to an account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_add_metadata_to_account(request=operations.V2AddMetadataToAccountRequest(
    request_body={
        'admin': 'true',
    },
    address='users:001',
    ledger='ledger001',
    dry_run=True,
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_count_accounts

Count the accounts from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_count_accounts(request=operations.V2CountAccountsRequest(
    ledger='ledger001',
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_count_transactions

Count the transactions from a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_count_transactions(request=operations.V2CountTransactionsRequest(
    ledger='ledger001',
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_create_bulk

Bulk request

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_create_bulk(request=operations.V2CreateBulkRequest(
    ledger='ledger001',
    request_body=[
        shared.V2BulkElementAddMetadata(
            action='<value>',
        ),
    ],
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_create_ledger

Create a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_create_ledger(request=operations.V2CreateLedgerRequest(
    ledger='ledger001',
    v2_create_ledger_request=shared.V2CreateLedgerRequest(
        metadata={
            'admin': 'true',
        },
    ),
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_create_transaction

Create a new transaction to a ledger

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_create_transaction(request=operations.V2CreateTransactionRequest(
    v2_post_transaction=shared.V2PostTransaction(
        metadata={
            'admin': 'true',
        },
        postings=[
            shared.V2Posting(
                amount=100,
                asset='COIN',
                destination='users:002',
                source='users:001',
            ),
        ],
        reference='ref:001',
        script=shared.V2PostTransactionScript(
            plain='vars {
        account $user
        }
        send [COIN 10] (
        	source = @world
        	destination = $user
        )
        ',
            vars={
                'user': 'users:042',
            },
        ),
    ),
    ledger='ledger001',
    dry_run=True,
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_delete_account_metadata

Delete metadata by key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_delete_account_metadata(request=operations.V2DeleteAccountMetadataRequest(
    address='3680 Emile Grove',
    key='foo',
    ledger='ledger001',
))

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
| errors.SDKError | 4xx-5xx         | */*             |

## v2_delete_ledger_metadata

Delete ledger metadata by key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_delete_ledger_metadata(request=operations.V2DeleteLedgerMetadataRequest(
    key='foo',
    ledger='ledger001',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V2DeleteLedgerMetadataRequest](../../models/operations/v2deleteledgermetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.V2DeleteLedgerMetadataResponse](../../models/operations/v2deleteledgermetadataresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_delete_transaction_metadata

Delete metadata by key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_delete_transaction_metadata(request=operations.V2DeleteTransactionMetadataRequest(
    id=1234,
    key='foo',
    ledger='ledger001',
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_account

Get account by its address

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_account(request=operations.V2GetAccountRequest(
    address='users:001',
    ledger='ledger001',
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_balances_aggregated

Get the aggregated balances from selected accounts

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_balances_aggregated(request=operations.V2GetBalancesAggregatedRequest(
    ledger='ledger001',
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_info

Show server information

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_info()

if res.v2_config_info_response is not None:
    # handle response
    pass

```


### Response

**[operations.V2GetInfoResponse](../../models/operations/v2getinforesponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_ledger

Get a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_ledger(request=operations.V2GetLedgerRequest(
    ledger='ledger001',
))

if res.v2_get_ledger_response is not None:
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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_ledger_info

Get information about a ledger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_ledger_info(request=operations.V2GetLedgerInfoRequest(
    ledger='ledger001',
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_transaction

Get transaction from a ledger by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_transaction(request=operations.V2GetTransactionRequest(
    id=1234,
    ledger='ledger001',
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_get_volumes_with_balances

Get list of volumes with balances for (account/asset)

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_get_volumes_with_balances(request=operations.V2GetVolumesWithBalancesRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    group_by=3,
    page_size=100,
))

if res.v2_volumes_with_balance_cursor_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V2GetVolumesWithBalancesRequest](../../models/operations/v2getvolumeswithbalancesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.V2GetVolumesWithBalancesResponse](../../models/operations/v2getvolumeswithbalancesresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_list_accounts

List accounts from a ledger, sorted by address in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_list_accounts(request=operations.V2ListAccountsRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_list_ledgers

List ledgers

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_list_ledgers(request=operations.V2ListLedgersRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_list_logs

List the logs from a ledger, sorted by ID in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_list_logs(request=operations.V2ListLogsRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_list_transactions

List transactions from a ledger, sorted by id in descending order.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_list_transactions(request=operations.V2ListTransactionsRequest(
    ledger='ledger001',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_read_stats

Get statistics from a ledger. (aggregate metrics on accounts and transactions)


### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_read_stats(request=operations.V2ReadStatsRequest(
    ledger='ledger001',
))

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

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_revert_transaction

Revert a ledger transaction by its ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_revert_transaction(request=operations.V2RevertTransactionRequest(
    id=1234,
    ledger='ledger001',
))

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
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |

## v2_update_ledger_metadata

Update ledger metadata

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.ledger.v2_update_ledger_metadata(request=operations.V2UpdateLedgerMetadataRequest(
    ledger='ledger001',
    request_body={
        'admin': 'true',
    },
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V2UpdateLedgerMetadataRequest](../../models/operations/v2updateledgermetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.V2UpdateLedgerMetadataResponse](../../models/operations/v2updateledgermetadataresponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4xx-5xx                | */*                    |
