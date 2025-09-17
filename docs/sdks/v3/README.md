# V3
(*payments.v3*)

## Overview

### Available Operations

* [add_account_to_pool](#add_account_to_pool) - Add an account to a pool
* [add_bank_account_to_payment_service_user](#add_bank_account_to_payment_service_user) - Add a bank account to a payment service user
* [approve_payment_initiation](#approve_payment_initiation) - Approve a payment initiation
* [create_account](#create_account) - Create a formance account object. This object will not be forwarded to the connector. It is only used for internal purposes.

* [create_bank_account](#create_bank_account) - Create a formance bank account object. This object will not be forwarded to the connector until you called the forwardBankAccount method.

* [create_payment](#create_payment) - Create a formance payment object. This object will not be forwarded to the connector. It is only used for internal purposes.

* [create_payment_service_user](#create_payment_service_user) - Create a formance payment service user object
* [create_pool](#create_pool) - Create a formance pool object
* [delete_payment_initiation](#delete_payment_initiation) - Delete a payment initiation by ID
* [delete_pool](#delete_pool) - Delete a pool by ID
* [forward_bank_account](#forward_bank_account) - Forward a Bank Account to a PSP for creation
* [forward_payment_service_user_bank_account](#forward_payment_service_user_bank_account) - Forward a payment service user's bank account to a connector
* [get_account](#get_account) - Get an account by ID
* [get_account_balances](#get_account_balances) - Get account balances
* [get_bank_account](#get_bank_account) - Get a Bank Account by ID
* [get_connector_config](#get_connector_config) - Get a connector configuration by ID
* [get_connector_schedule](#get_connector_schedule) - Get a connector schedule by ID
* [get_payment](#get_payment) - Get a payment by ID
* [get_payment_initiation](#get_payment_initiation) - Get a payment initiation by ID
* [get_payment_service_user](#get_payment_service_user) - Get a payment service user by ID
* [get_pool](#get_pool) - Get a pool by ID
* [get_pool_balances](#get_pool_balances) - Get historical pool balances from a particular point in time
* [get_pool_balances_latest](#get_pool_balances_latest) - Get latest pool balances
* [get_task](#get_task) - Get a task and its result by ID
* [initiate_payment](#initiate_payment) - Initiate a payment
* [install_connector](#install_connector) - Install a connector
* [list_accounts](#list_accounts) - List all accounts
* [list_bank_accounts](#list_bank_accounts) - List all bank accounts
* [list_connector_configs](#list_connector_configs) - List all connector configurations
* [list_connector_schedule_instances](#list_connector_schedule_instances) - List all connector schedule instances
* [list_connector_schedules](#list_connector_schedules) - List all connector schedules
* [list_connectors](#list_connectors) - List all connectors
* [list_payment_initiation_adjustments](#list_payment_initiation_adjustments) - List all payment initiation adjustments
* [list_payment_initiation_related_payments](#list_payment_initiation_related_payments) - List all payments related to a payment initiation
* [list_payment_initiations](#list_payment_initiations) - List all payment initiations
* [list_payment_service_users](#list_payment_service_users) - List all payment service users
* [list_payments](#list_payments) - List all payments
* [list_pools](#list_pools) - List all pools
* [reject_payment_initiation](#reject_payment_initiation) - Reject a payment initiation
* [remove_account_from_pool](#remove_account_from_pool) - Remove an account from a pool
* [reset_connector](#reset_connector) - Reset a connector. Be aware that this will delete all data and stop all existing tasks like payment initiations and bank account creations.
* [retry_payment_initiation](#retry_payment_initiation) - Retry a payment initiation
* [reverse_payment_initiation](#reverse_payment_initiation) - Reverse a payment initiation
* [uninstall_connector](#uninstall_connector) - Uninstall a connector
* [update_bank_account_metadata](#update_bank_account_metadata) - Update a bank account's metadata
* [update_payment_metadata](#update_payment_metadata) - Update a payment's metadata
* [v3_update_connector_config](#v3_update_connector_config) - Update the config of a connector

## add_account_to_pool

Add an account to a pool

### Example Usage

<!-- UsageSnippet language="python" operationID="v3AddAccountToPool" method="post" path="/api/payments/v3/pools/{poolID}/accounts/{accountID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.add_account_to_pool(request={
        "account_id": "<id>",
        "pool_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V3AddAccountToPoolRequest](../../models/operations/v3addaccounttopoolrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.V3AddAccountToPoolResponse](../../models/operations/v3addaccounttopoolresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## add_bank_account_to_payment_service_user

Add a bank account to a payment service user

### Example Usage

<!-- UsageSnippet language="python" operationID="v3AddBankAccountToPaymentServiceUser" method="post" path="/api/payments/v3/payment-service-users/{paymentServiceUserID}/bank-accounts/{bankAccountID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.add_bank_account_to_payment_service_user(request={
        "bank_account_id": "<id>",
        "payment_service_user_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.V3AddBankAccountToPaymentServiceUserRequest](../../models/operations/v3addbankaccounttopaymentserviceuserrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.V3AddBankAccountToPaymentServiceUserResponse](../../models/operations/v3addbankaccounttopaymentserviceuserresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## approve_payment_initiation

Approve a payment initiation

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ApprovePaymentInitiation" method="post" path="/api/payments/v3/payment-initiations/{paymentInitiationID}/approve" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.approve_payment_initiation(request={
        "payment_initiation_id": "<id>",
    })

    assert res.v3_approve_payment_initiation_response is not None

    # Handle response
    print(res.v3_approve_payment_initiation_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V3ApprovePaymentInitiationRequest](../../models/operations/v3approvepaymentinitiationrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.V3ApprovePaymentInitiationResponse](../../models/operations/v3approvepaymentinitiationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_account

Create a formance account object. This object will not be forwarded to the connector. It is only used for internal purposes.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreateAccount" method="post" path="/api/payments/v3/accounts" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.create_account()

    assert res.v3_create_account_response is not None

    # Handle response
    print(res.v3_create_account_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.V3CreateAccountRequest](../../models/shared/v3createaccountrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V3CreateAccountResponse](../../models/operations/v3createaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_bank_account

Create a formance bank account object. This object will not be forwarded to the connector until you called the forwardBankAccount method.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreateBankAccount" method="post" path="/api/payments/v3/bank-accounts" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.create_bank_account()

    assert res.v3_create_bank_account_response is not None

    # Handle response
    print(res.v3_create_bank_account_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.V3CreateBankAccountRequest](../../models/shared/v3createbankaccountrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V3CreateBankAccountResponse](../../models/operations/v3createbankaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_payment

Create a formance payment object. This object will not be forwarded to the connector. It is only used for internal purposes.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreatePayment" method="post" path="/api/payments/v3/payments" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.create_payment()

    assert res.v3_create_payment_response is not None

    # Handle response
    print(res.v3_create_payment_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.V3CreatePaymentRequest](../../models/shared/v3createpaymentrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V3CreatePaymentResponse](../../models/operations/v3createpaymentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_payment_service_user

Create a formance payment service user object

### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreatePaymentServiceUser" method="post" path="/api/payments/v3/payment-service-users" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.create_payment_service_user()

    assert res.v3_create_payment_service_user_response is not None

    # Handle response
    print(res.v3_create_payment_service_user_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.V3CreatePaymentServiceUserRequest](../../models/shared/v3createpaymentserviceuserrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3CreatePaymentServiceUserResponse](../../models/operations/v3createpaymentserviceuserresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## create_pool

Create a formance pool object

### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreatePool" method="post" path="/api/payments/v3/pools" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.create_pool()

    assert res.v3_create_pool_response is not None

    # Handle response
    print(res.v3_create_pool_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.V3CreatePoolRequest](../../models/shared/v3createpoolrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.V3CreatePoolResponse](../../models/operations/v3createpoolresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## delete_payment_initiation

Delete a payment initiation by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeletePaymentInitiation" method="delete" path="/api/payments/v3/payment-initiations/{paymentInitiationID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.delete_payment_initiation(request={
        "payment_initiation_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V3DeletePaymentInitiationRequest](../../models/operations/v3deletepaymentinitiationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.V3DeletePaymentInitiationResponse](../../models/operations/v3deletepaymentinitiationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## delete_pool

Delete a pool by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeletePool" method="delete" path="/api/payments/v3/pools/{poolID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.delete_pool(request={
        "pool_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V3DeletePoolRequest](../../models/operations/v3deletepoolrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V3DeletePoolResponse](../../models/operations/v3deletepoolresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## forward_bank_account

Forward a Bank Account to a PSP for creation

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ForwardBankAccount" method="post" path="/api/payments/v3/bank-accounts/{bankAccountID}/forward" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.forward_bank_account(request={
        "bank_account_id": "<id>",
    })

    assert res.v3_forward_bank_account_response is not None

    # Handle response
    print(res.v3_forward_bank_account_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3ForwardBankAccountRequest](../../models/operations/v3forwardbankaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3ForwardBankAccountResponse](../../models/operations/v3forwardbankaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## forward_payment_service_user_bank_account

Forward a payment service user's bank account to a connector

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ForwardPaymentServiceUserBankAccount" method="post" path="/api/payments/v3/payment-service-users/{paymentServiceUserID}/bank-accounts/{bankAccountID}/forward" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.forward_payment_service_user_bank_account(request={
        "bank_account_id": "<id>",
        "payment_service_user_id": "<id>",
    })

    assert res.v3_forward_payment_service_user_bank_account_response is not None

    # Handle response
    print(res.v3_forward_payment_service_user_bank_account_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.V3ForwardPaymentServiceUserBankAccountRequest](../../models/operations/v3forwardpaymentserviceuserbankaccountrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.V3ForwardPaymentServiceUserBankAccountResponse](../../models/operations/v3forwardpaymentserviceuserbankaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_account

Get an account by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetAccount" method="get" path="/api/payments/v3/accounts/{accountID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_account(request={
        "account_id": "<id>",
    })

    assert res.v3_get_account_response is not None

    # Handle response
    print(res.v3_get_account_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V3GetAccountRequest](../../models/operations/v3getaccountrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V3GetAccountResponse](../../models/operations/v3getaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_account_balances

Get account balances

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetAccountBalances" method="get" path="/api/payments/v3/accounts/{accountID}/balances" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_account_balances(request={
        "account_id": "<id>",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_balances_cursor_response is not None

    # Handle response
    print(res.v3_balances_cursor_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3GetAccountBalancesRequest](../../models/operations/v3getaccountbalancesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3GetAccountBalancesResponse](../../models/operations/v3getaccountbalancesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_bank_account

Get a Bank Account by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetBankAccount" method="get" path="/api/payments/v3/bank-accounts/{bankAccountID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_bank_account(request={
        "bank_account_id": "<id>",
    })

    assert res.v3_get_bank_account_response is not None

    # Handle response
    print(res.v3_get_bank_account_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V3GetBankAccountRequest](../../models/operations/v3getbankaccountrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V3GetBankAccountResponse](../../models/operations/v3getbankaccountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_connector_config

Get a connector configuration by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetConnectorConfig" method="get" path="/api/payments/v3/connectors/{connectorID}/config" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_connector_config(request={
        "connector_id": "<id>",
    })

    assert res.v3_get_connector_config_response is not None

    # Handle response
    print(res.v3_get_connector_config_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3GetConnectorConfigRequest](../../models/operations/v3getconnectorconfigrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3GetConnectorConfigResponse](../../models/operations/v3getconnectorconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_connector_schedule

Get a connector schedule by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetConnectorSchedule" method="get" path="/api/payments/v3/connectors/{connectorID}/schedules/{scheduleID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_connector_schedule(request={
        "connector_id": "<id>",
        "schedule_id": "<id>",
    })

    assert res.v3_connector_schedule_response is not None

    # Handle response
    print(res.v3_connector_schedule_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3GetConnectorScheduleRequest](../../models/operations/v3getconnectorschedulerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3GetConnectorScheduleResponse](../../models/operations/v3getconnectorscheduleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_payment

Get a payment by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetPayment" method="get" path="/api/payments/v3/payments/{paymentID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_payment(request={
        "payment_id": "<id>",
    })

    assert res.v3_get_payment_response is not None

    # Handle response
    print(res.v3_get_payment_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V3GetPaymentRequest](../../models/operations/v3getpaymentrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V3GetPaymentResponse](../../models/operations/v3getpaymentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_payment_initiation

Get a payment initiation by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetPaymentInitiation" method="get" path="/api/payments/v3/payment-initiations/{paymentInitiationID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_payment_initiation(request={
        "payment_initiation_id": "<id>",
    })

    assert res.v3_get_payment_initiation_response is not None

    # Handle response
    print(res.v3_get_payment_initiation_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3GetPaymentInitiationRequest](../../models/operations/v3getpaymentinitiationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3GetPaymentInitiationResponse](../../models/operations/v3getpaymentinitiationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_payment_service_user

Get a payment service user by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetPaymentServiceUser" method="get" path="/api/payments/v3/payment-service-users/{paymentServiceUserID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_payment_service_user(request={
        "payment_service_user_id": "<id>",
    })

    assert res.v3_get_payment_service_user_response is not None

    # Handle response
    print(res.v3_get_payment_service_user_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3GetPaymentServiceUserRequest](../../models/operations/v3getpaymentserviceuserrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3GetPaymentServiceUserResponse](../../models/operations/v3getpaymentserviceuserresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_pool

Get a pool by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetPool" method="get" path="/api/payments/v3/pools/{poolID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_pool(request={
        "pool_id": "<id>",
    })

    assert res.v3_get_pool_response is not None

    # Handle response
    print(res.v3_get_pool_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.V3GetPoolRequest](../../models/operations/v3getpoolrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.V3GetPoolResponse](../../models/operations/v3getpoolresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_pool_balances

Get historical pool balances from a particular point in time

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetPoolBalances" method="get" path="/api/payments/v3/pools/{poolID}/balances" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_pool_balances(request={
        "pool_id": "<id>",
    })

    assert res.v3_pool_balances_response is not None

    # Handle response
    print(res.v3_pool_balances_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetPoolBalancesRequest](../../models/operations/v3getpoolbalancesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetPoolBalancesResponse](../../models/operations/v3getpoolbalancesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_pool_balances_latest

Get latest pool balances

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetPoolBalancesLatest" method="get" path="/api/payments/v3/pools/{poolID}/balances/latest" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_pool_balances_latest(request={
        "pool_id": "<id>",
    })

    assert res.v3_pool_balances_response is not None

    # Handle response
    print(res.v3_pool_balances_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3GetPoolBalancesLatestRequest](../../models/operations/v3getpoolbalanceslatestrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3GetPoolBalancesLatestResponse](../../models/operations/v3getpoolbalanceslatestresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_task

Get a task and its result by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetTask" method="get" path="/api/payments/v3/tasks/{taskID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.get_task(request={
        "task_id": "<id>",
    })

    assert res.v3_get_task_response is not None

    # Handle response
    print(res.v3_get_task_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.V3GetTaskRequest](../../models/operations/v3gettaskrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.V3GetTaskResponse](../../models/operations/v3gettaskresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## initiate_payment

Initiate a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="v3InitiatePayment" method="post" path="/api/payments/v3/payment-initiations" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.initiate_payment(request={})

    assert res.v3_initiate_payment_response is not None

    # Handle response
    print(res.v3_initiate_payment_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3InitiatePaymentRequest](../../models/operations/v3initiatepaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3InitiatePaymentResponse](../../models/operations/v3initiatepaymentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## install_connector

Install a connector

### Example Usage

<!-- UsageSnippet language="python" operationID="v3InstallConnector" method="post" path="/api/payments/v3/connectors/install/{connector}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.install_connector(request={
        "connector": "<value>",
    })

    assert res.v3_install_connector_response is not None

    # Handle response
    print(res.v3_install_connector_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V3InstallConnectorRequest](../../models/operations/v3installconnectorrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.V3InstallConnectorResponse](../../models/operations/v3installconnectorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_accounts

List all accounts

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListAccounts" method="get" path="/api/payments/v3/accounts" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_accounts(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_accounts_cursor_response is not None

    # Handle response
    print(res.v3_accounts_cursor_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V3ListAccountsRequest](../../models/operations/v3listaccountsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.V3ListAccountsResponse](../../models/operations/v3listaccountsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_bank_accounts

List all bank accounts

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListBankAccounts" method="get" path="/api/payments/v3/bank-accounts" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_bank_accounts(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_bank_accounts_cursor_response is not None

    # Handle response
    print(res.v3_bank_accounts_cursor_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V3ListBankAccountsRequest](../../models/operations/v3listbankaccountsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.V3ListBankAccountsResponse](../../models/operations/v3listbankaccountsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_connector_configs

List all connector configurations

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListConnectorConfigs" method="get" path="/api/payments/v3/connectors/configs" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_connector_configs()

    assert res.v3_connector_configs_response is not None

    # Handle response
    print(res.v3_connector_configs_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.V3ListConnectorConfigsResponse](../../models/operations/v3listconnectorconfigsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_connector_schedule_instances

List all connector schedule instances

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListConnectorScheduleInstances" method="get" path="/api/payments/v3/connectors/{connectorID}/schedules/{scheduleID}/instances" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_connector_schedule_instances(request={
        "connector_id": "<id>",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "schedule_id": "<id>",
    })

    assert res.v3_connector_schedule_instances_cursor_response is not None

    # Handle response
    print(res.v3_connector_schedule_instances_cursor_response)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.V3ListConnectorScheduleInstancesRequest](../../models/operations/v3listconnectorscheduleinstancesrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.V3ListConnectorScheduleInstancesResponse](../../models/operations/v3listconnectorscheduleinstancesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_connector_schedules

List all connector schedules

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListConnectorSchedules" method="get" path="/api/payments/v3/connectors/{connectorID}/schedules" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_connector_schedules(request={
        "connector_id": "<id>",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_connector_schedules_cursor_response is not None

    # Handle response
    print(res.v3_connector_schedules_cursor_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V3ListConnectorSchedulesRequest](../../models/operations/v3listconnectorschedulesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.V3ListConnectorSchedulesResponse](../../models/operations/v3listconnectorschedulesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_connectors

List all connectors

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListConnectors" method="get" path="/api/payments/v3/connectors" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_connectors(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_connectors_cursor_response is not None

    # Handle response
    print(res.v3_connectors_cursor_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V3ListConnectorsRequest](../../models/operations/v3listconnectorsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V3ListConnectorsResponse](../../models/operations/v3listconnectorsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_payment_initiation_adjustments

List all payment initiation adjustments

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPaymentInitiationAdjustments" method="get" path="/api/payments/v3/payment-initiations/{paymentInitiationID}/adjustments" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_payment_initiation_adjustments(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "payment_initiation_id": "<id>",
    })

    assert res.v3_payment_initiation_adjustments_cursor_response is not None

    # Handle response
    print(res.v3_payment_initiation_adjustments_cursor_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.V3ListPaymentInitiationAdjustmentsRequest](../../models/operations/v3listpaymentinitiationadjustmentsrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.V3ListPaymentInitiationAdjustmentsResponse](../../models/operations/v3listpaymentinitiationadjustmentsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_payment_initiation_related_payments

List all payments related to a payment initiation

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPaymentInitiationRelatedPayments" method="get" path="/api/payments/v3/payment-initiations/{paymentInitiationID}/payments" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_payment_initiation_related_payments(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "payment_initiation_id": "<id>",
    })

    assert res.v3_payment_initiation_related_payments_cursor_response is not None

    # Handle response
    print(res.v3_payment_initiation_related_payments_cursor_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.V3ListPaymentInitiationRelatedPaymentsRequest](../../models/operations/v3listpaymentinitiationrelatedpaymentsrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.V3ListPaymentInitiationRelatedPaymentsResponse](../../models/operations/v3listpaymentinitiationrelatedpaymentsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_payment_initiations

List all payment initiations

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPaymentInitiations" method="get" path="/api/payments/v3/payment-initiations" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_payment_initiations(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_payment_initiations_cursor_response is not None

    # Handle response
    print(res.v3_payment_initiations_cursor_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V3ListPaymentInitiationsRequest](../../models/operations/v3listpaymentinitiationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.V3ListPaymentInitiationsResponse](../../models/operations/v3listpaymentinitiationsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_payment_service_users

List all payment service users

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPaymentServiceUsers" method="get" path="/api/payments/v3/payment-service-users" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_payment_service_users(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_payment_service_users_cursor_response is not None

    # Handle response
    print(res.v3_payment_service_users_cursor_response)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V3ListPaymentServiceUsersRequest](../../models/operations/v3listpaymentserviceusersrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.V3ListPaymentServiceUsersResponse](../../models/operations/v3listpaymentserviceusersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_payments

List all payments

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPayments" method="get" path="/api/payments/v3/payments" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_payments(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_payments_cursor_response is not None

    # Handle response
    print(res.v3_payments_cursor_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V3ListPaymentsRequest](../../models/operations/v3listpaymentsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.V3ListPaymentsResponse](../../models/operations/v3listpaymentsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## list_pools

List all pools

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPools" method="get" path="/api/payments/v3/pools" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.list_pools(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v3_pools_cursor_response is not None

    # Handle response
    print(res.v3_pools_cursor_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V3ListPoolsRequest](../../models/operations/v3listpoolsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V3ListPoolsResponse](../../models/operations/v3listpoolsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## reject_payment_initiation

Reject a payment initiation

### Example Usage

<!-- UsageSnippet language="python" operationID="v3RejectPaymentInitiation" method="post" path="/api/payments/v3/payment-initiations/{paymentInitiationID}/reject" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.reject_payment_initiation(request={
        "payment_initiation_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V3RejectPaymentInitiationRequest](../../models/operations/v3rejectpaymentinitiationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.V3RejectPaymentInitiationResponse](../../models/operations/v3rejectpaymentinitiationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## remove_account_from_pool

Remove an account from a pool

### Example Usage

<!-- UsageSnippet language="python" operationID="v3RemoveAccountFromPool" method="delete" path="/api/payments/v3/pools/{poolID}/accounts/{accountID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.remove_account_from_pool(request={
        "account_id": "<id>",
        "pool_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3RemoveAccountFromPoolRequest](../../models/operations/v3removeaccountfrompoolrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3RemoveAccountFromPoolResponse](../../models/operations/v3removeaccountfrompoolresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## reset_connector

Reset a connector. Be aware that this will delete all data and stop all existing tasks like payment initiations and bank account creations.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ResetConnector" method="post" path="/api/payments/v3/connectors/{connectorID}/reset" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.reset_connector(request={
        "connector_id": "<id>",
    })

    assert res.v3_reset_connector_response is not None

    # Handle response
    print(res.v3_reset_connector_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V3ResetConnectorRequest](../../models/operations/v3resetconnectorrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V3ResetConnectorResponse](../../models/operations/v3resetconnectorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## retry_payment_initiation

Retry a payment initiation

### Example Usage

<!-- UsageSnippet language="python" operationID="v3RetryPaymentInitiation" method="post" path="/api/payments/v3/payment-initiations/{paymentInitiationID}/retry" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.retry_payment_initiation(request={
        "payment_initiation_id": "<id>",
    })

    assert res.v3_retry_payment_initiation_response is not None

    # Handle response
    print(res.v3_retry_payment_initiation_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V3RetryPaymentInitiationRequest](../../models/operations/v3retrypaymentinitiationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.V3RetryPaymentInitiationResponse](../../models/operations/v3retrypaymentinitiationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## reverse_payment_initiation

Reverse a payment initiation

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ReversePaymentInitiation" method="post" path="/api/payments/v3/payment-initiations/{paymentInitiationID}/reverse" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.reverse_payment_initiation(request={
        "payment_initiation_id": "<id>",
    })

    assert res.v3_reverse_payment_initiation_response is not None

    # Handle response
    print(res.v3_reverse_payment_initiation_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V3ReversePaymentInitiationRequest](../../models/operations/v3reversepaymentinitiationrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.V3ReversePaymentInitiationResponse](../../models/operations/v3reversepaymentinitiationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## uninstall_connector

Uninstall a connector

### Example Usage

<!-- UsageSnippet language="python" operationID="v3UninstallConnector" method="delete" path="/api/payments/v3/connectors/{connectorID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.uninstall_connector(request={
        "connector_id": "<id>",
    })

    assert res.v3_uninstall_connector_response is not None

    # Handle response
    print(res.v3_uninstall_connector_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3UninstallConnectorRequest](../../models/operations/v3uninstallconnectorrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3UninstallConnectorResponse](../../models/operations/v3uninstallconnectorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## update_bank_account_metadata

Update a bank account's metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="v3UpdateBankAccountMetadata" method="patch" path="/api/payments/v3/bank-accounts/{bankAccountID}/metadata" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.update_bank_account_metadata(request={
        "bank_account_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.V3UpdateBankAccountMetadataRequest](../../models/operations/v3updatebankaccountmetadatarequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.V3UpdateBankAccountMetadataResponse](../../models/operations/v3updatebankaccountmetadataresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## update_payment_metadata

Update a payment's metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="v3UpdatePaymentMetadata" method="patch" path="/api/payments/v3/payments/{paymentID}/metadata" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.update_payment_metadata(request={
        "payment_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3UpdatePaymentMetadataRequest](../../models/operations/v3updatepaymentmetadatarequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3UpdatePaymentMetadataResponse](../../models/operations/v3updatepaymentmetadataresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V3ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## v3_update_connector_config

Update connector config

### Example Usage

<!-- UsageSnippet language="python" operationID="v3UpdateConnectorConfig" method="patch" path="/api/payments/v3/connectors/{connectorID}/config" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.payments.v3.v3_update_connector_config(request={
        "connector_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3UpdateConnectorConfigRequest](../../models/operations/v3updateconnectorconfigrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3UpdateConnectorConfigResponse](../../models/operations/v3updateconnectorconfigresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.PaymentsErrorResponse | default                      | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |