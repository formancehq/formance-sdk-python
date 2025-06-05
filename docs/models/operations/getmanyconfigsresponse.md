# GetManyConfigsResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `configs_response`                                                         | [Optional[shared.ConfigsResponse]](../../models/shared/configsresponse.md) | :heavy_minus_sign:                                                         | OK                                                                         |
| `content_type`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | HTTP response content type for this operation                              |
| `status_code`                                                              | *int*                                                                      | :heavy_check_mark:                                                         | HTTP response status code for this operation                               |
| `raw_response`                                                             | [httpx.Response](https://www.python-httpx.org/api/#response)               | :heavy_check_mark:                                                         | Raw HTTP response; suitable for custom response parsing                    |