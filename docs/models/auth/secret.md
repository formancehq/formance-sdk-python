# Secret

A client secret. The full value is returned only at creation and cannot be retrieved again


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `clear`                                            | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `id`                                               | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `last_digits`                                      | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `metadata`                                         | Dict[str, *str*]                                   | :heavy_minus_sign:                                 | Arbitrary key/value pairs attached to the resource |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Human-readable name identifying the secret         |