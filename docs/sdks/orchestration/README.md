# Orchestration
(*orchestration*)

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
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.CancelEventRequest(
    instance_id='string',
)

res = s.orchestration.cancel_event(req)

if res.status_code == 200:
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_trigger

Create trigger

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.TriggerData(
    event='string',
    vars={
        'key': 'string',
    },
    workflow_id='string',
)

res = s.orchestration.create_trigger(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_workflow

Create a workflow

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.CreateWorkflowRequest(
    stages=[
        {
            'key': 'string',
        },
    ],
)

res = s.orchestration.create_workflow(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_trigger

Read trigger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.DeleteTriggerRequest(
    trigger_id='string',
)

res = s.orchestration.delete_trigger(req)

if res.status_code == 200:
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_workflow

Delete a flow by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.DeleteWorkflowRequest(
    flow_id='string',
)

res = s.orchestration.delete_workflow(req)

if res.status_code == 200:
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_instance

Get a workflow instance by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetInstanceRequest(
    instance_id='string',
)

res = s.orchestration.get_instance(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_instance_history

Get a workflow instance history by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetInstanceHistoryRequest(
    instance_id='string',
)

res = s.orchestration.get_instance_history(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_instance_stage_history

Get a workflow instance stage history

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetInstanceStageHistoryRequest(
    instance_id='string',
    number=600636,
)

res = s.orchestration.get_instance_stage_history(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_workflow

Get a flow by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetWorkflowRequest(
    flow_id='string',
)

res = s.orchestration.get_workflow(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_instances

List instances of a workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListInstancesRequest()

res = s.orchestration.list_instances(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_triggers

List triggers

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.orchestration.list_triggers()

if res.list_triggers_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListTriggersResponse](../../models/operations/listtriggersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_triggers_occurrences

List triggers occurrences

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListTriggersOccurrencesRequest(
    trigger_id='string',
)

res = s.orchestration.list_triggers_occurrences(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_workflows

List registered workflows

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.orchestration.list_workflows()

if res.list_workflows_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListWorkflowsResponse](../../models/operations/listworkflowsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## orchestrationget_server_info

Get server info

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.orchestration.orchestrationget_server_info()

if res.server_info is not None:
    # handle response
    pass
```


### Response

**[operations.OrchestrationgetServerInfoResponse](../../models/operations/orchestrationgetserverinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## read_trigger

Read trigger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ReadTriggerRequest(
    trigger_id='string',
)

res = s.orchestration.read_trigger(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## run_workflow

Run workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.RunWorkflowRequest(
    request_body={
        'key': 'string',
    },
    workflow_id='string',
)

res = s.orchestration.run_workflow(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## send_event

Send an event to a running workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.SendEventRequest(
    request_body=operations.SendEventRequestBody(
        name='string',
    ),
    instance_id='string',
)

res = s.orchestration.send_event(req)

if res.status_code == 200:
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## test_trigger

Test trigger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.TestTriggerRequest(
    request_body={
        'key': 'string',
    },
    trigger_id='string',
)

res = s.orchestration.test_trigger(req)

if res.v2_test_trigger_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.TestTriggerRequest](../../models/operations/testtriggerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.TestTriggerResponse](../../models/operations/testtriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_cancel_event

Cancel a running workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2CancelEventRequest(
    instance_id='string',
)

res = s.orchestration.v2_cancel_event(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2CancelEventRequest](../../models/operations/v2canceleventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.V2CancelEventResponse](../../models/operations/v2canceleventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_create_trigger

Create trigger

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.V2TriggerData(
    event='string',
    vars={
        'key': 'string',
    },
    workflow_id='string',
)

res = s.orchestration.v2_create_trigger(req)

if res.v2_create_trigger_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.V2TriggerData](../../models/shared/v2triggerdata.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.V2CreateTriggerResponse](../../models/operations/v2createtriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_create_workflow

Create a workflow

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.V2CreateWorkflowRequest(
    stages=[
        {
            'key': 'string',
        },
    ],
)

res = s.orchestration.v2_create_workflow(req)

if res.v2_create_workflow_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.V2CreateWorkflowRequest](../../models/shared/v2createworkflowrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.V2CreateWorkflowResponse](../../models/operations/v2createworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_delete_trigger

Read trigger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2DeleteTriggerRequest(
    trigger_id='string',
)

res = s.orchestration.v2_delete_trigger(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2DeleteTriggerRequest](../../models/operations/v2deletetriggerrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.V2DeleteTriggerResponse](../../models/operations/v2deletetriggerresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | 404              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## v2_delete_workflow

Delete a flow by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2DeleteWorkflowRequest(
    flow_id='string',
)

res = s.orchestration.v2_delete_workflow(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V2DeleteWorkflowRequest](../../models/operations/v2deleteworkflowrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.V2DeleteWorkflowResponse](../../models/operations/v2deleteworkflowresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.V2Error   | 400,404          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## v2_get_instance

Get a workflow instance by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetInstanceRequest(
    instance_id='string',
)

res = s.orchestration.v2_get_instance(req)

if res.v2_get_workflow_instance_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2GetInstanceRequest](../../models/operations/v2getinstancerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.V2GetInstanceResponse](../../models/operations/v2getinstanceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_instance_history

Get a workflow instance history by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetInstanceHistoryRequest(
    instance_id='string',
)

res = s.orchestration.v2_get_instance_history(req)

if res.v2_get_workflow_instance_history_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V2GetInstanceHistoryRequest](../../models/operations/v2getinstancehistoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.V2GetInstanceHistoryResponse](../../models/operations/v2getinstancehistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_instance_stage_history

Get a workflow instance stage history

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetInstanceStageHistoryRequest(
    instance_id='string',
    number=465454,
)

res = s.orchestration.v2_get_instance_stage_history(req)

if res.v2_get_workflow_instance_history_stage_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V2GetInstanceStageHistoryRequest](../../models/operations/v2getinstancestagehistoryrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.V2GetInstanceStageHistoryResponse](../../models/operations/v2getinstancestagehistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_server_info

Get server info

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.orchestration.v2_get_server_info()

if res.v2_server_info is not None:
    # handle response
    pass
```


### Response

**[operations.V2GetServerInfoResponse](../../models/operations/v2getserverinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_get_workflow

Get a flow by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2GetWorkflowRequest(
    flow_id='string',
)

res = s.orchestration.v2_get_workflow(req)

if res.v2_get_workflow_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2GetWorkflowRequest](../../models/operations/v2getworkflowrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.V2GetWorkflowResponse](../../models/operations/v2getworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_list_instances

List instances of a workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ListInstancesRequest()

res = s.orchestration.v2_list_instances(req)

if res.v2_list_runs_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V2ListInstancesRequest](../../models/operations/v2listinstancesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.V2ListInstancesResponse](../../models/operations/v2listinstancesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_list_triggers

List triggers

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.orchestration.v2_list_triggers()

if res.v2_list_triggers_response is not None:
    # handle response
    pass
```


### Response

**[operations.V2ListTriggersResponse](../../models/operations/v2listtriggersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_list_triggers_occurrences

List triggers occurrences

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ListTriggersOccurrencesRequest(
    trigger_id='string',
)

res = s.orchestration.v2_list_triggers_occurrences(req)

if res.v2_list_triggers_occurrences_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V2ListTriggersOccurrencesRequest](../../models/operations/v2listtriggersoccurrencesrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.V2ListTriggersOccurrencesResponse](../../models/operations/v2listtriggersoccurrencesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_list_workflows

List registered workflows

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.orchestration.v2_list_workflows()

if res.v2_list_workflows_response is not None:
    # handle response
    pass
```


### Response

**[operations.V2ListWorkflowsResponse](../../models/operations/v2listworkflowsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_read_trigger

Read trigger

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2ReadTriggerRequest(
    trigger_id='string',
)

res = s.orchestration.v2_read_trigger(req)

if res.v2_read_trigger_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2ReadTriggerRequest](../../models/operations/v2readtriggerrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.V2ReadTriggerResponse](../../models/operations/v2readtriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_run_workflow

Run workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2RunWorkflowRequest(
    request_body={
        'key': 'string',
    },
    workflow_id='string',
)

res = s.orchestration.v2_run_workflow(req)

if res.v2_run_workflow_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.V2RunWorkflowRequest](../../models/operations/v2runworkflowrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.V2RunWorkflowResponse](../../models/operations/v2runworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## v2_send_event

Send an event to a running workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.V2SendEventRequest(
    request_body=operations.V2SendEventRequestBody(
        name='string',
    ),
    instance_id='string',
)

res = s.orchestration.v2_send_event(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V2SendEventRequest](../../models/operations/v2sendeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.V2SendEventResponse](../../models/operations/v2sendeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
