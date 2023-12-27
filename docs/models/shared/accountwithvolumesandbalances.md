# AccountWithVolumesAndBalances


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `address`                                          | *str*                                              | :heavy_check_mark:                                 | N/A                                                | users:001                                          |
| `balances`                                         | Dict[str, *int*]                                   | :heavy_minus_sign:                                 | N/A                                                | [object Object]                                    |
| `metadata`                                         | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                | [object Object]                                    |
| `type`                                             | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                | virtual                                            |
| `volumes`                                          | Dict[str, [Volume](../../models/shared/volume.md)] | :heavy_minus_sign:                                 | N/A                                                | [object Object]                                    |