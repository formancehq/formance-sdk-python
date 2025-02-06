# Search
(*search*)

## Overview

### Available Operations

* [search](#search) - Search
* [searchget_server_info](#searchget_server_info) - Get server info

## search

ElasticSearch query engine

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

    res = sdk.search.search(request={
        "after": [
            "users:002",
        ],
        "cursor": "YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=",
        "ledgers": [
            "quickstart",
        ],
        "policy": "OR",
        "sort": "id:asc",
        "terms": [
            "destination=central_bank1",
        ],
    })

    assert res.response is not None

    # Handle response
    print(res.response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.Query](../../models/shared/query.md)                        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.SearchResponse](../../models/operations/searchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## searchget_server_info

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

    res = sdk.search.searchget_server_info()

    assert res.server_info is not None

    # Handle response
    print(res.server_info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.SearchgetServerInfoResponse](../../models/operations/searchgetserverinforesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |