# Wallet


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the wallet was created                                          |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The unique ID of the wallet.                                         |
| `ledger`                                                             | *str*                                                                | :heavy_check_mark:                                                   | Name of the ledger backing this wallet                               |
| `metadata`                                                           | Dict[str, *str*]                                                     | :heavy_check_mark:                                                   | Metadata associated with the wallet.                                 |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Human-readable name of the wallet                                    |