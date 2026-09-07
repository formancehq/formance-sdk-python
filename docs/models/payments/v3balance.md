# V3Balance


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Identifier of the account this balance belongs to                    |
| `asset`                                                              | *str*                                                                | :heavy_check_mark:                                                   | Asset the balance is denominated in                                  |
| `balance`                                                            | *int*                                                                | :heavy_check_mark:                                                   | Amount held, in the asset's smallest unit                            |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Start of the period this balance covers                              |
| `last_updated_at`                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the balance was last refreshed from the provider                |