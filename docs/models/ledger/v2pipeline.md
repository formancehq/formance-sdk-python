# V2Pipeline


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `enabled`                                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `exporter_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Identifier of the exporter the pipeline feeds                        |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `last_log_id`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `ledger`                                                             | *str*                                                                | :heavy_check_mark:                                                   | Name of the ledger the pipeline reads from                           |