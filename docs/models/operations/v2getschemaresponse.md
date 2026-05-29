# V2GetSchemaResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `content_type`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | HTTP response content type for this operation                                |
| `status_code`                                                                | *int*                                                                        | :heavy_check_mark:                                                           | HTTP response status code for this operation                                 |
| `raw_response`                                                               | [httpx.Response](https://www.python-httpx.org/api/#response)                 | :heavy_check_mark:                                                           | Raw HTTP response; suitable for custom response parsing                      |
| `v2_schema_response`                                                         | [Optional[ledger.V2SchemaResponse]](../../models/ledger/v2schemaresponse.md) | :heavy_minus_sign:                                                           | Schema retrieved successfully                                                |