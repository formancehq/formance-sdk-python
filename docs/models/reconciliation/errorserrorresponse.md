# ErrorsErrorResponse

Error response


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `details`                                                 | *Optional[str]*                                           | :heavy_minus_sign:                                        | Optional link carrying additional context about the error |                                                           |
| `error_code`                                              | *str*                                                     | :heavy_check_mark:                                        | Machine-readable error code identifying the failure       | VALIDATION                                                |
| `error_message`                                           | *str*                                                     | :heavy_check_mark:                                        | Human-readable description of the error                   |                                                           |