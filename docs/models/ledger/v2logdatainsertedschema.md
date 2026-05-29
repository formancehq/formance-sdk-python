# V2LogDataInsertedSchema

Payload for INSERTED_SCHEMA log entries. Contains the schema that was inserted into the ledger.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `v2_schema_data`                                             | [ledger.V2SchemaData1](../../models/ledger/v2schemadata1.md) | :heavy_check_mark:                                           | Complete schema structure with metadata                      |