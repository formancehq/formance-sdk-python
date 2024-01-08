# Reconciliation
(*reconciliation*)

### Available Operations

* [create_policy](#create_policy) - Create a policy
* [delete_policy](#delete_policy) - Delete a policy
* [get_policy](#get_policy) - Get a policy
* [get_reconciliation](#get_reconciliation) - Get a reconciliation
* [list_policies](#list_policies) - List policies
* [list_reconciliations](#list_reconciliations) - List reconciliations
* [reconcile](#reconcile) - Reconcile using a policy
* [reconciliationget_server_info](#reconciliationget_server_info) - Get server info

## create_policy

Create a policy

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.PolicyRequest(
    ledger_name='default',
    ledger_query={
        'key': 'string',
    },
    name='XXX',
    payments_pool_id='XXX',
)

res = s.reconciliation.create_policy(req)

if res.policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.PolicyRequest](../../models/shared/policyrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreatePolicyResponse](../../models/operations/createpolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_policy

Delete a policy by its id.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.DeletePolicyRequest(
    policy_id='string',
)

res = s.reconciliation.delete_policy(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeletePolicyRequest](../../models/operations/deletepolicyrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeletePolicyResponse](../../models/operations/deletepolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_policy

Get a policy

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetPolicyRequest(
    policy_id='string',
)

res = s.reconciliation.get_policy(req)

if res.policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetPolicyRequest](../../models/operations/getpolicyrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetPolicyResponse](../../models/operations/getpolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_reconciliation

Get a reconciliation

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetReconciliationRequest(
    reconciliation_id='string',
)

res = s.reconciliation.get_reconciliation(req)

if res.reconciliation_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetReconciliationRequest](../../models/operations/getreconciliationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetReconciliationResponse](../../models/operations/getreconciliationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_policies

List policies

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListPoliciesRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.reconciliation.list_policies(req)

if res.policies_cursor_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPoliciesRequest](../../models/operations/listpoliciesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListPoliciesResponse](../../models/operations/listpoliciesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_reconciliations

List reconciliations

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ListReconciliationsRequest(
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
)

res = s.reconciliation.list_reconciliations(req)

if res.reconciliations_cursor_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListReconciliationsRequest](../../models/operations/listreconciliationsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ListReconciliationsResponse](../../models/operations/listreconciliationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## reconcile

Reconcile using a policy

### Example Usage

```python
import dateutil.parser
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.ReconcileRequest(
    reconciliation_request=shared.ReconciliationRequest(
        reconciled_at_ledger=dateutil.parser.isoparse('2021-01-01T00:00:00.000Z'),
        reconciled_at_payments=dateutil.parser.isoparse('2021-01-01T00:00:00.000Z'),
    ),
    policy_id='string',
)

res = s.reconciliation.reconcile(req)

if res.reconciliation_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ReconcileRequest](../../models/operations/reconcilerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ReconcileResponse](../../models/operations/reconcileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## reconciliationget_server_info

Get server info

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.reconciliation.reconciliationget_server_info()

if res.server_info is not None:
    # handle response
    pass
```


### Response

**[operations.ReconciliationgetServerInfoResponse](../../models/operations/reconciliationgetserverinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
