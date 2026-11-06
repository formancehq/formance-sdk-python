# TemporalStats


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `first_seen`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `last_seen`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `peak_hours`                                                         | List[[ledger_v3.HourBucket](../../models/ledger_v3/hourbucket.md)]   | :heavy_minus_sign:                                                   | N/A                                                                  |
| `transactions_per_day`                                               | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  |