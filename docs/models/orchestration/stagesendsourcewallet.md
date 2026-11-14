# StageSendSourceWallet

Take the funds from a wallet


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `balance`                                                                        | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Name of the balance within the wallet. Defaults to the main balance when omitted |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | Identifier of the wallet to take funds from                                      |