# GetVersionsResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `env`                                                    | *str*                                                    | :heavy_check_mark:                                       | Environment the stack is deployed in                     |
| `region`                                                 | *str*                                                    | :heavy_check_mark:                                       | Region the stack is deployed in                          |
| `versions`                                               | List[[gateway.Version](../../models/gateway/version.md)] | :heavy_check_mark:                                       | Version and health of each component in the stack        |