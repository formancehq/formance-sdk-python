# AnyVariantAction


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `drop`                                                                                     | [Optional[ledger_v3.DropAction]](../../models/ledger_v3/dropaction.md)                     | :heavy_minus_sign:                                                                         | Turns the entry into a fill-gap that preserves log-ID and tx-ID continuity.                |
| `rewrite_address`                                                                          | [Optional[ledger_v3.RewriteAddressAction]](../../models/ledger_v3/rewriteaddressaction.md) | :heavy_minus_sign:                                                                         | N/A                                                                                        |