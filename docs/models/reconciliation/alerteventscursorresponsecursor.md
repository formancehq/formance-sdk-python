# AlertEventsCursorResponseCursor

Paginated cursor wrapping the alert's event log


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | List[[reconciliation.AlertEvent](../../models/reconciliation/alertevent.md)] | :heavy_check_mark:                                                           | N/A                                                                          |
| `has_more`                                                                   | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          |
| `next`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `page_size`                                                                  | *int*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `previous`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |