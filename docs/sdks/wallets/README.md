# Wallets
(*wallets*)

### Available Operations

* [confirm_hold](#confirm_hold) - Confirm a hold
* [create_balance](#create_balance) - Create a balance
* [create_wallet](#create_wallet) - Create a new wallet
* [credit_wallet](#credit_wallet) - Credit a wallet
* [debit_wallet](#debit_wallet) - Debit a wallet
* [get_balance](#get_balance) - Get detailed balance
* [get_hold](#get_hold) - Get a hold
* [get_holds](#get_holds) - Get all holds for a wallet
* [get_transactions](#get_transactions)
* [get_wallet](#get_wallet) - Get a wallet
* [get_wallet_summary](#get_wallet_summary) - Get wallet summary
* [list_balances](#list_balances) - List balances of a wallet
* [list_wallets](#list_wallets) - List all wallets
* [update_wallet](#update_wallet) - Update a wallet
* [void_hold](#void_hold) - Cancel a hold
* [walletsget_server_info](#walletsget_server_info) - Get server info

## confirm_hold

Confirm a hold

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.confirm_hold(request=operations.ConfirmHoldRequest(
    hold_id='<value>',
    confirm_hold_request=shared.ConfirmHoldRequest(
        amount=100,
        final=True,
    ),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ConfirmHoldRequest](../../models/operations/confirmholdrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ConfirmHoldResponse](../../models/operations/confirmholdresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## create_balance

Create a balance

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.create_balance(request=operations.CreateBalanceRequest(
    id='<id>',
))

if res.create_balance_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateBalanceRequest](../../models/operations/createbalancerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateBalanceResponse](../../models/operations/createbalanceresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## create_wallet

Create a new wallet

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.create_wallet(request=shared.CreateWalletRequest(
    metadata={
        'key': '<value>',
    },
    name='<value>',
))

if res.create_wallet_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.CreateWalletRequest](../../models/shared/createwalletrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateWalletResponse](../../models/operations/createwalletresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## credit_wallet

Credit a wallet

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.credit_wallet(request=operations.CreditWalletRequest(
    id='<id>',
    credit_wallet_request=shared.CreditWalletRequest(
        amount=shared.Monetary(
            amount=100,
            asset='USD/2',
        ),
        metadata={
            'key': '',
        },
        sources=[
            shared.LedgerAccountSubject(
                identifier='<value>',
                type='<value>',
            ),
        ],
    ),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreditWalletRequest](../../models/operations/creditwalletrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreditWalletResponse](../../models/operations/creditwalletresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## debit_wallet

Debit a wallet

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.debit_wallet(request=operations.DebitWalletRequest(
    id='<id>',
    debit_wallet_request=shared.DebitWalletRequest(
        amount=shared.Monetary(
            amount=100,
            asset='USD/2',
        ),
        metadata={
            'key': '',
        },
        pending=True,
    ),
))

if res.debit_wallet_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.DebitWalletRequest](../../models/operations/debitwalletrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DebitWalletResponse](../../models/operations/debitwalletresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_balance

Get detailed balance

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.get_balance(request=operations.GetBalanceRequest(
    balance_name='<value>',
    id='<id>',
))

if res.get_balance_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetBalanceRequest](../../models/operations/getbalancerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetBalanceResponse](../../models/operations/getbalanceresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_hold

Get a hold

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.get_hold(request=operations.GetHoldRequest(
    hold_id='<value>',
))

if res.get_hold_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetHoldRequest](../../models/operations/getholdrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetHoldResponse](../../models/operations/getholdresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_holds

Get all holds for a wallet

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.get_holds(request=operations.GetHoldsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    metadata={
        'admin': 'true',
    },
    page_size=100,
    wallet_id='wallet1',
))

if res.get_holds_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetHoldsRequest](../../models/operations/getholdsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetHoldsResponse](../../models/operations/getholdsresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_transactions

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.get_transactions(request=operations.GetTransactionsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    wallet_id='wallet1',
))

if res.get_transactions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetTransactionsRequest](../../models/operations/gettransactionsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetTransactionsResponse](../../models/operations/gettransactionsresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_wallet

Get a wallet

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.get_wallet(request=operations.GetWalletRequest(
    id='<id>',
))

if res.get_wallet_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetWalletRequest](../../models/operations/getwalletrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetWalletResponse](../../models/operations/getwalletresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_wallet_summary

Get wallet summary

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.get_wallet_summary(request=operations.GetWalletSummaryRequest(
    id='<id>',
))

if res.get_wallet_summary_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetWalletSummaryRequest](../../models/operations/getwalletsummaryrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetWalletSummaryResponse](../../models/operations/getwalletsummaryresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## list_balances

List balances of a wallet

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.list_balances(request=operations.ListBalancesRequest(
    id='<id>',
))

if res.list_balances_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListBalancesRequest](../../models/operations/listbalancesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListBalancesResponse](../../models/operations/listbalancesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_wallets

List all wallets

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.list_wallets(request=operations.ListWalletsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    metadata={
        'admin': 'true',
    },
    name='wallet1',
    page_size=100,
))

if res.list_wallets_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListWalletsRequest](../../models/operations/listwalletsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListWalletsResponse](../../models/operations/listwalletsresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## update_wallet

Update a wallet

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.update_wallet(request=operations.UpdateWalletRequest(
    id='<id>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateWalletRequest](../../models/operations/updatewalletrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateWalletResponse](../../models/operations/updatewalletresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## void_hold

Cancel a hold

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.void_hold(request=operations.VoidHoldRequest(
    hold_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.VoidHoldRequest](../../models/operations/voidholdrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.VoidHoldResponse](../../models/operations/voidholdresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## walletsget_server_info

Get server info

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.wallets.walletsget_server_info()

if res.server_info is not None:
    # handle response
    pass

```


### Response

**[operations.WalletsgetServerInfoResponse](../../models/operations/walletsgetserverinforesponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.WalletsErrorResponse | default                     | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
