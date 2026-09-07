# V3ReversePaymentInitiationRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `amount`                                                                 | *int*                                                                    | :heavy_check_mark:                                                       | Amount to reverse, in the asset's smallest unit                          |
| `asset`                                                                  | *str*                                                                    | :heavy_check_mark:                                                       | Asset the reversal is denominated in                                     |
| `description`                                                            | *str*                                                                    | :heavy_check_mark:                                                       | Human-readable reason for the reversal                                   |
| `metadata`                                                               | Dict[str, *str*]                                                         | :heavy_minus_sign:                                                       | Arbitrary key/value pairs attached to the resource                       |
| `reference`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | Caller-supplied identifier for the reversal, used to deduplicate retries |