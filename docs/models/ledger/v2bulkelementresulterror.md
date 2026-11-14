# V2BulkElementResultError


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `error_code`                                         | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `error_description`                                  | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `error_details`                                      | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `log_id`                                             | *int*                                                | :heavy_check_mark:                                   | Identifier of the log entry produced by this element |
| `response_type`                                      | *str*                                                | :heavy_check_mark:                                   | The action this result corresponds to                |