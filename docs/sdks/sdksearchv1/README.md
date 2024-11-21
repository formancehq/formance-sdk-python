# SDKSearchV1
(*search.v1*)

## Overview

### Available Operations

* [~~search~~](#search) - search.v1 :warning: **Deprecated**
* [~~searchget_server_info~~](#searchget_server_info) - Get server info :warning: **Deprecated**

## ~~search~~

Elasticsearch.v1 query engine

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

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


res = s.search.v1.search(request=shared.Query(
    after=[
        'users:002',
    ],
    cursor='YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=',
    ledgers=[
        'quickstart',
    ],
    policy='OR',
    raw=shared.QueryRaw(),
    sort='id:asc',
    terms=[
        'destination=central_bank1',
    ],
))

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `request`                                    | [shared.Query](../../models/shared/query.md) | :heavy_check_mark:                           | The request object to use for the request.   |

### Response

**[operations.SearchResponse](../../models/operations/searchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~searchget_server_info~~

Get server info

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

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


res = s.search.v1.searchget_server_info()

if res.server_info is not None:
    # handle response
    pass

```

### Response

**[operations.SearchgetServerInfoResponse](../../models/operations/searchgetserverinforesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |