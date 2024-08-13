# Payments
(*payments*)

### Available Operations

* [add_account_to_pool](#add_account_to_pool) - Add an account to a pool
* [connectors_transfer](#connectors_transfer) - Transfer funds between Connector accounts
* [create_account](#create_account) - Create an account
* [create_bank_account](#create_bank_account) - Create a BankAccount in Payments and on the PSP
* [create_payment](#create_payment) - Create a payment
* [create_pool](#create_pool) - Create a Pool
* [create_transfer_initiation](#create_transfer_initiation) - Create a TransferInitiation
* [delete_pool](#delete_pool) - Delete a Pool
* [delete_transfer_initiation](#delete_transfer_initiation) - Delete a transfer initiation
* [forward_bank_account](#forward_bank_account) - Forward a bank account to a connector
* [get_account_balances](#get_account_balances) - Get account balances
* [get_bank_account](#get_bank_account) - Get a bank account created by user on Formance
* [~~get_connector_task~~](#get_connector_task) - Read a specific task of the connector :warning: **Deprecated**
* [get_connector_task_v1](#get_connector_task_v1) - Read a specific task of the connector
* [get_payment](#get_payment) - Get a payment
* [get_pool](#get_pool) - Get a Pool
* [get_pool_balances](#get_pool_balances) - Get pool balances
* [get_transfer_initiation](#get_transfer_initiation) - Get a transfer initiation
* [install_connector](#install_connector) - Install a connector
* [list_all_connectors](#list_all_connectors) - List all installed connectors
* [list_bank_accounts](#list_bank_accounts) - List bank accounts created by user on Formance
* [list_configs_available_connectors](#list_configs_available_connectors) - List the configs of each available connector
* [~~list_connector_tasks~~](#list_connector_tasks) - List tasks from a connector :warning: **Deprecated**
* [list_connector_tasks_v1](#list_connector_tasks_v1) - List tasks from a connector
* [list_payments](#list_payments) - List payments
* [list_pools](#list_pools) - List Pools
* [list_transfer_initiations](#list_transfer_initiations) - List Transfer Initiations
* [paymentsget_account](#paymentsget_account) - Get an account
* [paymentsget_server_info](#paymentsget_server_info) - Get server info
* [paymentslist_accounts](#paymentslist_accounts) - List accounts
* [~~read_connector_config~~](#read_connector_config) - Read the config of a connector :warning: **Deprecated**
* [read_connector_config_v1](#read_connector_config_v1) - Read the config of a connector
* [remove_account_from_pool](#remove_account_from_pool) - Remove an account from a pool
* [~~reset_connector~~](#reset_connector) - Reset a connector :warning: **Deprecated**
* [reset_connector_v1](#reset_connector_v1) - Reset a connector
* [retry_transfer_initiation](#retry_transfer_initiation) - Retry a failed transfer initiation
* [reverse_transfer_initiation](#reverse_transfer_initiation) - Reverse a transfer initiation
* [udpate_transfer_initiation_status](#udpate_transfer_initiation_status) - Update the status of a transfer initiation
* [~~uninstall_connector~~](#uninstall_connector) - Uninstall a connector :warning: **Deprecated**
* [uninstall_connector_v1](#uninstall_connector_v1) - Uninstall a connector
* [update_bank_account_metadata](#update_bank_account_metadata) - Update metadata of a bank account
* [update_connector_config_v1](#update_connector_config_v1) - Update the config of a connector
* [update_metadata](#update_metadata) - Update metadata

## add_account_to_pool

Add an account to a pool

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.add_account_to_pool(request=operations.AddAccountToPoolRequest(
    add_account_to_pool_request=shared.AddAccountToPoolRequest(
        account_id='<value>',
    ),
    pool_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.AddAccountToPoolRequest](../../models/operations/addaccounttopoolrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.AddAccountToPoolResponse](../../models/operations/addaccounttopoolresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## connectors_transfer

Execute a transfer between two accounts.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.connectors_transfer(request=operations.ConnectorsTransferRequest(
    transfer_request=shared.TransferRequest(
        amount=100,
        asset='USD',
        destination='acct_1Gqj58KZcSIg2N2q',
        source='acct_1Gqj58KZcSIg2N2q',
    ),
    connector=shared.Connector.BANKING_CIRCLE,
))

if res.transfer_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ConnectorsTransferRequest](../../models/operations/connectorstransferrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ConnectorsTransferResponse](../../models/operations/connectorstransferresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## create_account

Create an account

### Example Usage

```python
import dateutil.parser
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.create_account(request=shared.AccountRequest(
    connector_id='<value>',
    created_at=dateutil.parser.isoparse('2024-08-19T02:15:08.668Z'),
    reference='<value>',
    type=shared.AccountType.UNKNOWN,
))

if res.payments_account_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.AccountRequest](../../models/shared/accountrequest.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateAccountResponse](../../models/operations/createaccountresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## create_bank_account

Create a bank account in Payments and on the PSP.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.create_bank_account(request=shared.BankAccountRequest(
    connector_id='<value>',
    country='GB',
    name='My account',
))

if res.bank_account_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.BankAccountRequest](../../models/shared/bankaccountrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateBankAccountResponse](../../models/operations/createbankaccountresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## create_payment

Create a payment

### Example Usage

```python
import dateutil.parser
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.create_payment(request=shared.PaymentRequest(
    amount=100,
    asset='USD',
    connector_id='<value>',
    created_at=dateutil.parser.isoparse('2024-11-09T01:03:21.153Z'),
    reference='<value>',
    scheme=shared.PaymentScheme.GOOGLE_PAY,
    status=shared.PaymentStatus.DISPUTE_WON,
    type=shared.PaymentType.TRANSFER,
))

if res.payment_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.PaymentRequest](../../models/shared/paymentrequest.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreatePaymentResponse](../../models/operations/createpaymentresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## create_pool

Create a Pool

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.create_pool(request=shared.PoolRequest(
    account_i_ds=[
        '<value>',
    ],
    name='<value>',
))

if res.pool_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.PoolRequest](../../models/shared/poolrequest.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreatePoolResponse](../../models/operations/createpoolresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## create_transfer_initiation

Create a transfer initiation

### Example Usage

```python
import dateutil.parser
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.create_transfer_initiation(request=shared.TransferInitiationRequest(
    amount=256698,
    asset='USD',
    description='Multi-tiered incremental methodology',
    destination_account_id='<value>',
    reference='XXX',
    scheduled_at=dateutil.parser.isoparse('2023-05-04T22:47:54.364Z'),
    source_account_id='<value>',
    type=shared.TransferInitiationRequestType.TRANSFER,
    validated=False,
))

if res.transfer_initiation_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.TransferInitiationRequest](../../models/shared/transferinitiationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateTransferInitiationResponse](../../models/operations/createtransferinitiationresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## delete_pool

Delete a pool by its id.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.delete_pool(request=operations.DeletePoolRequest(
    pool_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeletePoolRequest](../../models/operations/deletepoolrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeletePoolResponse](../../models/operations/deletepoolresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## delete_transfer_initiation

Delete a transfer initiation by its id.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.delete_transfer_initiation(request=operations.DeleteTransferInitiationRequest(
    transfer_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.DeleteTransferInitiationRequest](../../models/operations/deletetransferinitiationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.DeleteTransferInitiationResponse](../../models/operations/deletetransferinitiationresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## forward_bank_account

Forward a bank account to a connector

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.forward_bank_account(request=operations.ForwardBankAccountRequest(
    forward_bank_account_request=shared.ForwardBankAccountRequest(
        connector_id='<value>',
    ),
    bank_account_id='XXX',
))

if res.bank_account_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ForwardBankAccountRequest](../../models/operations/forwardbankaccountrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ForwardBankAccountResponse](../../models/operations/forwardbankaccountresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_account_balances

Get account balances

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_account_balances(request=operations.GetAccountBalancesRequest(
    account_id='XXX',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    sort=[
        'date:asc',
        'status:desc',
    ],
))

if res.balances_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountBalancesRequest](../../models/operations/getaccountbalancesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAccountBalancesResponse](../../models/operations/getaccountbalancesresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_bank_account

Get a bank account created by user on Formance

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_bank_account(request=operations.GetBankAccountRequest(
    bank_account_id='XXX',
))

if res.bank_account_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetBankAccountRequest](../../models/operations/getbankaccountrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetBankAccountResponse](../../models/operations/getbankaccountresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## ~~get_connector_task~~

Get a specific task associated to the connector.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_connector_task(request=operations.GetConnectorTaskRequest(
    connector=shared.Connector.ADYEN,
    task_id='task1',
))

if res.task_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetConnectorTaskRequest](../../models/operations/getconnectortaskrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetConnectorTaskResponse](../../models/operations/getconnectortaskresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_connector_task_v1

Get a specific task associated to the connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_connector_task_v1(request=operations.GetConnectorTaskV1Request(
    connector=shared.Connector.BANKING_CIRCLE,
    connector_id='XXX',
    task_id='task1',
))

if res.task_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetConnectorTaskV1Request](../../models/operations/getconnectortaskv1request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetConnectorTaskV1Response](../../models/operations/getconnectortaskv1response.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_payment

Get a payment

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_payment(request=operations.GetPaymentRequest(
    payment_id='XXX',
))

if res.payment_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetPaymentRequest](../../models/operations/getpaymentrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetPaymentResponse](../../models/operations/getpaymentresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_pool

Get a Pool

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_pool(request=operations.GetPoolRequest(
    pool_id='XXX',
))

if res.pool_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetPoolRequest](../../models/operations/getpoolrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetPoolResponse](../../models/operations/getpoolresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_pool_balances

Get pool balances

### Example Usage

```python
import dateutil.parser
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_pool_balances(request=operations.GetPoolBalancesRequest(
    at=dateutil.parser.isoparse('2023-05-05T06:40:23.018Z'),
    pool_id='XXX',
))

if res.pool_balances_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetPoolBalancesRequest](../../models/operations/getpoolbalancesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetPoolBalancesResponse](../../models/operations/getpoolbalancesresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## get_transfer_initiation

Get a transfer initiation

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.get_transfer_initiation(request=operations.GetTransferInitiationRequest(
    transfer_id='XXX',
))

if res.transfer_initiation_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetTransferInitiationRequest](../../models/operations/gettransferinitiationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetTransferInitiationResponse](../../models/operations/gettransferinitiationresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## install_connector

Install a connector by its name and config.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.install_connector(request=operations.InstallConnectorRequest(
    connector_config=shared.WiseConfig(
        api_key='XXX',
        name='My Wise Account',
        polling_period='60s',
    ),
    connector=shared.Connector.ADYEN,
))

if res.connector_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.InstallConnectorRequest](../../models/operations/installconnectorrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.InstallConnectorResponse](../../models/operations/installconnectorresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_all_connectors

List all installed connectors.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_all_connectors()

if res.connectors_response is not None:
    # handle response
    pass

```




### Response

**[operations.ListAllConnectorsResponse](../../models/operations/listallconnectorsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_bank_accounts

List all bank accounts created by user on Formance.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_bank_accounts(request=operations.ListBankAccountsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    sort=[
        'date:asc',
        'status:desc',
    ],
))

if res.bank_accounts_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListBankAccountsRequest](../../models/operations/listbankaccountsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListBankAccountsResponse](../../models/operations/listbankaccountsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_configs_available_connectors

List the configs of each available connector.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_configs_available_connectors()

if res.connectors_configs_response is not None:
    # handle response
    pass

```




### Response

**[operations.ListConfigsAvailableConnectorsResponse](../../models/operations/listconfigsavailableconnectorsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## ~~list_connector_tasks~~

List all tasks associated with this connector.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_connector_tasks(request=operations.ListConnectorTasksRequest(
    connector=shared.Connector.MODULR,
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

if res.tasks_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListConnectorTasksRequest](../../models/operations/listconnectortasksrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ListConnectorTasksResponse](../../models/operations/listconnectortasksresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_connector_tasks_v1

List all tasks associated with this connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_connector_tasks_v1(request=operations.ListConnectorTasksV1Request(
    connector=shared.Connector.BANKING_CIRCLE,
    connector_id='XXX',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
))

if res.tasks_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListConnectorTasksV1Request](../../models/operations/listconnectortasksv1request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ListConnectorTasksV1Response](../../models/operations/listconnectortasksv1response.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_payments

List payments

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_payments(request=operations.ListPaymentsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    sort=[
        'date:asc',
        'status:desc',
    ],
))

if res.payments_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPaymentsRequest](../../models/operations/listpaymentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListPaymentsResponse](../../models/operations/listpaymentsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_pools

List Pools

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_pools(request=operations.ListPoolsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    sort=[
        'date:asc',
        'status:desc',
    ],
))

if res.pools_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListPoolsRequest](../../models/operations/listpoolsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListPoolsResponse](../../models/operations/listpoolsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## list_transfer_initiations

List Transfer Initiations

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.list_transfer_initiations(request=operations.ListTransferInitiationsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    sort=[
        'date:asc',
        'status:desc',
    ],
))

if res.transfer_initiations_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTransferInitiationsRequest](../../models/operations/listtransferinitiationsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListTransferInitiationsResponse](../../models/operations/listtransferinitiationsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## paymentsget_account

Get an account

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.paymentsget_account(request=operations.PaymentsgetAccountRequest(
    account_id='XXX',
))

if res.payments_account_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PaymentsgetAccountRequest](../../models/operations/paymentsgetaccountrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PaymentsgetAccountResponse](../../models/operations/paymentsgetaccountresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## paymentsget_server_info

Get server info

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.paymentsget_server_info()

if res.server_info is not None:
    # handle response
    pass

```




### Response

**[operations.PaymentsgetServerInfoResponse](../../models/operations/paymentsgetserverinforesponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## paymentslist_accounts

List accounts

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.paymentslist_accounts(request=operations.PaymentslistAccountsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    page_size=100,
    sort=[
        'date:asc',
        'status:desc',
    ],
))

if res.accounts_cursor is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PaymentslistAccountsRequest](../../models/operations/paymentslistaccountsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PaymentslistAccountsResponse](../../models/operations/paymentslistaccountsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## ~~read_connector_config~~

Read connector config

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.read_connector_config(request=operations.ReadConnectorConfigRequest(
    connector=shared.Connector.GENERIC,
))

if res.connector_config_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ReadConnectorConfigRequest](../../models/operations/readconnectorconfigrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ReadConnectorConfigResponse](../../models/operations/readconnectorconfigresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## read_connector_config_v1

Read connector config

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.read_connector_config_v1(request=operations.ReadConnectorConfigV1Request(
    connector=shared.Connector.CURRENCY_CLOUD,
    connector_id='XXX',
))

if res.connector_config_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ReadConnectorConfigV1Request](../../models/operations/readconnectorconfigv1request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ReadConnectorConfigV1Response](../../models/operations/readconnectorconfigv1response.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## remove_account_from_pool

Remove an account from a pool by its id.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.remove_account_from_pool(request=operations.RemoveAccountFromPoolRequest(
    account_id='XXX',
    pool_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveAccountFromPoolRequest](../../models/operations/removeaccountfrompoolrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.RemoveAccountFromPoolResponse](../../models/operations/removeaccountfrompoolresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## ~~reset_connector~~

Reset a connector by its name.
It will remove the connector and ALL PAYMENTS generated with it.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.reset_connector(request=operations.ResetConnectorRequest(
    connector=shared.Connector.ATLAR,
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ResetConnectorRequest](../../models/operations/resetconnectorrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ResetConnectorResponse](../../models/operations/resetconnectorresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## reset_connector_v1

Reset a connector by its name.
It will remove the connector and ALL PAYMENTS generated with it.


### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.reset_connector_v1(request=operations.ResetConnectorV1Request(
    connector=shared.Connector.GENERIC,
    connector_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ResetConnectorV1Request](../../models/operations/resetconnectorv1request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ResetConnectorV1Response](../../models/operations/resetconnectorv1response.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## retry_transfer_initiation

Retry a failed transfer initiation

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.retry_transfer_initiation(request=operations.RetryTransferInitiationRequest(
    transfer_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RetryTransferInitiationRequest](../../models/operations/retrytransferinitiationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RetryTransferInitiationResponse](../../models/operations/retrytransferinitiationresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## reverse_transfer_initiation

Reverse transfer initiation

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.reverse_transfer_initiation(request=operations.ReverseTransferInitiationRequest(
    reverse_transfer_initiation_request=shared.ReverseTransferInitiationRequest(
        amount=327549,
        asset='USD',
        description='Streamlined high-level local area network',
        metadata={
            'key': '<value>',
        },
        reference='XXX',
    ),
    transfer_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ReverseTransferInitiationRequest](../../models/operations/reversetransferinitiationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ReverseTransferInitiationResponse](../../models/operations/reversetransferinitiationresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## udpate_transfer_initiation_status

Update a transfer initiation status

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.udpate_transfer_initiation_status(request=operations.UdpateTransferInitiationStatusRequest(
    update_transfer_initiation_status_request=shared.UpdateTransferInitiationStatusRequest(
        status=shared.Status.VALIDATED,
    ),
    transfer_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.UdpateTransferInitiationStatusRequest](../../models/operations/udpatetransferinitiationstatusrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.UdpateTransferInitiationStatusResponse](../../models/operations/udpatetransferinitiationstatusresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## ~~uninstall_connector~~

Uninstall a connector by its name.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.uninstall_connector(request=operations.UninstallConnectorRequest(
    connector=shared.Connector.MODULR,
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UninstallConnectorRequest](../../models/operations/uninstallconnectorrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UninstallConnectorResponse](../../models/operations/uninstallconnectorresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## uninstall_connector_v1

Uninstall a connector by its name.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.uninstall_connector_v1(request=operations.UninstallConnectorV1Request(
    connector=shared.Connector.GENERIC,
    connector_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UninstallConnectorV1Request](../../models/operations/uninstallconnectorv1request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UninstallConnectorV1Response](../../models/operations/uninstallconnectorv1response.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## update_bank_account_metadata

Update metadata of a bank account

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.update_bank_account_metadata(request=operations.UpdateBankAccountMetadataRequest(
    update_bank_account_metadata_request=shared.UpdateBankAccountMetadataRequest(
        metadata={
            'key': '<value>',
        },
    ),
    bank_account_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateBankAccountMetadataRequest](../../models/operations/updatebankaccountmetadatarequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.UpdateBankAccountMetadataResponse](../../models/operations/updatebankaccountmetadataresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## update_connector_config_v1

Update connector config

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.update_connector_config_v1(request=operations.UpdateConnectorConfigV1Request(
    connector_config=shared.StripeConfig(
        api_key='XXX',
        name='My Stripe Account',
        page_size=50,
        polling_period='60s',
    ),
    connector=shared.Connector.STRIPE,
    connector_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateConnectorConfigV1Request](../../models/operations/updateconnectorconfigv1request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateConnectorConfigV1Response](../../models/operations/updateconnectorconfigv1response.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## update_metadata

Update metadata

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.payments.update_metadata(request=operations.UpdateMetadataRequest(
    request_body={
        'key': '<value>',
    },
    payment_id='XXX',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateMetadataRequest](../../models/operations/updatemetadatarequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateMetadataResponse](../../models/operations/updatemetadataresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |
