# Ledger
(*ledger*)

## Overview

### Available Operations

* [get_info](#get_info) - Show server information
* [get_metrics](#get_metrics) - Read in memory metrics

## get_info

Show server information

### Example Usage

<!-- UsageSnippet language="python" operationID="v2GetInfo" method="get" path="/api/ledger/_/info" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.get_info()

    assert res.v2_config_info_response is not None

    # Handle response
    print(res.v2_config_info_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.V2GetInfoResponse](../../models/operations/v2getinforesponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |

## get_metrics

Read in memory metrics

### Example Usage

<!-- UsageSnippet language="python" operationID="getMetrics" method="get" path="/api/ledger/_/metrics" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.ledger.get_metrics()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetMetricsResponse](../../models/operations/getmetricsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.V2ErrorResponse | default                | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |