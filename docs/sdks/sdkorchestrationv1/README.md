# SDKOrchestrationV1
(*orchestration.v1*)

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

## cancel_event

Cancel a running workflow

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


res = s.orchestration.v1.cancel_event(request=operations.CancelEventRequest(
    instance_id='xxx',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CancelEventRequest](../../models/operations/canceleventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

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
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.create_trigger()

if res.create_trigger_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.TriggerData](../../models/shared/triggerdata.md) | :heavy_check_mark:                                       | The request object to use for the request.               |

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
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.create_workflow()

if res.create_workflow_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CreateWorkflowRequest](../../models/shared/createworkflowrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.delete_trigger(request=operations.DeleteTriggerRequest(
    trigger_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteTriggerRequest](../../models/operations/deletetriggerrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.delete_workflow(request=operations.DeleteWorkflowRequest(
    flow_id='xxx',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteWorkflowRequest](../../models/operations/deleteworkflowrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.get_instance(request=operations.GetInstanceRequest(
    instance_id='xxx',
))

if res.get_workflow_instance_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetInstanceRequest](../../models/operations/getinstancerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.get_instance_history(request=operations.GetInstanceHistoryRequest(
    instance_id='xxx',
))

if res.get_workflow_instance_history_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetInstanceHistoryRequest](../../models/operations/getinstancehistoryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.get_instance_stage_history(request=operations.GetInstanceStageHistoryRequest(
    instance_id='xxx',
    number=0,
))

if res.get_workflow_instance_history_stage_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetInstanceStageHistoryRequest](../../models/operations/getinstancestagehistoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.get_workflow(request=operations.GetWorkflowRequest(
    flow_id='xxx',
))

if res.get_workflow_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetWorkflowRequest](../../models/operations/getworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.list_instances(request=operations.ListInstancesRequest(
    running=True,
    workflow_id='xxx',
))

if res.list_runs_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListInstancesRequest](../../models/operations/listinstancesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.list_triggers(request=operations.ListTriggersRequest())

if res.list_triggers_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListTriggersRequest](../../models/operations/listtriggersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.list_triggers_occurrences(request=operations.ListTriggersOccurrencesRequest(
    trigger_id='<value>',
))

if res.list_triggers_occurrences_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTriggersOccurrencesRequest](../../models/operations/listtriggersoccurrencesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |

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
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.list_workflows()

if res.list_workflows_response is not None:
    # handle response
    pass

```

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
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.orchestrationget_server_info()

if res.server_info is not None:
    # handle response
    pass

```

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.read_trigger(request=operations.ReadTriggerRequest(
    trigger_id='<value>',
))

if res.read_trigger_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ReadTriggerRequest](../../models/operations/readtriggerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.run_workflow(request=operations.RunWorkflowRequest(
    workflow_id='xxx',
))

if res.run_workflow_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RunWorkflowRequest](../../models/operations/runworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

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
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.orchestration.v1.send_event(request=operations.SendEventRequest(
    instance_id='xxx',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.SendEventRequest](../../models/operations/sendeventrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |

### Response

**[operations.SendEventResponse](../../models/operations/sendeventresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | default          | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |