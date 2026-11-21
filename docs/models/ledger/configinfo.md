# ConfigInfo

Configuration and version information for the ledger server


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `config`                                              | [ledger.Config](../../models/ledger/config.md)        | :heavy_check_mark:                                    | Configuration the ledger server is running with       |
| `experimental_features`                               | List[*str*]                                           | :heavy_minus_sign:                                    | Experimental feature flags enabled on this deployment |
| `server`                                              | *str*                                                 | :heavy_check_mark:                                    | Name of the server serving the API                    |
| `version`                                             | *str*                                                 | :heavy_check_mark:                                    | Version of the ledger service                         |