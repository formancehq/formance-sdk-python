# Payload

Named system payload variants are preserved as supplied, including
nested fields and future sibling variants. Only apply is typed here;
other variants remain open-ended (EN-2781).



## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `__pydantic_extra__`                                         | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `apply`                                                      | [Optional[ledger_v3.Apply]](../../models/ledger_v3/apply.md) | :heavy_minus_sign:                                           | N/A                                                          |