# V2LedgerInfo

Runtime information about a ledger, including the state of its storage migrations


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `name`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Name of the ledger                                                                   | ledger001                                                                            |
| `storage`                                                                            | [Optional[ledger.V2LedgerInfoStorage]](../../models/ledger/v2ledgerinfostorage.md)   | :heavy_minus_sign:                                                                   | Storage backend information, including the migrations applied to the ledger's bucket |                                                                                      |