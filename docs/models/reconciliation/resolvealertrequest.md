# ResolveAlertRequest

Mark an alert resolved. When `transactionRefs` is non-empty the
resolution kind is recorded as `fixed_by_booking`.



## Fields

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `by`                                                                                                                 | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | Who is resolving the alert                                                                                           |
| `note`                                                                                                               | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Free-text note to record with the resolution                                                                         |
| `transaction_refs`                                                                                                   | List[*str*]                                                                                                          | :heavy_minus_sign:                                                                                                   | References of the transactions booked to correct the break. Supplying any records the resolution as fixed_by_booking |