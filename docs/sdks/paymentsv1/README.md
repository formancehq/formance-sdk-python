# PaymentsV1
(*payments.v1*)

## Overview

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
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v1.add_account_to_pool(request={
        "add_account_to_pool_request": {
            "account_id": "<id>",
        },
        "pool_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.AddAccountToPoolRequest](../../models/operations/addaccounttopoolrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.AddAccountToPoolResponse](../../models/operations/addaccounttopoolresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## connectors_transfer

Execute a transfer between two accounts.

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

    res = sdk.payments.v1.connectors_transfer(request={
        "transfer_request": {
            "amount": 100,
            "asset": "USD",
            "destination": "acct_1Gqj58KZcSIg2N2q",
            "source": "acct_1Gqj58KZcSIg2N2q",
        },
        "connector": shared.ConnectorEnum.GENERIC,
    })

    assert res.transfer_response is not None

    # Handle response
    print(res.transfer_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ConnectorsTransferRequest](../../models/operations/connectorstransferrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ConnectorsTransferResponse](../../models/operations/connectorstransferresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_account

Create an account

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
from formance_sdk_python.utils import parse_datetime


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v1.create_account(request={
        "connector_id": "<id>",
        "created_at": parse_datetime("2025-07-27T08:57:17.388Z"),
        "reference": "<value>",
        "type": shared.AccountType.UNKNOWN,
    })

    assert res.payments_account_response is not None

    # Handle response
    print(res.payments_account_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.AccountRequest](../../models/shared/accountrequest.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateAccountResponse](../../models/operations/createaccountresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_bank_account

Create a bank account in Payments and on the PSP.

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

    res = sdk.payments.v1.create_bank_account(request={
        "connector_id": "<id>",
        "country": "GB",
        "name": "My account",
    })

    assert res.bank_account_response is not None

    # Handle response
    print(res.bank_account_response)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.BankAccountRequest](../../models/shared/bankaccountrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.CreateBankAccountResponse](../../models/operations/createbankaccountresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_payment

Create a payment

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
from formance_sdk_python.utils import parse_datetime


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v1.create_payment(request={
        "amount": 100,
        "asset": "USD",
        "connector_id": "<id>",
        "created_at": parse_datetime("2025-08-26T06:29:11.777Z"),
        "reference": "<value>",
        "scheme": shared.PaymentScheme.RTP,
        "status": shared.PaymentStatus.REFUNDED_FAILURE,
        "type": shared.PaymentType.PAYOUT,
    })

    assert res.payment_response is not None

    # Handle response
    print(res.payment_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.PaymentRequest](../../models/shared/paymentrequest.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreatePaymentResponse](../../models/operations/createpaymentresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_pool

Create a Pool

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

    res = sdk.payments.v1.create_pool(request={
        "account_i_ds": [
            "<value 1>",
            "<value 2>",
        ],
        "name": "<value>",
    })

    assert res.pool_response is not None

    # Handle response
    print(res.pool_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.PoolRequest](../../models/shared/poolrequest.md)            | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreatePoolResponse](../../models/operations/createpoolresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_transfer_initiation

Create a transfer initiation

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
from formance_sdk_python.utils import parse_datetime


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v1.create_transfer_initiation(request={
        "amount": 83093,
        "asset": "USD",
        "description": "flowery yum keenly operating knavishly commemorate recent apropos",
        "destination_account_id": "<id>",
        "reference": "XXX",
        "scheduled_at": parse_datetime("2025-07-09T05:18:01.065Z"),
        "source_account_id": "<id>",
        "type": shared.TransferInitiationRequestType.TRANSFER,
        "validated": False,
    })

    assert res.transfer_initiation_response is not None

    # Handle response
    print(res.transfer_initiation_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.TransferInitiationRequest](../../models/shared/transferinitiationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateTransferInitiationResponse](../../models/operations/createtransferinitiationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_pool

Delete a pool by its id.

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

    res = sdk.payments.v1.delete_pool(request={
        "pool_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeletePoolRequest](../../models/operations/deletepoolrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.DeletePoolResponse](../../models/operations/deletepoolresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_transfer_initiation

Delete a transfer initiation by its id.

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

    res = sdk.payments.v1.delete_transfer_initiation(request={
        "transfer_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.DeleteTransferInitiationRequest](../../models/operations/deletetransferinitiationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.DeleteTransferInitiationResponse](../../models/operations/deletetransferinitiationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## forward_bank_account

Forward a bank account to a connector

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

    res = sdk.payments.v1.forward_bank_account(request={
        "forward_bank_account_request": {
            "connector_id": "<id>",
        },
        "bank_account_id": "XXX",
    })

    assert res.bank_account_response is not None

    # Handle response
    print(res.bank_account_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ForwardBankAccountRequest](../../models/operations/forwardbankaccountrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ForwardBankAccountResponse](../../models/operations/forwardbankaccountresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_account_balances

Get account balances

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

    res = sdk.payments.v1.get_account_balances(request={
        "account_id": "XXX",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "sort": [
            "date:asc",
            "status:desc",
        ],
    })

    assert res.balances_cursor is not None

    # Handle response
    print(res.balances_cursor)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountBalancesRequest](../../models/operations/getaccountbalancesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAccountBalancesResponse](../../models/operations/getaccountbalancesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_bank_account

Get a bank account created by user on Formance

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

    res = sdk.payments.v1.get_bank_account(request={
        "bank_account_id": "XXX",
    })

    assert res.bank_account_response is not None

    # Handle response
    print(res.bank_account_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetBankAccountRequest](../../models/operations/getbankaccountrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetBankAccountResponse](../../models/operations/getbankaccountresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## ~~get_connector_task~~

Get a specific task associated to the connector.

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

    res = sdk.payments.v1.get_connector_task(request={
        "connector": shared.ConnectorEnum.MONEYCORP,
        "task_id": "task1",
    })

    assert res.task_response is not None

    # Handle response
    print(res.task_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetConnectorTaskRequest](../../models/operations/getconnectortaskrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetConnectorTaskResponse](../../models/operations/getconnectortaskresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_connector_task_v1

Get a specific task associated to the connector.

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

    res = sdk.payments.v1.get_connector_task_v1(request={
        "connector": shared.ConnectorEnum.MODULR,
        "connector_id": "XXX",
        "task_id": "task1",
    })

    assert res.task_response is not None

    # Handle response
    print(res.task_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetConnectorTaskV1Request](../../models/operations/getconnectortaskv1request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetConnectorTaskV1Response](../../models/operations/getconnectortaskv1response.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_payment

Get a payment

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

    res = sdk.payments.v1.get_payment(request={
        "payment_id": "XXX",
    })

    assert res.payment_response is not None

    # Handle response
    print(res.payment_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetPaymentRequest](../../models/operations/getpaymentrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetPaymentResponse](../../models/operations/getpaymentresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_pool

Get a Pool

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

    res = sdk.payments.v1.get_pool(request={
        "pool_id": "XXX",
    })

    assert res.pool_response is not None

    # Handle response
    print(res.pool_response)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetPoolRequest](../../models/operations/getpoolrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.GetPoolResponse](../../models/operations/getpoolresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_pool_balances

Get pool balances

### Example Usage

```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared
from formance_sdk_python.utils import parse_datetime


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v1.get_pool_balances(request={
        "at": parse_datetime("2024-11-27T10:59:51.663Z"),
        "pool_id": "XXX",
    })

    assert res.pool_balances_response is not None

    # Handle response
    print(res.pool_balances_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetPoolBalancesRequest](../../models/operations/getpoolbalancesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetPoolBalancesResponse](../../models/operations/getpoolbalancesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_transfer_initiation

Get a transfer initiation

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

    res = sdk.payments.v1.get_transfer_initiation(request={
        "transfer_id": "XXX",
    })

    assert res.transfer_initiation_response is not None

    # Handle response
    print(res.transfer_initiation_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetTransferInitiationRequest](../../models/operations/gettransferinitiationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetTransferInitiationResponse](../../models/operations/gettransferinitiationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## install_connector

Install a connector by its name and config.

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

    res = sdk.payments.v1.install_connector(request={
        "connector_config": {
            "api_key": "XXX",
            "login_id": "XXX",
            "name": "My CurrencyCloud Account",
            "polling_period": "60s",
            "provider": "Currencycloud",
        },
        "connector": shared.ConnectorEnum.MANGOPAY,
    })

    assert res.connector_response is not None

    # Handle response
    print(res.connector_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.InstallConnectorRequest](../../models/operations/installconnectorrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.InstallConnectorResponse](../../models/operations/installconnectorresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_all_connectors

List all installed connectors.

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

    res = sdk.payments.v1.list_all_connectors()

    assert res.connectors_response is not None

    # Handle response
    print(res.connectors_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListAllConnectorsResponse](../../models/operations/listallconnectorsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_bank_accounts

List all bank accounts created by user on Formance.

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

    res = sdk.payments.v1.list_bank_accounts(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "sort": [
            "date:asc",
            "status:desc",
        ],
    })

    assert res.bank_accounts_cursor is not None

    # Handle response
    print(res.bank_accounts_cursor)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListBankAccountsRequest](../../models/operations/listbankaccountsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListBankAccountsResponse](../../models/operations/listbankaccountsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_configs_available_connectors

List the configs of each available connector.

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

    res = sdk.payments.v1.list_configs_available_connectors()

    assert res.connectors_configs_response is not None

    # Handle response
    print(res.connectors_configs_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListConfigsAvailableConnectorsResponse](../../models/operations/listconfigsavailableconnectorsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## ~~list_connector_tasks~~

List all tasks associated with this connector.

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

    res = sdk.payments.v1.list_connector_tasks(request={
        "connector": shared.ConnectorEnum.MODULR,
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.tasks_cursor is not None

    # Handle response
    print(res.tasks_cursor)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListConnectorTasksRequest](../../models/operations/listconnectortasksrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListConnectorTasksResponse](../../models/operations/listconnectortasksresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_connector_tasks_v1

List all tasks associated with this connector.

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

    res = sdk.payments.v1.list_connector_tasks_v1(request={
        "connector": shared.ConnectorEnum.WISE,
        "connector_id": "XXX",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.tasks_cursor is not None

    # Handle response
    print(res.tasks_cursor)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListConnectorTasksV1Request](../../models/operations/listconnectortasksv1request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListConnectorTasksV1Response](../../models/operations/listconnectortasksv1response.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_payments

List payments

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

    res = sdk.payments.v1.list_payments(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "sort": [
            "date:asc",
            "status:desc",
        ],
    })

    assert res.payments_cursor is not None

    # Handle response
    print(res.payments_cursor)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPaymentsRequest](../../models/operations/listpaymentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListPaymentsResponse](../../models/operations/listpaymentsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_pools

List Pools

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

    res = sdk.payments.v1.list_pools(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "sort": [
            "date:asc",
            "status:desc",
        ],
    })

    assert res.pools_cursor is not None

    # Handle response
    print(res.pools_cursor)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListPoolsRequest](../../models/operations/listpoolsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.ListPoolsResponse](../../models/operations/listpoolsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_transfer_initiations

List Transfer Initiations

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

    res = sdk.payments.v1.list_transfer_initiations(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "sort": [
            "date:asc",
            "status:desc",
        ],
    })

    assert res.transfer_initiations_cursor is not None

    # Handle response
    print(res.transfer_initiations_cursor)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTransferInitiationsRequest](../../models/operations/listtransferinitiationsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListTransferInitiationsResponse](../../models/operations/listtransferinitiationsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## paymentsget_account

Get an account

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

    res = sdk.payments.v1.paymentsget_account(request={
        "account_id": "XXX",
    })

    assert res.payments_account_response is not None

    # Handle response
    print(res.payments_account_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PaymentsgetAccountRequest](../../models/operations/paymentsgetaccountrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PaymentsgetAccountResponse](../../models/operations/paymentsgetaccountresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## paymentsget_server_info

Get server info

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

    res = sdk.payments.v1.paymentsget_server_info()

    assert res.server_info is not None

    # Handle response
    print(res.server_info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.PaymentsgetServerInfoResponse](../../models/operations/paymentsgetserverinforesponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## paymentslist_accounts

List accounts

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

    res = sdk.payments.v1.paymentslist_accounts(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "sort": [
            "date:asc",
            "status:desc",
        ],
    })

    assert res.accounts_cursor is not None

    # Handle response
    print(res.accounts_cursor)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PaymentslistAccountsRequest](../../models/operations/paymentslistaccountsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PaymentslistAccountsResponse](../../models/operations/paymentslistaccountsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## ~~read_connector_config~~

Read connector config

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

    res = sdk.payments.v1.read_connector_config(request={
        "connector": shared.ConnectorEnum.MODULR,
    })

    assert res.connector_config_response is not None

    # Handle response
    print(res.connector_config_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ReadConnectorConfigRequest](../../models/operations/readconnectorconfigrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ReadConnectorConfigResponse](../../models/operations/readconnectorconfigresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## read_connector_config_v1

Read connector config

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

    res = sdk.payments.v1.read_connector_config_v1(request={
        "connector": shared.ConnectorEnum.MANGOPAY,
        "connector_id": "XXX",
    })

    assert res.connector_config_response is not None

    # Handle response
    print(res.connector_config_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ReadConnectorConfigV1Request](../../models/operations/readconnectorconfigv1request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ReadConnectorConfigV1Response](../../models/operations/readconnectorconfigv1response.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## remove_account_from_pool

Remove an account from a pool by its id.

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

    res = sdk.payments.v1.remove_account_from_pool(request={
        "account_id": "XXX",
        "pool_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveAccountFromPoolRequest](../../models/operations/removeaccountfrompoolrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAccountFromPoolResponse](../../models/operations/removeaccountfrompoolresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## ~~reset_connector~~

Reset a connector by its name.
It will remove the connector and ALL PAYMENTS generated with it.


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

    res = sdk.payments.v1.reset_connector(request={
        "connector": shared.ConnectorEnum.WISE,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ResetConnectorRequest](../../models/operations/resetconnectorrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ResetConnectorResponse](../../models/operations/resetconnectorresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## reset_connector_v1

Reset a connector by its name.
It will remove the connector and ALL PAYMENTS generated with it.


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

    res = sdk.payments.v1.reset_connector_v1(request={
        "connector": shared.ConnectorEnum.WISE,
        "connector_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ResetConnectorV1Request](../../models/operations/resetconnectorv1request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ResetConnectorV1Response](../../models/operations/resetconnectorv1response.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## retry_transfer_initiation

Retry a failed transfer initiation

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

    res = sdk.payments.v1.retry_transfer_initiation(request={
        "transfer_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RetryTransferInitiationRequest](../../models/operations/retrytransferinitiationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RetryTransferInitiationResponse](../../models/operations/retrytransferinitiationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## reverse_transfer_initiation

Reverse transfer initiation

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

    res = sdk.payments.v1.reverse_transfer_initiation(request={
        "reverse_transfer_initiation_request": {
            "amount": 978875,
            "asset": "USD",
            "description": "whenever phooey a unlike tremendously whoever after when tight",
            "metadata": {
                "key": "<value>",
            },
            "reference": "XXX",
        },
        "transfer_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ReverseTransferInitiationRequest](../../models/operations/reversetransferinitiationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ReverseTransferInitiationResponse](../../models/operations/reversetransferinitiationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## udpate_transfer_initiation_status

Update a transfer initiation status

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

    res = sdk.payments.v1.udpate_transfer_initiation_status(request={
        "update_transfer_initiation_status_request": {
            "status": shared.Status.VALIDATED,
        },
        "transfer_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.UdpateTransferInitiationStatusRequest](../../models/operations/udpatetransferinitiationstatusrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.UdpateTransferInitiationStatusResponse](../../models/operations/udpatetransferinitiationstatusresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## ~~uninstall_connector~~

Uninstall a connector by its name.

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

    res = sdk.payments.v1.uninstall_connector(request={
        "connector": shared.ConnectorEnum.GENERIC,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UninstallConnectorRequest](../../models/operations/uninstallconnectorrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UninstallConnectorResponse](../../models/operations/uninstallconnectorresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## uninstall_connector_v1

Uninstall a connector by its name.

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

    res = sdk.payments.v1.uninstall_connector_v1(request={
        "connector": shared.ConnectorEnum.BANKING_CIRCLE,
        "connector_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UninstallConnectorV1Request](../../models/operations/uninstallconnectorv1request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UninstallConnectorV1Response](../../models/operations/uninstallconnectorv1response.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update_bank_account_metadata

Update metadata of a bank account

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

    res = sdk.payments.v1.update_bank_account_metadata(request={
        "update_bank_account_metadata_request": {
            "metadata": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
        },
        "bank_account_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateBankAccountMetadataRequest](../../models/operations/updatebankaccountmetadatarequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UpdateBankAccountMetadataResponse](../../models/operations/updatebankaccountmetadataresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update_connector_config_v1

Update connector config

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

    res = sdk.payments.v1.update_connector_config_v1(request={
        "connector_config": {
            "api_key": "XXX",
            "api_secret": "XXX",
            "name": "My Modulr Account",
            "polling_period": "60s",
            "provider": "Modulr",
        },
        "connector": shared.ConnectorEnum.MANGOPAY,
        "connector_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateConnectorConfigV1Request](../../models/operations/updateconnectorconfigv1request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateConnectorConfigV1Response](../../models/operations/updateconnectorconfigv1response.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update_metadata

Update metadata

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

    res = sdk.payments.v1.update_metadata(request={
        "request_body": {
            "key": "<value>",
        },
        "payment_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateMetadataRequest](../../models/operations/updatemetadatarequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateMetadataResponse](../../models/operations/updatemetadataresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |