# ReconciliationRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `reconciled_at_ledger`                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Point in time at which the ledger side is evaluated                  | 2021-01-01T00:00:00.000Z                                             |
| `reconciled_at_payments`                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Point in time at which the payments side is evaluated                | 2021-01-01T00:00:00.000Z                                             |