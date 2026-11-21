# Error

Request or server error. The HTTP status and code identify the failure.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `details`                                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Additional details; when structured, this string contains a JSON object.            |
| `error_code`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Machine-readable error code (e.g. `not_found`, `unauthorized`, `connector_missing`) |
| `error_message`                                                                     | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |