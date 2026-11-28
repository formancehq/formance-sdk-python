# V2ResumeActivityResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `content_type`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | HTTP response content type for this operation                            |
| `status_code`                                                            | *int*                                                                    | :heavy_check_mark:                                                       | HTTP response status code for this operation                             |
| `raw_response`                                                           | [httpx.Response](https://www.python-httpx.org/api/#response)             | :heavy_check_mark:                                                       | Raw HTTP response; suitable for custom response parsing                  |
| `v2_error`                                                               | [Optional[orchestration.V2Error]](../../models/orchestration/v2error.md) | :heavy_minus_sign:                                                       | General error                                                            |