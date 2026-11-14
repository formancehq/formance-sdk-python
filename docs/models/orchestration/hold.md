# Hold

Funds locked by a pending wallet debit, later either confirmed or voided


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `description`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | Human-readable reason the funds were held                                        |
| `destination`                                                                    | [Optional[orchestration.Subject]](../../models/orchestration/subject.md)         | :heavy_minus_sign:                                                               | The counterparty of a wallet movement, either a ledger account or another wallet |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The unique ID of the hold.                                                       |
| `metadata`                                                                       | Dict[str, *str*]                                                                 | :heavy_check_mark:                                                               | Metadata associated with the hold.                                               |
| `wallet_id`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the wallet the hold is associated with.                                |