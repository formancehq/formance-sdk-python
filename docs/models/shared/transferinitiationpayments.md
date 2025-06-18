# TransferInitiationPayments


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `error`                                                              | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `payment_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `status`                                                             | [shared.PaymentStatus](../../models/shared/paymentstatus.md)         | :heavy_check_mark:                                                   | N/A                                                                  |