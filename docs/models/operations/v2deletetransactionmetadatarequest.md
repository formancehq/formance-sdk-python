# V2DeleteTransactionMetadataRequest


## Fields

| Field                  | Type                   | Required               | Description            | Example                |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `idempotency_key`      | *Optional[str]*        | :heavy_minus_sign:     | Use an idempotency key |                        |
| `id`                   | *int*                  | :heavy_check_mark:     | Transaction ID.        | 1234                   |
| `key`                  | *str*                  | :heavy_check_mark:     | The key to remove.     | foo                    |
| `ledger`               | *str*                  | :heavy_check_mark:     | Name of the ledger.    | ledger001              |