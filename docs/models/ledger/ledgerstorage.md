# LedgerStorage

Storage backend the ledgers are held in


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `driver`                                          | *str*                                             | :heavy_check_mark:                                | Name of the storage driver backing the ledgers    |
| `ledgers`                                         | List[*str*]                                       | :heavy_check_mark:                                | Names of the ledgers held in this storage backend |