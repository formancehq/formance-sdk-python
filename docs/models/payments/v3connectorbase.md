# V3ConnectorBase

Summary of a connector, without its configuration


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the connector was installed                                     |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Unique identifier of the connector                                   |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Human-readable name of the connector instance                        |
| `provider`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Name of the payment provider behind the connector                    |
| `reference`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Stable reference identifying the connector                           |