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
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Query(
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
)

res = s.search.search(req)

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
| errors.SDKError | 400-600         | */*             |

## searchget_server_info

Get server info

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
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
| errors.SDKError | 400-600         | */*             |
