# PoolsCursorCursor

Paginated cursor wrapping the list of pools


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `data`                                                 | List[[payments.Pool](../../models/payments/pool.md)]   | :heavy_check_mark:                                     | N/A                                                    |                                                        |
| `has_more`                                             | *bool*                                                 | :heavy_check_mark:                                     | Whether further pages are available                    | false                                                  |
| `next`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Cursor for the next page, absent on the last page      |                                                        |
| `page_size`                                            | *int*                                                  | :heavy_check_mark:                                     | Number of items requested per page                     | 15                                                     |
| `previous`                                             | *Optional[str]*                                        | :heavy_minus_sign:                                     | Cursor for the previous page, absent on the first page | YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=           |