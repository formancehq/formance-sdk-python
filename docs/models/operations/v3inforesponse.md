# V3InfoResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `content_type`                                                         | *str*                                                                  | :heavy_check_mark:                                                     | HTTP response content type for this operation                          |
| `server_info`                                                          | [Optional[ledger_v3.ServerInfo]](../../models/ledger_v3/serverinfo.md) | :heavy_minus_sign:                                                     | Server build information                                               |
| `status_code`                                                          | *int*                                                                  | :heavy_check_mark:                                                     | HTTP response status code for this operation                           |
| `raw_response`                                                         | [httpx.Response](https://www.python-httpx.org/api/#response)           | :heavy_check_mark:                                                     | Raw HTTP response; suitable for custom response parsing                |