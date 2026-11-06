# Error

Request or server error. The HTTP status and code identify the failure.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `code`                                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | Machine-readable error code (e.g. `not_found`, `unauthorized`, `connector_missing`) |
| `details`                                                                           | Dict[str, *Any*]                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `message`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |