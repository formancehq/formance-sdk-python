# V2LogDataRevertedTransaction

Payload for REVERTED_TRANSACTION log entries. Contains both the original reverted transaction and the new reverting transaction.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `v2_log_transaction`                                               | [ledger.V2LogTransaction](../../models/ledger/v2logtransaction.md) | :heavy_check_mark:                                                 | Transaction structure as it appears in log payloads                |
| `v2_log_transaction1`                                              | [ledger.V2LogTransaction](../../models/ledger/v2logtransaction.md) | :heavy_check_mark:                                                 | Transaction structure as it appears in log payloads                |