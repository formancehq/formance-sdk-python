# ConnectorCursorCursor


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data`                                                                 | List[[connectivity.Connector](../../models/connectivity/connector.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `has_more`                                                             | *bool*                                                                 | :heavy_check_mark:                                                     | N/A                                                                    |
| `next`                                                                 | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Cursor of the next page; absent on the last page                       |
| `page_size`                                                            | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |