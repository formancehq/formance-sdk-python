# V3DeletePreparedQueryRequest


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `ledger_name`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | Name of the ledger                                                          |
| `query_name`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | Prepared query name, URL-encoded as one path segment. Decoded exactly once. |