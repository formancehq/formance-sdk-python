# V3RemoveEventsSinkRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `idempotency_key`                                             | *Optional[str]*                                               | :heavy_minus_sign:                                            | Idempotency key for the request                               |
| `controller_id`                                               | *Optional[str]*                                               | :heavy_minus_sign:                                            | Optional opaque owner identity used as a removal precondition |
| `sink_name`                                                   | *str*                                                         | :heavy_check_mark:                                            | Name of the event sink to remove                              |