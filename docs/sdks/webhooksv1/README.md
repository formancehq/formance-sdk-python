# Webhooks.V1

## Overview

### Available Operations

* [activate_config](#activate_config) - Activate one config
* [change_config_secret](#change_config_secret) - Change the signing secret of a config
* [deactivate_config](#deactivate_config) - Deactivate one config
* [delete_config](#delete_config) - Delete one config
* [get_deliveries](#get_deliveries) - List webhook deliveries
* [get_delivery](#get_delivery) - Get a webhook delivery
* [get_delivery_attempts](#get_delivery_attempts) - List attempts for a webhook delivery
* [get_many_configs](#get_many_configs) - Get many configs
* [insert_config](#insert_config) - Insert a new config
* [replay_deliveries](#replay_deliveries) - Replay a page of failed or pending deliveries
* [replay_delivery](#replay_delivery) - Replay one failed or pending delivery
* [test_config](#test_config) - Test one config
* [update_config](#update_config) - Update one config

## activate_config

Activate a webhooks config by ID, to start receiving webhooks to its endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="activateConfig" method="put" path="/api/webhooks/configs/{id}/activate" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.activate_config(request={
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res.config_response is not None

    # Handle response
    print(res.config_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ActivateConfigRequest](../../models/operations/activateconfigrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ActivateConfigResponse](../../models/operations/activateconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## change_config_secret

Change the signing secret of the endpoint of a webhooks config.

If not passed or empty, a secret is automatically generated.
The format is a random string of bytes of size 24, base64 encoded. (larger size after encoding)


### Example Usage

<!-- UsageSnippet language="python" operationID="changeConfigSecret" method="put" path="/api/webhooks/configs/{id}/secret/change" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.change_config_secret(request={
        "config_change_secret": {
            "secret": "V0bivxRWveaoz08afqjU6Ko/jwO0Cb+3",
        },
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res.config_response is not None

    # Handle response
    print(res.config_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ChangeConfigSecretRequest](../../models/operations/changeconfigsecretrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ChangeConfigSecretResponse](../../models/operations/changeconfigsecretresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## deactivate_config

Deactivate a webhooks config by ID, to stop receiving webhooks to its endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="deactivateConfig" method="put" path="/api/webhooks/configs/{id}/deactivate" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.deactivate_config(request={
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res.config_response is not None

    # Handle response
    print(res.config_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeactivateConfigRequest](../../models/operations/deactivateconfigrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.DeactivateConfigResponse](../../models/operations/deactivateconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## delete_config

Delete a webhooks config by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConfig" method="delete" path="/api/webhooks/configs/{id}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.delete_config(request={
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteConfigRequest](../../models/operations/deleteconfigrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.DeleteConfigResponse](../../models/operations/deleteconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_deliveries

List webhook deliveries

### Example Usage

<!-- UsageSnippet language="python" operationID="getDeliveries" method="get" path="/api/webhooks/deliveries" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.get_deliveries(request={})

    assert res.deliveries_response is not None

    # Handle response
    print(res.deliveries_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetDeliveriesRequest](../../models/operations/getdeliveriesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetDeliveriesResponse](../../models/operations/getdeliveriesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_delivery

Get a webhook delivery

### Example Usage

<!-- UsageSnippet language="python" operationID="getDelivery" method="get" path="/api/webhooks/deliveries/{id}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.get_delivery(request={
        "id": "01e5cac6-75f1-4720-81ca-5563ce22d2e0",
    })

    assert res.delivery_response is not None

    # Handle response
    print(res.delivery_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetDeliveryRequest](../../models/operations/getdeliveryrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetDeliveryResponse](../../models/operations/getdeliveryresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_delivery_attempts

List attempts for a webhook delivery

### Example Usage

<!-- UsageSnippet language="python" operationID="getDeliveryAttempts" method="get" path="/api/webhooks/deliveries/{id}/attempts" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.get_delivery_attempts(request={
        "id": "967e7a38-b11b-4809-92cf-6789e24dbe13",
    })

    assert res.delivery_attempts_response is not None

    # Handle response
    print(res.delivery_attempts_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetDeliveryAttemptsRequest](../../models/operations/getdeliveryattemptsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetDeliveryAttemptsResponse](../../models/operations/getdeliveryattemptsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_many_configs

Sorted by updated date descending

### Example Usage

<!-- UsageSnippet language="python" operationID="getManyConfigs" method="get" path="/api/webhooks/configs" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.get_many_configs(request={
        "endpoint": "https://example.com",
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res.configs_response is not None

    # Handle response
    print(res.configs_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetManyConfigsRequest](../../models/operations/getmanyconfigsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetManyConfigsResponse](../../models/operations/getmanyconfigsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## insert_config

Insert a new webhooks config.

The endpoint should be a valid https URL and be unique.

The secret is the endpoint's verification secret.
If not passed or empty, a secret is automatically generated.
The format is a random string of bytes of size 24, base64 encoded. (larger size after encoding)

All eventTypes are converted to lower-case when inserted.


### Example Usage

<!-- UsageSnippet language="python" operationID="insertConfig" method="post" path="/api/webhooks/configs" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.insert_config(request={
        "endpoint": "https://example.com",
        "event_types": [
            "TYPE1",
            "TYPE2",
        ],
        "secret": "V0bivxRWveaoz08afqjU6Ko/jwO0Cb+3",
    })

    assert res.config_response is not None

    # Handle response
    print(res.config_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [webhooks.ConfigUser](../../models/webhooks/configuser.md)          | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.InsertConfigResponse](../../models/operations/insertconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## replay_deliveries

Replay a page of failed or pending deliveries

### Example Usage

<!-- UsageSnippet language="python" operationID="replayDeliveries" method="post" path="/api/webhooks/deliveries/replay" -->
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

    res = sdk.webhooks.v1.replay_deliveries(request={
        "idempotency_key": "<value>",
        "replay_deliveries_request": {
            "created_at_from": parse_datetime("2026-10-16T11:02:44.647Z"),
        },
    })

    assert res.replay_deliveries_response is not None

    # Handle response
    print(res.replay_deliveries_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ReplayDeliveriesRequest](../../models/operations/replaydeliveriesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ReplayDeliveriesResponse](../../models/operations/replaydeliveriesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## replay_delivery

Replay one failed or pending delivery

### Example Usage

<!-- UsageSnippet language="python" operationID="replayDelivery" method="post" path="/api/webhooks/deliveries/{id}/replay" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.replay_delivery(request={
        "idempotency_key": "<value>",
        "id": "06a0d0bb-48de-45f0-b12f-6458a3a41bbe",
    })

    assert res.delivery_response is not None

    # Handle response
    print(res.delivery_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ReplayDeliveryRequest](../../models/operations/replaydeliveryrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ReplayDeliveryResponse](../../models/operations/replaydeliveryresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## test_config

Test a config by sending a webhook to its endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="testConfig" method="get" path="/api/webhooks/configs/{id}/test" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.test_config(request={
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res.attempt_response is not None

    # Handle response
    print(res.attempt_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.TestConfigRequest](../../models/operations/testconfigrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.TestConfigResponse](../../models/operations/testconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## update_config

Update a webhooks config by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateConfig" method="put" path="/api/webhooks/configs/{id}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.webhooks.v1.update_config(request={
        "config_user": {
            "endpoint": "https://example.com",
            "event_types": [
                "TYPE1",
                "TYPE2",
            ],
            "secret": "V0bivxRWveaoz08afqjU6Ko/jwO0Cb+3",
        },
        "id": "4997257d-dfb6-445b-929c-cbe2ab182818",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateConfigRequest](../../models/operations/updateconfigrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.UpdateConfigResponse](../../models/operations/updateconfigresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| webhooks.ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |