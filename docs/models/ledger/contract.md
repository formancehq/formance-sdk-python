# Contract


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `account`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | Account address, or pattern, the contract applies to | users:001                                            |
| `expr`                                               | [ledger.Expr](../../models/ledger/expr.md)           | :heavy_check_mark:                                   | Expression the account's balances must satisfy       |                                                      |