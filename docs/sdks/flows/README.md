# flows

### Available Operations

* [flowsget_server_info](#flowsget_server_info) - Get server info
* [cancel_event](#cancel_event) - Cancel a running workflow
* [create_workflow](#create_workflow) - Create workflow
* [get_instance](#get_instance) - Get a workflow instance by id
* [get_instance_history](#get_instance_history) - Get a workflow instance history by id
* [get_instance_stage_history](#get_instance_stage_history) - Get a workflow instance stage history
* [get_workflow](#get_workflow) - Get a flow by id
* [list_instances](#list_instances) - List instances of a workflow
* [list_workflows](#list_workflows) - List registered workflows
* [run_workflow](#run_workflow) - Run workflow
* [send_event](#send_event) - Send an event to a running workflow

## flowsget_server_info

Get server info

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)


res = s.flows.flowsget_server_info()

if res.server_info is not None:
    # handle response
```


### Response

**[operations.FlowsgetServerInfoResponse](../../models/operations/flowsgetserverinforesponse.md)**


## cancel_event

Cancel a running workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.CancelEventRequest(
    instance_id='dolorem',
)

res = s.flows.cancel_event(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CancelEventRequest](../../models/operations/canceleventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CancelEventResponse](../../models/operations/canceleventresponse.md)**


## create_workflow

Create a workflow

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = shared.CreateWorkflowRequest(
    name='Rose Rolfson',
    stages=[
        {
            "excepturi": 'accusantium',
            "iure": 'culpa',
        },
        {
            "sapiente": 'architecto',
            "mollitia": 'dolorem',
            "culpa": 'consequuntur',
            "repellat": 'mollitia',
        },
    ],
)

res = s.flows.create_workflow(req)

if res.create_workflow_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CreateWorkflowRequest](../../models/shared/createworkflowrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateWorkflowResponse](../../models/operations/createworkflowresponse.md)**


## get_instance

Get a workflow instance by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetInstanceRequest(
    instance_id='occaecati',
)

res = s.flows.get_instance(req)

if res.get_workflow_instance_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetInstanceRequest](../../models/operations/getinstancerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetInstanceResponse](../../models/operations/getinstanceresponse.md)**


## get_instance_history

Get a workflow instance history by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetInstanceHistoryRequest(
    instance_id='numquam',
)

res = s.flows.get_instance_history(req)

if res.get_workflow_instance_history_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetInstanceHistoryRequest](../../models/operations/getinstancehistoryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetInstanceHistoryResponse](../../models/operations/getinstancehistoryresponse.md)**


## get_instance_stage_history

Get a workflow instance stage history

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetInstanceStageHistoryRequest(
    instance_id='commodi',
    number=466311,
)

res = s.flows.get_instance_stage_history(req)

if res.get_workflow_instance_history_stage_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetInstanceStageHistoryRequest](../../models/operations/getinstancestagehistoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetInstanceStageHistoryResponse](../../models/operations/getinstancestagehistoryresponse.md)**


## get_workflow

Get a flow by id

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetWorkflowRequest(
    flow_id='molestiae',
)

res = s.flows.get_workflow(req)

if res.get_workflow_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetWorkflowRequest](../../models/operations/getworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetWorkflowResponse](../../models/operations/getworkflowresponse.md)**


## list_instances

List instances of a workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.ListInstancesRequest(
    running=False,
    workflow_id='velit',
)

res = s.flows.list_instances(req)

if res.list_runs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListInstancesRequest](../../models/operations/listinstancesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListInstancesResponse](../../models/operations/listinstancesresponse.md)**


## list_workflows

List registered workflows

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)


res = s.flows.list_workflows()

if res.list_workflows_response is not None:
    # handle response
```


### Response

**[operations.ListWorkflowsResponse](../../models/operations/listworkflowsresponse.md)**


## run_workflow

Run workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.RunWorkflowRequest(
    request_body={
        "quia": 'quis',
        "vitae": 'laborum',
        "animi": 'enim',
    },
    wait=False,
    workflow_id='odit',
)

res = s.flows.run_workflow(req)

if res.run_workflow_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RunWorkflowRequest](../../models/operations/runworkflowrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.RunWorkflowResponse](../../models/operations/runworkflowresponse.md)**


## send_event

Send an event to a running workflow

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.SendEventRequest(
    request_body=operations.SendEventRequestBody(
        name='Jimmy Wiegand',
    ),
    instance_id='possimus',
)

res = s.flows.send_event(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.SendEventRequest](../../models/operations/sendeventrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.SendEventResponse](../../models/operations/sendeventresponse.md)**
