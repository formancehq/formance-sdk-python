# V2Hold


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `description`                                                  | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `destination`                                                  | [Optional[shared.V2Subject]](../../models/shared/v2subject.md) | :heavy_minus_sign:                                             | N/A                                                            |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | The unique ID of the hold.                                     |
| `metadata`                                                     | Dict[str, *str*]                                               | :heavy_check_mark:                                             | Metadata associated with the hold.                             |
| `wallet_id`                                                    | *str*                                                          | :heavy_check_mark:                                             | The ID of the wallet the hold is associated with.              |