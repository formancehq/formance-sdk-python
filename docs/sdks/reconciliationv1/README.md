# Reconciliation.V1

## Overview

### Available Operations

* [accept_alert](#accept_alert) - Accept an alert (accepted_by_business)
* [ack_alert](#ack_alert) - Acknowledge an alert
* [create_policy](#create_policy) - Create a policy
* [create_rule](#create_rule) - Create a rule
* [delete_policy](#delete_policy) - Delete a policy
* [delete_rule](#delete_rule) - Delete a rule (cascades to evaluations + alerts + alert events)
* [evaluate_rule](#evaluate_rule) - Evaluate a rule now
* [get_alert](#get_alert) - Get an alert
* [get_evaluation](#get_evaluation) - Get an evaluation
* [get_policy](#get_policy) - Get a policy
* [get_reconciliation](#get_reconciliation) - Get a reconciliation
* [get_rule](#get_rule) - Get a rule
* [get_server_info_reconciliation](#get_server_info_reconciliation) - Get server info
* [list_alert_events](#list_alert_events) - List alert events (append-only timeline)
* [list_alerts](#list_alerts) - List alerts
* [list_evaluations](#list_evaluations) - List evaluations
* [list_policies](#list_policies) - List policies
* [list_reconciliations](#list_reconciliations) - List reconciliations
* [list_rules](#list_rules) - List rules
* [patch_rule](#patch_rule) - Patch a rule (partial update)
* [reconcile](#reconcile) - Reconcile using a policy
* [resolve_alert](#resolve_alert) - Resolve an alert (fixed_by_booking)
* [snooze_alert](#snooze_alert) - Snooze an alert's notifications until a future instant
* [unsnooze_alert](#unsnooze_alert) - Lift a snooze early

## accept_alert

Accept an alert (accepted_by_business)

### Example Usage

<!-- UsageSnippet language="python" operationID="acceptAlert" method="post" path="/api/reconciliation/alerts/{alertID}/accept" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.accept_alert(request={
        "accept_alert_request": {
            "by": "<value>",
            "note": "<value>",
        },
        "alert_id": "5550ef95-072d-4bbb-9d3b-6a9dd307b2bd",
    })

    assert res.alert_response is not None

    # Handle response
    print(res.alert_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.AcceptAlertRequest](../../models/operations/acceptalertrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.AcceptAlertResponse](../../models/operations/acceptalertresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## ack_alert

Acknowledge an alert

### Example Usage

<!-- UsageSnippet language="python" operationID="ackAlert" method="post" path="/api/reconciliation/alerts/{alertID}/ack" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.ack_alert(request={
        "ack_alert_request": {
            "by": "ops@buildr.com",
        },
        "alert_id": "5439ab64-6482-49fb-993f-3411bfe19fef",
    })

    assert res.alert_response is not None

    # Handle response
    print(res.alert_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.AckAlertRequest](../../models/operations/ackalertrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.AckAlertResponse](../../models/operations/ackalertresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## create_policy

Create a policy

### Example Usage

<!-- UsageSnippet language="python" operationID="createPolicy" method="post" path="/api/reconciliation/policies" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.create_policy(request={
        "ledger_name": "default",
        "ledger_query": {
            "key": "<value>",
        },
        "name": "XXX",
        "payments_pool_id": "XXX",
    })

    assert res.policy_response is not None

    # Handle response
    print(res.policy_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [reconciliation.PolicyRequest](../../models/reconciliation/policyrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.CreatePolicyResponse](../../models/operations/createpolicyresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## create_rule

Create a rule

### Example Usage

<!-- UsageSnippet language="python" operationID="createRule" method="post" path="/api/reconciliation/rules" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import reconciliation, shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.create_rule(request={
        "name": "<value>",
        "schedule": {
            "expr": "*/15 * * * *",
            "kind": reconciliation.ScheduleKind.ON_DEMAND,
            "safety_margin": "30s",
            "tz": "UTC",
        },
        "template_kind": reconciliation.TemplateKind.LEDGER_VS_POOL_DRIFT,
        "template_spec": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
    })

    assert res.rule_response is not None

    # Handle response
    print(res.rule_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [reconciliation.RuleRequest](../../models/reconciliation/rulerequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.CreateRuleResponse](../../models/operations/createruleresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## delete_policy

Delete a policy by its id.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePolicy" method="delete" path="/api/reconciliation/policies/{policyID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.delete_policy(request={
        "policy_id": "XXX",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeletePolicyRequest](../../models/operations/deletepolicyrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.DeletePolicyResponse](../../models/operations/deletepolicyresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## delete_rule

Delete a rule (cascades to evaluations + alerts + alert events)

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteRule" method="delete" path="/api/reconciliation/rules/{ruleID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.delete_rule(request={
        "rule_id": "3254b217-2184-4bf4-bbc8-b529fa29bd7c",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteRuleRequest](../../models/operations/deleterulerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.DeleteRuleResponse](../../models/operations/deleteruleresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## evaluate_rule

Evaluate a rule now

### Example Usage

<!-- UsageSnippet language="python" operationID="evaluateRule" method="post" path="/api/reconciliation/rules/{ruleID}/evaluate" -->
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

    res = sdk.reconciliation.v1.evaluate_rule(request={
        "evaluate_rule_request": {
            "safety_margin": "30s",
            "source_pi_ts": {
                "ledger:main#0": parse_datetime("2026-06-30T23:59:59Z"),
                "pool:acct#0": parse_datetime("2026-06-30T23:00:00Z"),
            },
        },
        "rule_id": "e9d27cb2-b7fc-4383-b319-936c01a66703",
    })

    assert res.evaluation_response is not None

    # Handle response
    print(res.evaluation_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.EvaluateRuleRequest](../../models/operations/evaluaterulerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.EvaluateRuleResponse](../../models/operations/evaluateruleresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_alert

Get an alert

### Example Usage

<!-- UsageSnippet language="python" operationID="getAlert" method="get" path="/api/reconciliation/alerts/{alertID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.get_alert(request={
        "alert_id": "c7c54af9-81a4-4208-844b-4f25f89cf8a1",
    })

    assert res.alert_response is not None

    # Handle response
    print(res.alert_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetAlertRequest](../../models/operations/getalertrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.GetAlertResponse](../../models/operations/getalertresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_evaluation

Get an evaluation

### Example Usage

<!-- UsageSnippet language="python" operationID="getEvaluation" method="get" path="/api/reconciliation/evaluations/{evaluationID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.get_evaluation(request={
        "evaluation_id": "121717d3-a7d1-444d-9d11-6ea2dc0d3db5",
    })

    assert res.evaluation_response is not None

    # Handle response
    print(res.evaluation_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetEvaluationRequest](../../models/operations/getevaluationrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetEvaluationResponse](../../models/operations/getevaluationresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_policy

Get a policy

### Example Usage

<!-- UsageSnippet language="python" operationID="getPolicy" method="get" path="/api/reconciliation/policies/{policyID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.get_policy(request={
        "policy_id": "XXX",
    })

    assert res.policy_response is not None

    # Handle response
    print(res.policy_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetPolicyRequest](../../models/operations/getpolicyrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetPolicyResponse](../../models/operations/getpolicyresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_reconciliation

Get a reconciliation

### Example Usage

<!-- UsageSnippet language="python" operationID="getReconciliation" method="get" path="/api/reconciliation/reconciliations/{reconciliationID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.get_reconciliation(request={
        "reconciliation_id": "XXX",
    })

    assert res.reconciliation_response is not None

    # Handle response
    print(res.reconciliation_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetReconciliationRequest](../../models/operations/getreconciliationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetReconciliationResponse](../../models/operations/getreconciliationresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_rule

Get a rule

### Example Usage

<!-- UsageSnippet language="python" operationID="getRule" method="get" path="/api/reconciliation/rules/{ruleID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.get_rule(request={
        "rule_id": "fd71d712-041d-4271-b7c5-c9adac177f52",
    })

    assert res.rule_response is not None

    # Handle response
    print(res.rule_response)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetRuleRequest](../../models/operations/getrulerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.GetRuleResponse](../../models/operations/getruleresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_server_info_reconciliation

Get server info

### Example Usage

<!-- UsageSnippet language="python" operationID="getServerInfo_reconciliation" method="get" path="/api/reconciliation/_info" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.get_server_info_reconciliation()

    assert res.server_info is not None

    # Handle response
    print(res.server_info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetServerInfoReconciliationResponse](../../models/operations/getserverinforeconciliationresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## list_alert_events

Returns a page of the events recorded for this alert — every evaluation
that touched it plus every manual transition. The list is append-only;
events are never modified or deleted. Ordered most-recent-first and
cursor-paginated: a long-lived alert's timeline is unbounded (one row per
failing evaluation), so callers must page through it.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAlertEvents" method="get" path="/api/reconciliation/alerts/{alertID}/events" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.list_alert_events(request={
        "alert_id": "259536e6-acd5-4e38-9154-10e46ea2bc63",
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.alert_events_cursor_response is not None

    # Handle response
    print(res.alert_events_cursor_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListAlertEventsRequest](../../models/operations/listalerteventsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListAlertEventsResponse](../../models/operations/listalerteventsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## list_alerts

List alerts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAlerts" method="get" path="/api/reconciliation/alerts" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.list_alerts(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.alerts_cursor_response is not None

    # Handle response
    print(res.alerts_cursor_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListAlertsRequest](../../models/operations/listalertsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.ListAlertsResponse](../../models/operations/listalertsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## list_evaluations

List evaluations

### Example Usage

<!-- UsageSnippet language="python" operationID="listEvaluations" method="get" path="/api/reconciliation/evaluations" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.list_evaluations(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.evaluations_cursor_response is not None

    # Handle response
    print(res.evaluations_cursor_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListEvaluationsRequest](../../models/operations/listevaluationsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListEvaluationsResponse](../../models/operations/listevaluationsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## list_policies

List policies

### Example Usage

<!-- UsageSnippet language="python" operationID="listPolicies" method="get" path="/api/reconciliation/policies" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.list_policies(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.policies_cursor_response is not None

    # Handle response
    print(res.policies_cursor_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPoliciesRequest](../../models/operations/listpoliciesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListPoliciesResponse](../../models/operations/listpoliciesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## list_reconciliations

List reconciliations

### Example Usage

<!-- UsageSnippet language="python" operationID="listReconciliations" method="get" path="/api/reconciliation/reconciliations" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.list_reconciliations(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.reconciliations_cursor_response is not None

    # Handle response
    print(res.reconciliations_cursor_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListReconciliationsRequest](../../models/operations/listreconciliationsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListReconciliationsResponse](../../models/operations/listreconciliationsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## list_rules

List rules

### Example Usage

<!-- UsageSnippet language="python" operationID="listRules" method="get" path="/api/reconciliation/rules" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.list_rules(request={
        "cursor": "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        "page_size": 100,
    })

    assert res.rules_cursor_response is not None

    # Handle response
    print(res.rules_cursor_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListRulesRequest](../../models/operations/listrulesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.ListRulesResponse](../../models/operations/listrulesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## patch_rule

Patch a rule (partial update)

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRule" method="patch" path="/api/reconciliation/rules/{ruleID}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import reconciliation, shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.patch_rule(request={
        "rule_patch_request": {
            "schedule": {
                "expr": "*/15 * * * *",
                "kind": reconciliation.ScheduleKind.CRON,
                "safety_margin": "30s",
                "tz": "UTC",
            },
        },
        "rule_id": "0b4aa7b1-cc5d-4700-91ec-4983510fef86",
    })

    assert res.rule_response is not None

    # Handle response
    print(res.rule_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PatchRuleRequest](../../models/operations/patchrulerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.PatchRuleResponse](../../models/operations/patchruleresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## reconcile

Reconcile using a policy

### Example Usage

<!-- UsageSnippet language="python" operationID="reconcile" method="post" path="/api/reconciliation/policies/{policyID}/reconciliation" -->
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

    res = sdk.reconciliation.v1.reconcile(request={
        "reconciliation_request": {
            "reconciled_at_ledger": parse_datetime("2021-01-01T00:00:00.000Z"),
            "reconciled_at_payments": parse_datetime("2021-01-01T00:00:00.000Z"),
        },
        "policy_id": "XXX",
    })

    assert res.reconciliation_response is not None

    # Handle response
    print(res.reconciliation_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ReconcileRequest](../../models/operations/reconcilerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.ReconcileResponse](../../models/operations/reconcileresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## resolve_alert

Resolve an alert (fixed_by_booking)

### Example Usage

<!-- UsageSnippet language="python" operationID="resolveAlert" method="post" path="/api/reconciliation/alerts/{alertID}/resolve" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.resolve_alert(request={
        "resolve_alert_request": {
            "by": "<value>",
        },
        "alert_id": "53527ec3-b39f-4eee-ac1d-6e2bad87f240",
    })

    assert res.alert_response is not None

    # Handle response
    print(res.alert_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ResolveAlertRequest](../../models/operations/resolvealertrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ResolveAlertResponse](../../models/operations/resolvealertresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## snooze_alert

Mutes the alert's webhook notifications until `until`. The alert keeps
failing, keeps its status, and keeps counting against period-green —
only its notifications are suppressed, even if the discrepancy changes.
The first failing evaluation at or after `until` clears the snooze and
notifies once. Re-snoozing overwrites the window. Rejects RESOLVED
alerts and a non-future `until`.


### Example Usage

<!-- UsageSnippet language="python" operationID="snoozeAlert" method="post" path="/api/reconciliation/alerts/{alertID}/snooze" -->
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

    res = sdk.reconciliation.v1.snooze_alert(request={
        "snooze_alert_request": {
            "by": "ops@buildr.com",
            "until": parse_datetime("2026-07-17T12:27:27.142Z"),
        },
        "alert_id": "96529a25-9005-499e-a0ec-daa0ae32f4cb",
    })

    assert res.alert_response is not None

    # Handle response
    print(res.alert_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.SnoozeAlertRequest](../../models/operations/snoozealertrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.SnoozeAlertResponse](../../models/operations/snoozealertresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## unsnooze_alert

Clears an active snooze before its window elapses. Idempotent —
unsnoozing an alert that is not snoozed returns it unchanged.


### Example Usage

<!-- UsageSnippet language="python" operationID="unsnoozeAlert" method="post" path="/api/reconciliation/alerts/{alertID}/unsnooze" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.reconciliation.v1.unsnooze_alert(request={
        "unsnooze_alert_request": {
            "by": "ops@buildr.com",
        },
        "alert_id": "a1f12fdd-d9de-483a-b3c6-41ec79a76231",
    })

    assert res.alert_response is not None

    # Handle response
    print(res.alert_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UnsnoozeAlertRequest](../../models/operations/unsnoozealertrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UnsnoozeAlertResponse](../../models/operations/unsnoozealertresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| reconciliation.ErrorsErrorResponse | default                            | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |