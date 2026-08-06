# ReplayDeliveriesRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `config_ids`                                                         | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_at_from`                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at_to`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `cursor`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `page_size`                                                          | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `statuses`                                                           | List[[webhooks.Status](../../models/webhooks/status.md)]             | :heavy_minus_sign:                                                   | N/A                                                                  |