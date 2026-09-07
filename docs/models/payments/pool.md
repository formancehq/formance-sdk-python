# Pool

A named group of accounts whose balances are aggregated together


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `accounts`                                                               | List[*str*]                                                              | :heavy_check_mark:                                                       | Accounts currently in the pool                                           |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique identifier of the pool                                            |
| `name`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | Human-readable name of the pool                                          |
| `query`                                                                  | Dict[str, *Any*]                                                         | :heavy_minus_sign:                                                       | Filter selecting the accounts a dynamic pool contains                    |
| `type`                                                                   | [Optional[payments.PoolTypeEnum]](../../models/payments/pooltypeenum.md) | :heavy_minus_sign:                                                       | Whether a pool holds a fixed account list or is driven by a query        |