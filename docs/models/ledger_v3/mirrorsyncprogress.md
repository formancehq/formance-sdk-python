# MirrorSyncProgress

Sync progress for MIRROR ledgers (populated at read time)


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `cursor`                                                                         | *int*                                                                            | :heavy_check_mark:                                                               | Last ingested v2 log ID                                                          |
| `error`                                                                          | [Optional[ledger_v3.MirrorSyncError]](../../models/ledger_v3/mirrorsyncerror.md) | :heavy_minus_sign:                                                               | Most recent mirror sync error (null if healthy)                                  |
| `remaining_logs`                                                                 | *int*                                                                            | :heavy_check_mark:                                                               | Number of remaining logs to sync (sourceLogCount - cursor)                       |
| `source_log_count`                                                               | *int*                                                                            | :heavy_check_mark:                                                               | Latest known log ID in the v2 source                                             |
| `state`                                                                          | [ledger_v3.State](../../models/ledger_v3/state.md)                               | :heavy_check_mark:                                                               | Current sync state (SYNCING = catching up, FOLLOWING = up to date)               |