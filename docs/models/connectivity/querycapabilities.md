# QueryCapabilities

The filterable keys per resource, serialized from the same allowlist
the server enforces -- it cannot drift from what queries accept.



## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `resources`                                                                                                  | Dict[str, Dict[str, [connectivity.QueryFieldCapability](../../models/connectivity/queryfieldcapability.md)]] | :heavy_check_mark:                                                                                           | N/A                                                                                                          |