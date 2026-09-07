# V3OrdersCursorResponseCursor

Paginated cursor wrapping the list of orders


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `data`                                                     | List[[payments.V3Order](../../models/payments/v3order.md)] | :heavy_check_mark:                                         | N/A                                                        |                                                            |
| `has_more`                                                 | *bool*                                                     | :heavy_check_mark:                                         | N/A                                                        | false                                                      |
| `next`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `page_size`                                                | *int*                                                      | :heavy_check_mark:                                         | N/A                                                        | 15                                                         |
| `previous`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=               |