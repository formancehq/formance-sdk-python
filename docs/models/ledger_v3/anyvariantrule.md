# AnyVariantRule

Rule scoped to every variant. `log` is the full MirrorLogEntry — use `has(log.<variant>)` guards to read variant-specific fields.



## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `actions`                                                                      | List[[ledger_v3.AnyVariantAction](../../models/ledger_v3/anyvariantaction.md)] | :heavy_minus_sign:                                                             | N/A                                                                            |
| `match`                                                                        | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |