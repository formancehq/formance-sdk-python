# ListInstancesResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `content_type`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | HTTP response content type for this operation                                |
| `list_runs_response`                                                         | [Optional[shared.ListRunsResponse]](../../models/shared/listrunsresponse.md) | :heavy_minus_sign:                                                           | List of workflow instances                                                   |
| `status_code`                                                                | *int*                                                                        | :heavy_check_mark:                                                           | HTTP response status code for this operation                                 |
| `raw_response`                                                               | [httpx.Response](https://www.python-httpx.org/api/#response)                 | :heavy_check_mark:                                                           | Raw HTTP response; suitable for custom response parsing                      |