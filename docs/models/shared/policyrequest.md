# PolicyRequest


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `ledger_name`                                         | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   | default                                               |
| `ledger_query`                                        | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   | {"$match": {"metadata[reconciliation]": "pool:main"}} |
| `name`                                                | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   | XXX                                                   |
| `payments_pool_id`                                    | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   | XXX                                                   |