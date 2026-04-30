# CreditWalletRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `monetary`                                                           | [orchestration.Monetary](../../models/orchestration/monetary.md)     | :heavy_check_mark:                                                   | N/A                                                                  |
| `balance`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The balance to credit                                                |
| `metadata`                                                           | Dict[str, *str*]                                                     | :heavy_check_mark:                                                   | Metadata associated with the wallet.                                 |
| `reference`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `sources`                                                            | List[[orchestration.Subject](../../models/orchestration/subject.md)] | :heavy_check_mark:                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |