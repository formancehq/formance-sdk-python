# OrchestrationHold


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `description`                                              | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `destination`                                              | [Optional[shared.Subject]](../../models/shared/subject.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | The unique ID of the hold.                                 |
| `metadata`                                                 | Dict[str, *str*]                                           | :heavy_check_mark:                                         | Metadata associated with the hold.                         |
| `wallet_id`                                                | *str*                                                      | :heavy_check_mark:                                         | The ID of the wallet the hold is associated with.          |