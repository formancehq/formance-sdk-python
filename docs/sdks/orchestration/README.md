# Orchestration
(*orchestration*)

## Overview

### Available Operations

* [cancel_event](#cancel_event) - Cancel a running workflow
* [create_trigger](#create_trigger) - Create trigger
* [create_workflow](#create_workflow) - Create workflow
* [delete_trigger](#delete_trigger) - Delete trigger
* [delete_workflow](#delete_workflow) - Delete a flow by id
* [get_instance](#get_instance) - Get a workflow instance by id
* [get_instance_history](#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](#get_instance_stage_history) - Get a workflow instance stage history
* [get_workflow](#get_workflow) - Get a flow by id
* [list_instances](#list_instances) - List instances of a workflow
* [list_triggers](#list_triggers) - List triggers
* [list_triggers_occurrences](#list_triggers_occurrences) - List triggers occurrences
* [list_workflows](#list_workflows) - List registered workflows
* [orchestrationget_server_info](#orchestrationget_server_info) - Get server info
* [read_trigger](#read_trigger) - Read trigger
* [run_workflow](#run_workflow) - Run workflow
* [send_event](#send_event) - Send an event to a running workflow
* [test_trigger](#test_trigger) - Test trigger
* [v2_cancel_event](#v2_cancel_event) - Cancel a running workflow
* [v2_create_trigger](#v2_create_trigger) - Create trigger
* [v2_create_workflow](#v2_create_workflow) - Create workflow
* [v2_delete_trigger](#v2_delete_trigger) - Delete trigger
* [v2_delete_workflow](#v2_delete_workflow) - Delete a flow by id
* [v2_get_instance](#v2_get_instance) - Get a workflow instance by id
* [v2_get_instance_history](#v2_get_instance_history) - Get a workflow instance history by id
* [v2_get_instance_stage_history](#v2_get_instance_stage_history) - Get a workflow instance stage history
* [v2_get_server_info](#v2_get_server_info) - Get server info
* [v2_get_workflow](#v2_get_workflow) - Get a flow by id
* [v2_list_instances](#v2_list_instances) - List instances of a workflow
* [v2_list_triggers](#v2_list_triggers) - List triggers
* [v2_list_triggers_occurrences](#v2_list_triggers_occurrences) - List triggers occurrences
* [v2_list_workflows](#v2_list_workflows) - List registered workflows
* [v2_read_trigger](#v2_read_trigger) - Read trigger
* [v2_run_workflow](#v2_run_workflow) - Run workflow
* [v2_send_event](#v2_send_event) - Send an event to a running workflow

## cancel_event

Cancel a running workflow

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

    res = sdk.orchestration.cancel_event(request={
        "instance_id": "xxx",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CancelEventRequest](../../models/operations/canceleventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.CancelEventResponse](../../models/operations/canceleventresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_trigger

Create trigger

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

    res = sdk.orchestration.create_trigger()

    assert res.create_trigger_response is not None

    # Handle response
    print(res.create_trigger_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.TriggerData](../../models/shared/triggerdata.md)            | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateTriggerResponse](../../models/operations/createtriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_workflow

Create a workflow

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

    res = sdk.orchestration.create_workflow()

    assert res.create_workflow_response is not None

    # Handle response
    print(res.create_workflow_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CreateWorkflowRequest](../../models/shared/createworkflowrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.CreateWorkflowResponse](../../models/operations/createworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## delete_trigger

Read trigger

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

    res = sdk.orchestration.delete_trigger(request={
        "trigger_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteTriggerRequest](../../models/operations/deletetriggerrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.DeleteTriggerResponse](../../models/operations/deletetriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## delete_workflow

Delete a flow by id

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

    res = sdk.orchestration.delete_workflow(request={
        "flow_id": "xxx",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteWorkflowRequest](../../models/operations/deleteworkflowrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.DeleteWorkflowResponse](../../models/operations/deleteworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_instance

Get a workflow instance by id

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

    res = sdk.orchestration.get_instance(request={
        "instance_id": "xxx",
    })

    assert res.get_workflow_instance_response is not None

    # Handle response
    print(res.get_workflow_instance_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetInstanceRequest](../../models/operations/getinstancerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetInstanceResponse](../../models/operations/getinstanceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_instance_history

Get a workflow instance history by id

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

    res = sdk.orchestration.get_instance_history(request={
        "instance_id": "xxx",
    })

    assert res.get_workflow_instance_history_response is not None

    # Handle response
    print(res.get_workflow_instance_history_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetInstanceHistoryRequest](../../models/operations/getinstancehistoryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetInstanceHistoryResponse](../../models/operations/getinstancehistoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_instance_stage_history

Get a workflow instance stage history

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

    res = sdk.orchestration.get_instance_stage_history(request={
        "instance_id": "xxx",
        "number": 0,
    })

    assert res.get_workflow_instance_history_stage_response is not None

    # Handle response
    print(res.get_workflow_instance_history_stage_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetInstanceStageHistoryRequest](../../models/operations/getinstancestagehistoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetInstanceStageHistoryResponse](../../models/operations/getinstancestagehistoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_workflow

Get a flow by id

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

    res = sdk.orchestration.get_workflow(request={
        "flow_id": "xxx",
    })

    assert res.get_workflow_response is not None

    # Handle response
    print(res.get_workflow_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetWorkflowRequest](../../models/operations/getworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetWorkflowResponse](../../models/operations/getworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_instances

List instances of a workflow

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

    res = sdk.orchestration.list_instances(request={
        "running": True,
        "workflow_id": "xxx",
    })

    assert res.list_runs_response is not None

    # Handle response
    print(res.list_runs_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListInstancesRequest](../../models/operations/listinstancesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListInstancesResponse](../../models/operations/listinstancesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_triggers

List triggers

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

    res = sdk.orchestration.list_triggers(request={})

    assert res.list_triggers_response is not None

    # Handle response
    print(res.list_triggers_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListTriggersRequest](../../models/operations/listtriggersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListTriggersResponse](../../models/operations/listtriggersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_triggers_occurrences

List triggers occurrences

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

    res = sdk.orchestration.list_triggers_occurrences(request={
        "trigger_id": "<id>",
    })

    assert res.list_triggers_occurrences_response is not None

    # Handle response
    print(res.list_triggers_occurrences_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTriggersOccurrencesRequest](../../models/operations/listtriggersoccurrencesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListTriggersOccurrencesResponse](../../models/operations/listtriggersoccurrencesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_workflows

List registered workflows

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

    res = sdk.orchestration.list_workflows()

    assert res.list_workflows_response is not None

    # Handle response
    print(res.list_workflows_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListWorkflowsResponse](../../models/operations/listworkflowsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## orchestrationget_server_info

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

    res = sdk.orchestration.orchestrationget_server_info()

    assert res.server_info is not None

    # Handle response
    print(res.server_info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.OrchestrationgetServerInfoResponse](../../models/operations/orchestrationgetserverinforesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## read_trigger

Read trigger

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

    res = sdk.orchestration.read_trigger(request={
        "trigger_id": "<id>",
    })

    assert res.read_trigger_response is not None

    # Handle response
    print(res.read_trigger_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ReadTriggerRequest](../../models/operations/readtriggerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ReadTriggerResponse](../../models/operations/readtriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## run_workflow

Run workflow

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

    res = sdk.orchestration.run_workflow(request={
        "workflow_id": "xxx",
    })

    assert res.run_workflow_response is not None

    # Handle response
    print(res.run_workflow_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RunWorkflowRequest](../../models/operations/runworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.RunWorkflowResponse](../../models/operations/runworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## send_event

Send an event to a running workflow

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

    res = sdk.orchestration.send_event(request={
        "instance_id": "xxx",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.SendEventRequest](../../models/operations/sendeventrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.SendEventResponse](../../models/operations/sendeventresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## test_trigger

Test trigger

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

    res = sdk.orchestration.test_trigger(request={
        "trigger_id": "<id>",
    })

    assert res.v2_test_trigger_response is not None

    # Handle response
    print(res.v2_test_trigger_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.TestTriggerRequest](../../models/operations/testtriggerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.TestTriggerResponse](../../models/operations/testtriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_cancel_event

Cancel a running workflow

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

    res = sdk.orchestration.v2_cancel_event(request={
        "instance_id": "xxx",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2CancelEventRequest](../../models/operations/v2canceleventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.V2CancelEventResponse](../../models/operations/v2canceleventresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_create_trigger

Create trigger

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

    res = sdk.orchestration.v2_create_trigger()

    assert res.v2_create_trigger_response is not None

    # Handle response
    print(res.v2_create_trigger_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.V2TriggerData](../../models/shared/v2triggerdata.md)        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.V2CreateTriggerResponse](../../models/operations/v2createtriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_create_workflow

Create a workflow

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

    res = sdk.orchestration.v2_create_workflow()

    assert res.v2_create_workflow_response is not None

    # Handle response
    print(res.v2_create_workflow_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.V2CreateWorkflowRequest](../../models/shared/v2createworkflowrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V2CreateWorkflowResponse](../../models/operations/v2createworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_delete_trigger

Read trigger

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

    res = sdk.orchestration.v2_delete_trigger(request={
        "trigger_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2DeleteTriggerRequest](../../models/operations/v2deletetriggerrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V2DeleteTriggerResponse](../../models/operations/v2deletetriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_delete_workflow

Delete a flow by id

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

    res = sdk.orchestration.v2_delete_workflow(request={
        "flow_id": "xxx",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V2DeleteWorkflowRequest](../../models/operations/v2deleteworkflowrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V2DeleteWorkflowResponse](../../models/operations/v2deleteworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_get_instance

Get a workflow instance by id

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

    res = sdk.orchestration.v2_get_instance(request={
        "instance_id": "xxx",
    })

    assert res.v2_get_workflow_instance_response is not None

    # Handle response
    print(res.v2_get_workflow_instance_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2GetInstanceRequest](../../models/operations/v2getinstancerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.V2GetInstanceResponse](../../models/operations/v2getinstanceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_get_instance_history

Get a workflow instance history by id

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

    res = sdk.orchestration.v2_get_instance_history(request={
        "instance_id": "xxx",
    })

    assert res.v2_get_workflow_instance_history_response is not None

    # Handle response
    print(res.v2_get_workflow_instance_history_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V2GetInstanceHistoryRequest](../../models/operations/v2getinstancehistoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V2GetInstanceHistoryResponse](../../models/operations/v2getinstancehistoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_get_instance_stage_history

Get a workflow instance stage history

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

    res = sdk.orchestration.v2_get_instance_stage_history(request={
        "instance_id": "xxx",
        "number": 0,
    })

    assert res.v2_get_workflow_instance_history_stage_response is not None

    # Handle response
    print(res.v2_get_workflow_instance_history_stage_response)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V2GetInstanceStageHistoryRequest](../../models/operations/v2getinstancestagehistoryrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.V2GetInstanceStageHistoryResponse](../../models/operations/v2getinstancestagehistoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_get_server_info

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

    res = sdk.orchestration.v2_get_server_info()

    assert res.v2_server_info is not None

    # Handle response
    print(res.v2_server_info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.V2GetServerInfoResponse](../../models/operations/v2getserverinforesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_get_workflow

Get a flow by id

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

    res = sdk.orchestration.v2_get_workflow(request={
        "flow_id": "xxx",
    })

    assert res.v2_get_workflow_response is not None

    # Handle response
    print(res.v2_get_workflow_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2GetWorkflowRequest](../../models/operations/v2getworkflowrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.V2GetWorkflowResponse](../../models/operations/v2getworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_list_instances

List instances of a workflow

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

    res = sdk.orchestration.v2_list_instances(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
        "running": True,
        "workflow_id": "xxx",
    })

    assert res.v2_list_runs_response is not None

    # Handle response
    print(res.v2_list_runs_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2ListInstancesRequest](../../models/operations/v2listinstancesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V2ListInstancesResponse](../../models/operations/v2listinstancesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_list_triggers

List triggers

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

    res = sdk.orchestration.v2_list_triggers(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_list_triggers_response is not None

    # Handle response
    print(res.v2_list_triggers_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V2ListTriggersRequest](../../models/operations/v2listtriggersrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.V2ListTriggersResponse](../../models/operations/v2listtriggersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_list_triggers_occurrences

List triggers occurrences

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

    res = sdk.orchestration.v2_list_triggers_occurrences(request={
        "trigger_id": "<id>",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_list_triggers_occurrences_response is not None

    # Handle response
    print(res.v2_list_triggers_occurrences_response)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V2ListTriggersOccurrencesRequest](../../models/operations/v2listtriggersoccurrencesrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.V2ListTriggersOccurrencesResponse](../../models/operations/v2listtriggersoccurrencesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_list_workflows

List registered workflows

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

    res = sdk.orchestration.v2_list_workflows(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.v2_list_workflows_response is not None

    # Handle response
    print(res.v2_list_workflows_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2ListWorkflowsRequest](../../models/operations/v2listworkflowsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V2ListWorkflowsResponse](../../models/operations/v2listworkflowsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_read_trigger

Read trigger

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

    res = sdk.orchestration.v2_read_trigger(request={
        "trigger_id": "<id>",
    })

    assert res.v2_read_trigger_response is not None

    # Handle response
    print(res.v2_read_trigger_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2ReadTriggerRequest](../../models/operations/v2readtriggerrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.V2ReadTriggerResponse](../../models/operations/v2readtriggerresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_run_workflow

Run workflow

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

    res = sdk.orchestration.v2_run_workflow(request={
        "workflow_id": "xxx",
    })

    assert res.v2_run_workflow_response is not None

    # Handle response
    print(res.v2_run_workflow_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2RunWorkflowRequest](../../models/operations/v2runworkflowrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.V2RunWorkflowResponse](../../models/operations/v2runworkflowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## v2_send_event

Send an event to a running workflow

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

    res = sdk.orchestration.v2_send_event(request={
        "instance_id": "xxx",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V2SendEventRequest](../../models/operations/v2sendeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V2SendEventResponse](../../models/operations/v2sendeventresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |