# Search
(*search*)

### Available Operations

* [search](#search) - Search
* [searchget_server_info](#searchget_server_info) - Get server info

## search

ElasticSearch query engine

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.search.search(request=shared.Query(
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## searchget_server_info

Get server info

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="<YOUR_AUTHORIZATION_HERE>",
)


res = s.search.searchget_server_info()

if res.server_info is not None:
    # handle response
    pass

```


### Response

**[operations.SearchgetServerInfoResponse](../../models/operations/searchgetserverinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
