# BankAccountRelatedAccounts


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `account_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | Identifier of the provider-side account                                 |
| `connector_id`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | Identifier of the connector holding the provider-side account           |
| `created_at`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_check_mark:                                                      | When the bank account was forwarded to this provider                    |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | Unique identifier of the link between the bank account and the provider |
| `provider`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | Name of the payment provider behind the connector                       |