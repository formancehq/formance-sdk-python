# ConnectionCursorCursor


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `data`                                                                   | List[[connectivity.Connection](../../models/connectivity/connection.md)] | :heavy_check_mark:                                                       | N/A                                                                      |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | N/A                                                                      |
| `next`                                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Cursor of the next page; absent on the last page                         |
| `page_size`                                                              | *int*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |