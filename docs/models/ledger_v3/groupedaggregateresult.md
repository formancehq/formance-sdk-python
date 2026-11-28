# GroupedAggregateResult


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `prefix`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | Account prefix this group matches                                              |
| `volumes`                                                                      | List[[ledger_v3.AggregatedVolume](../../models/ledger_v3/aggregatedvolume.md)] | :heavy_check_mark:                                                             | Aggregated volumes for accounts matching this prefix                           |