# CreatedTransactionRule

Rule scoped to MirrorCreatedTransaction. Inside `match`, `log` is the created-transaction proto directly (e.g. `log.metadata["k"]`).



## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `actions`                                                                                      | List[[ledger_v3.CreatedTransactionAction](../../models/ledger_v3/createdtransactionaction.md)] | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `match`                                                                                        | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | N/A                                                                                            |