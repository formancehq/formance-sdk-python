# V2DeleteAccountMetadataRequest


## Fields

| Field                  | Type                   | Required               | Description            | Example                |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `idempotency_key`      | *Optional[str]*        | :heavy_minus_sign:     | Use an idempotency key |                        |
| `address`              | *str*                  | :heavy_check_mark:     | Account address        |                        |
| `key`                  | *str*                  | :heavy_check_mark:     | The key to remove.     | foo                    |
| `ledger`               | *str*                  | :heavy_check_mark:     | Name of the ledger.    | ledger001              |