# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [activate_config](#activate_config) - Activate one config
* [change_config_secret](#change_config_secret) - Change the signing secret of a config
* [deactivate_config](#deactivate_config) - Deactivate one config
* [delete_config](#delete_config) - Delete one config
* [get_many_configs](#get_many_configs) - Get many configs
* [insert_config](#insert_config) - Insert a new config
* [test_config](#test_config) - Test one config

## activate_config

Activate a webhooks config by ID, to start receiving webhooks to its endpoint.

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


res = s.webhooks.activate_config(request=operations.ActivateConfigRequest(
    id='4997257d-dfb6-445b-929c-cbe2ab182818',
))

if res.config_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ActivateConfigRequest](../../models/operations/activateconfigrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[operations.ActivateConfigResponse](../../models/operations/activateconfigresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |


## change_config_secret

Change the signing secret of the endpoint of a webhooks config.

If not passed or empty, a secret is automatically generated.
The format is a random string of bytes of size 24, base64 encoded. (larger size after encoding)


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


res = s.webhooks.change_config_secret(request=operations.ChangeConfigSecretRequest(
    id='4997257d-dfb6-445b-929c-cbe2ab182818',
    config_change_secret=shared.ConfigChangeSecret(
        secret='V0bivxRWveaoz08afqjU6Ko/jwO0Cb+3',
    ),
))

if res.config_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ChangeConfigSecretRequest](../../models/operations/changeconfigsecretrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |

### Response

**[operations.ChangeConfigSecretResponse](../../models/operations/changeconfigsecretresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |


## deactivate_config

Deactivate a webhooks config by ID, to stop receiving webhooks to its endpoint.

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


res = s.webhooks.deactivate_config(request=operations.DeactivateConfigRequest(
    id='4997257d-dfb6-445b-929c-cbe2ab182818',
))

if res.config_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeactivateConfigRequest](../../models/operations/deactivateconfigrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |

### Response

**[operations.DeactivateConfigResponse](../../models/operations/deactivateconfigresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |


## delete_config

Delete a webhooks config by ID.

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


res = s.webhooks.delete_config(request=operations.DeleteConfigRequest(
    id='4997257d-dfb6-445b-929c-cbe2ab182818',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteConfigRequest](../../models/operations/deleteconfigrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |

### Response

**[operations.DeleteConfigResponse](../../models/operations/deleteconfigresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |


## get_many_configs

Sorted by updated date descending

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


res = s.webhooks.get_many_configs(request=operations.GetManyConfigsRequest(
    endpoint='https://example.com',
    id='4997257d-dfb6-445b-929c-cbe2ab182818',
))

if res.configs_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetManyConfigsRequest](../../models/operations/getmanyconfigsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[operations.GetManyConfigsResponse](../../models/operations/getmanyconfigsresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |


## insert_config

Insert a new webhooks config.

The endpoint should be a valid https URL and be unique.

The secret is the endpoint's verification secret.
If not passed or empty, a secret is automatically generated.
The format is a random string of bytes of size 24, base64 encoded. (larger size after encoding)

All eventTypes are converted to lower-case when inserted.


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


res = s.webhooks.insert_config(request=shared.ConfigUser(
    endpoint='https://example.com',
    event_types=[
        'TYPE1',
    ],
    name='customer_payment',
    secret='V0bivxRWveaoz08afqjU6Ko/jwO0Cb+3',
))

if res.config_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.ConfigUser](../../models/shared/configuser.md) | :heavy_check_mark:                                     | The request object to use for the request.             |

### Response

**[operations.InsertConfigResponse](../../models/operations/insertconfigresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |


## test_config

Test a config by sending a webhook to its endpoint.

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


res = s.webhooks.test_config(request=operations.TestConfigRequest(
    id='4997257d-dfb6-445b-929c-cbe2ab182818',
))

if res.attempt_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.TestConfigRequest](../../models/operations/testconfigrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |

### Response

**[operations.TestConfigResponse](../../models/operations/testconfigresponse.md)**

### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.WebhooksErrorResponse | default                      | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |
