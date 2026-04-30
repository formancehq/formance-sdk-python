# ~~Search.V1~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

### Available Operations

* [~~get_server_info_search~~](#get_server_info_search) - Get server info :warning: **Deprecated**
* [~~search~~](#search) - search.v1 :warning: **Deprecated**

## ~~get_server_info_search~~

Get server info

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getServerInfo_search" method="get" path="/api/search/_info" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.search.v1.get_server_info_search()

    assert res.server_info is not None

    # Handle response
    print(res.server_info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.GetServerInfoSearchResponse](../../models/operations/getserverinfosearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~search~~

Elasticsearch.v1 query engine

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="search" method="post" path="/api/search/" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.search.v1.search(request={
        "after": [
            "users:002",
        ],
        "cursor": "YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=",
        "ledgers": [
            "quickstart",
        ],
        "policy": "OR",
        "raw": {},
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
| `request`                                                           | [search.Query](../../models/search/query.md)                        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.SearchResponse](../../models/operations/searchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |