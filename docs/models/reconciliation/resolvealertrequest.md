# ResolveAlertRequest

Mark an alert resolved. When `transactionRefs` is non-empty the
resolution kind is recorded as `fixed_by_booking`.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `by`               | *str*              | :heavy_check_mark: | N/A                |
| `note`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `transaction_refs` | List[*str*]        | :heavy_minus_sign: | N/A                |