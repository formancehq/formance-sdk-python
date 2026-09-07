# V3CreateBankAccountRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_number`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Domestic account number. Supply this or an IBAN                     |
| `country`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Country the account is held in, as an ISO 3166-1 alpha-2 code       |
| `iban`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | International bank account number. Supply this or an account number |
| `metadata`                                                          | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | Arbitrary key/value pairs attached to the resource                  |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Human-readable name for the bank account                            |
| `swift_bic_code`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | SWIFT/BIC code identifying the bank                                 |