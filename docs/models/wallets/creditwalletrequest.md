# CreditWalletRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `monetary`                                                           | [wallets.Monetary](../../models/wallets/monetary.md)                 | :heavy_check_mark:                                                   | N/A                                                                  |
| `balance`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The balance to credit                                                |
| `metadata`                                                           | Dict[str, *str*]                                                     | :heavy_minus_sign:                                                   | Metadata associated with the wallet.                                 |
| `reference`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `sources`                                                            | List[[wallets.Subject](../../models/wallets/subject.md)]             | :heavy_minus_sign:                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |