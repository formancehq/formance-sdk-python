# V2SchemasCursor

Paginated cursor over the ledger's schemas


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `data`                                                   | List[[ledger.V2Schema](../../models/ledger/v2schema.md)] | :heavy_check_mark:                                       | The schemas on this page                                 |                                                          |
| `has_more`                                               | *bool*                                                   | :heavy_check_mark:                                       | Whether further pages are available                      |                                                          |
| `next`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | Cursor for the next page, absent on the last page        | aW0gdmVuaWFtLCBxdWlzIG5vc3RydWQ=                         |
| `page_size`                                              | *int*                                                    | :heavy_check_mark:                                       | Number of items requested per page                       |                                                          |
| `previous`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | Cursor for the previous page, absent on the first page   | YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=             |