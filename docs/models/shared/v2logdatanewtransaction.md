# V2LogDataNewTransaction

Payload for NEW_TRANSACTION log entries. Contains the created transaction and any account metadata set during creation.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `account_metadata`                                                 | Dict[str, Dict[str, *str*]]                                        | :heavy_check_mark:                                                 | Metadata applied to accounts involved in the transaction           |
| `transaction`                                                      | [shared.V2LogTransaction](../../models/shared/v2logtransaction.md) | :heavy_check_mark:                                                 | Transaction structure as it appears in log payloads                |