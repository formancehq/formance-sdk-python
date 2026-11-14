# ListWalletsResponseCursor

Paginated cursor wrapping the list of wallets


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `data`                                                 | List[[wallets.Wallet](../../models/wallets/wallet.md)] | :heavy_check_mark:                                     | N/A                                                    |                                                        |
| `has_more`                                             | *Optional[bool]*                                       | :heavy_minus_sign:                                     | Whether further pages are available                    | false                                                  |
| `next`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Cursor for the next page, absent on the last page      |                                                        |
| `page_size`                                            | *int*                                                  | :heavy_check_mark:                                     | Number of items requested per page                     | 15                                                     |
| `previous`                                             | *Optional[str]*                                        | :heavy_minus_sign:                                     | Cursor for the previous page, absent on the first page | YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=           |