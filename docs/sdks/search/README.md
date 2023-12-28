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
    security=shared.Security(
        authorization="",
    ),
)

req = shared.Query(
    after=[
        'u',
        's',
        'e',
        'r',
        's',
        ':',
        '0',
        '0',
        '2',
    ],
    cursor='YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=',
    ledgers=[
        'q',
        'u',
        'i',
        'c',
        'k',
        's',
        't',
        'a',
        'r',
        't',
    ],
    policy='OR',
    raw=shared.QueryRaw(),
    sort='id:asc',
    terms=[
        'd',
        'e',
        's',
        't',
        'i',
        'n',
        'a',
        't',
        'i',
        'o',
        'n',
        '=',
        'c',
        'e',
        'n',
        't',
        'r',
        'a',
        'l',
        '_',
        'b',
        'a',
        'n',
        'k',
        '1',
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


## searchget_server_info

Get server info

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        authorization="",
    ),
)


res = s.search.searchget_server_info()

if res.server_info is not None:
    # handle response
    pass
```


### Response

**[operations.SearchgetServerInfoResponse](../../models/operations/searchgetserverinforesponse.md)**

