# StatusError

Fixed sanitized failure diagnostic. Unknown or stale failure provenance is failure_unknown. Ingestion failures with known provenance are reported under ingestion instead.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `code`                                                 | [connectivity.Code](../../models/connectivity/code.md) | :heavy_check_mark:                                     | N/A                                                    |
| `message`                                              | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |