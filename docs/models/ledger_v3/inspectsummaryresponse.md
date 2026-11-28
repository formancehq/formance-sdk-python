# InspectSummaryResponse


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `cardinality`                                                 | *int*                                                         | :heavy_check_mark:                                            | Number of distinct values                                     |
| `entities_with_key`                                           | *int*                                                         | :heavy_check_mark:                                            | Number of entities that have this metadata key set (non-null) |
| `entities_with_null`                                          | *int*                                                         | :heavy_check_mark:                                            | Number of entities with a null value for this key             |
| `max`                                                         | *Optional[Any]*                                               | :heavy_minus_sign:                                            | Maximum value (null if index is empty)                        |
| `min`                                                         | *Optional[Any]*                                               | :heavy_minus_sign:                                            | Minimum value (null if index is empty)                        |