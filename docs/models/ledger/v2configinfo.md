# V2ConfigInfo


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `experimental_features`                               | List[*str*]                                           | :heavy_minus_sign:                                    | Experimental feature flags enabled on this deployment |
| `server`                                              | *str*                                                 | :heavy_check_mark:                                    | Name of the server serving the API                    |
| `version`                                             | *str*                                                 | :heavy_check_mark:                                    | Version of the ledger service                         |