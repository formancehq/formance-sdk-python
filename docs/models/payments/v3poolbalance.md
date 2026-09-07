# V3PoolBalance


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `amount`                                                                | *int*                                                                   | :heavy_check_mark:                                                      | Total held across the pool for this asset, in the asset's smallest unit |
| `asset`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | Asset the balance is denominated in                                     |
| `related_accounts`                                                      | List[*str*]                                                             | :heavy_minus_sign:                                                      | Accounts contributing to this balance                                   |