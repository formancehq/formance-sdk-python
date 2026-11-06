# AggregateVolumesData


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `groups`                                                                                   | List[[ledger_v3.GroupedAggregateResult](../../models/ledger_v3/groupedaggregateresult.md)] | :heavy_minus_sign:                                                                         | Per-prefix aggregated volumes (present when groupByPrefixes is set)                        |
| `volumes`                                                                                  | List[[ledger_v3.AggregatedVolume](../../models/ledger_v3/aggregatedvolume.md)]             | :heavy_check_mark:                                                                         | Flat aggregated volumes per asset                                                          |