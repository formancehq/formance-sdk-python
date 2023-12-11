# Payments
(*payments*)

### Available Operations

* [connectors_stripe_transfer](#connectors_stripe_transfer) - Transfer funds between Stripe accounts
* [connectors_transfer](#connectors_transfer) - Transfer funds between Connector accounts
* [get_account_balances](#get_account_balances) - Get account balances
* [get_connector_task](#get_connector_task) - Read a specific task of the connector
* [get_payment](#get_payment) - Get a payment
* [install_connector](#install_connector) - Install a connector
* [list_all_connectors](#list_all_connectors) - List all installed connectors
* [list_configs_available_connectors](#list_configs_available_connectors) - List the configs of each available connector
* [list_connector_tasks](#list_connector_tasks) - List tasks from a connector
* [list_connectors_transfers](#list_connectors_transfers) - List transfers and their statuses
* [list_payments](#list_payments) - List payments
* [paymentsget_account](#paymentsget_account) - Get an account
* [paymentsget_server_info](#paymentsget_server_info) - Get server info
* [paymentslist_accounts](#paymentslist_accounts) - List accounts
* [read_connector_config](#read_connector_config) - Read the config of a connector
* [reset_connector](#reset_connector) - Reset a connector
* [uninstall_connector](#uninstall_connector) - Uninstall a connector
* [update_metadata](#update_metadata) - Update metadata

## connectors_stripe_transfer

Execute a transfer between two Stripe accounts.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK()

req = shared.StripeTransferRequest(
    amount=100,
    asset='USD',
    destination='acct_1Gqj58KZcSIg2N2q',
    metadata=shared.StripeTransferRequestMetadata(),
)

res = s.payments.connectors_stripe_transfer(req)

if res.stripe_transfer_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.StripeTransferRequest](../../models/shared/stripetransferrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ConnectorsStripeTransferResponse](../../models/operations/connectorsstripetransferresponse.md)**


## connectors_transfer

Execute a transfer between two accounts.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ConnectorsTransferRequest(
    transfer_request=shared.TransferRequest(
        amount=100,
        asset='USD',
        destination='acct_1Gqj58KZcSIg2N2q',
        source='acct_1Gqj58KZcSIg2N2q',
    ),
    connector=shared.Connector.MODULR,
)

res = s.payments.connectors_transfer(req)

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


## get_account_balances

Get account balances

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations

s = sdk.SDK()

req = operations.GetAccountBalancesRequest(
    account_id='string',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    sort=[
        'string',
    ],
)

res = s.payments.get_account_balances(req)

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


## get_connector_task

Get a specific task associated to the connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.GetConnectorTaskRequest(
    connector=shared.Connector.MONEYCORP,
    task_id='string',
)

res = s.payments.get_connector_task(req)

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


## get_payment

Get a payment

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.GetPaymentRequest(
    payment_id='string',
)

res = s.payments.get_payment(req)

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


## install_connector

Install a connector by its name and config.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.InstallConnectorRequest(
    shared.DummyPayConfig(
        directory='/tmp/dummypay',
        file_generation_period='60s',
        file_polling_period='60s',
    ),
    connector=shared.Connector.MONEYCORP,
)

res = s.payments.install_connector(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.InstallConnectorRequest](../../models/operations/installconnectorrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.InstallConnectorResponse](../../models/operations/installconnectorresponse.md)**


## list_all_connectors

List all installed connectors.

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.payments.list_all_connectors()

if res.connectors_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListAllConnectorsResponse](../../models/operations/listallconnectorsresponse.md)**


## list_configs_available_connectors

List the configs of each available connector.

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.payments.list_configs_available_connectors()

if res.connectors_configs_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListConfigsAvailableConnectorsResponse](../../models/operations/listconfigsavailableconnectorsresponse.md)**


## list_connector_tasks

List all tasks associated with this connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ListConnectorTasksRequest(
    connector=shared.Connector.WISE,
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.payments.list_connector_tasks(req)

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


## list_connectors_transfers

List transfers

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ListConnectorsTransfersRequest(
    connector=shared.Connector.BANKING_CIRCLE,
)

res = s.payments.list_connectors_transfers(req)

if res.transfers_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListConnectorsTransfersRequest](../../models/operations/listconnectorstransfersrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListConnectorsTransfersResponse](../../models/operations/listconnectorstransfersresponse.md)**


## list_payments

List payments

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.ListPaymentsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    sort=[
        'string',
    ],
)

res = s.payments.list_payments(req)

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


## paymentsget_account

Get an account

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.PaymentsgetAccountRequest(
    account_id='string',
)

res = s.payments.paymentsget_account(req)

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


## paymentsget_server_info

Get server info

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.payments.paymentsget_server_info()

if res.server_info is not None:
    # handle response
    pass
```


### Response

**[operations.PaymentsgetServerInfoResponse](../../models/operations/paymentsgetserverinforesponse.md)**


## paymentslist_accounts

List accounts

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.PaymentslistAccountsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    sort=[
        'string',
    ],
)

res = s.payments.paymentslist_accounts(req)

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


## read_connector_config

Read connector config

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ReadConnectorConfigRequest(
    connector=shared.Connector.MONEYCORP,
)

res = s.payments.read_connector_config(req)

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


## reset_connector

Reset a connector by its name.
It will remove the connector and ALL PAYMENTS generated with it.


### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ResetConnectorRequest(
    connector=shared.Connector.MANGOPAY,
)

res = s.payments.reset_connector(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ResetConnectorRequest](../../models/operations/resetconnectorrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ResetConnectorResponse](../../models/operations/resetconnectorresponse.md)**


## uninstall_connector

Uninstall a connector by its name.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.UninstallConnectorRequest(
    connector=shared.Connector.WISE,
)

res = s.payments.uninstall_connector(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UninstallConnectorRequest](../../models/operations/uninstallconnectorrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UninstallConnectorResponse](../../models/operations/uninstallconnectorresponse.md)**


## update_metadata

Update metadata

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.UpdateMetadataRequest(
    payment_metadata=shared.PaymentMetadata(),
    payment_id='string',
)

res = s.payments.update_metadata(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateMetadataRequest](../../models/operations/updatemetadatarequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateMetadataResponse](../../models/operations/updatemetadataresponse.md)**

