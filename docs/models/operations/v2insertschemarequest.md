# V2InsertSchemaRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `idempotency_key`                                            | *Optional[str]*                                              | :heavy_minus_sign:                                           | Use an idempotency key                                       |                                                              |
| `v2_schema_data`                                             | [ledger.V2SchemaData2](../../models/ledger/v2schemadata2.md) | :heavy_check_mark:                                           | N/A                                                          |                                                              |
| `ledger`                                                     | *str*                                                        | :heavy_check_mark:                                           | Name of the ledger.                                          | ledger001                                                    |
| `version`                                                    | *str*                                                        | :heavy_check_mark:                                           | Schema version.                                              | v1.0.0                                                       |