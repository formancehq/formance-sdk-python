# TransferInitiationPayments


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `created_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | When the payment was produced                                                |
| `error`                                                                      | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | Why the payment failed, absent when it succeeded                             |
| `payment_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | Identifier of the payment produced by the initiation                         |
| `status`                                                                     | [payments.LegacyPaymentStatus](../../models/payments/legacypaymentstatus.md) | :heavy_check_mark:                                                           | Status of a payment as reported by the legacy payments API                   |