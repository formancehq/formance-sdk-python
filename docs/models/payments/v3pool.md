# V3Pool

A named group of accounts whose balances are aggregated together


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `created_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | When the pool was created                                                    |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique identifier of the pool                                                |
| `name`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Human-readable name of the pool                                              |
| `pool_accounts`                                                              | List[*str*]                                                                  | :heavy_check_mark:                                                           | Accounts currently in the pool                                               |
| `query`                                                                      | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | Filter selecting the accounts a dynamic pool contains                        |
| `type`                                                                       | [Optional[payments.V3PoolTypeEnum]](../../models/payments/v3pooltypeenum.md) | :heavy_minus_sign:                                                           | Whether a pool holds a fixed account list or is driven by a query            |