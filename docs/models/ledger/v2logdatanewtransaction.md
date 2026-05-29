# V2LogDataNewTransaction

Payload for NEW_TRANSACTION log entries. Contains the created transaction and any account metadata set during creation.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `v2_log_transaction`                                               | [ledger.V2LogTransaction](../../models/ledger/v2logtransaction.md) | :heavy_check_mark:                                                 | Transaction structure as it appears in log payloads                |
| `account_metadata`                                                 | Dict[str, Dict[str, *str*]]                                        | :heavy_check_mark:                                                 | Metadata applied to accounts involved in the transaction           |