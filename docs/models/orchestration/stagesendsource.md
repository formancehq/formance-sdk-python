# StageSendSource

Where a send stage takes the funds from


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `account`                                                                                              | [Optional[orchestration.StageSendSourceAccount]](../../models/orchestration/stagesendsourceaccount.md) | :heavy_minus_sign:                                                                                     | Take the funds from a ledger account                                                                   |
| `payment`                                                                                              | [Optional[orchestration.StageSendSourcePayment]](../../models/orchestration/stagesendsourcepayment.md) | :heavy_minus_sign:                                                                                     | Take the funds from a payment                                                                          |
| `wallet`                                                                                               | [Optional[orchestration.StageSendSourceWallet]](../../models/orchestration/stagesendsourcewallet.md)   | :heavy_minus_sign:                                                                                     | Take the funds from a wallet                                                                           |