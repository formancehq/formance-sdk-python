# ConfigsResponseCursor

Paginated cursor wrapping the list of configurations


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `data`                                                                   | List[[webhooks.WebhooksConfig](../../models/webhooks/webhooksconfig.md)] | :heavy_check_mark:                                                       | N/A                                                                      |                                                                          |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Whether further pages are available                                      | false                                                                    |