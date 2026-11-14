# AccountVolume


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `asset`                                                                      | *str*                                                                        | :heavy_check_mark:                                                           | Asset identifier (e.g. "USD/2")                                              |
| `color`                                                                      | *str*                                                                        | :heavy_check_mark:                                                           | Color of the bucket. Empty string is the uncolored bucket.                   |
| `volumes`                                                                    | [ledger_v3.VolumesWithBalance](../../models/ledger_v3/volumeswithbalance.md) | :heavy_check_mark:                                                           | N/A                                                                          |