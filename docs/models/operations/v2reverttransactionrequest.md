# V2RevertTransactionRequest


## Fields

| Field               | Type                | Required            | Description         | Example             |
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| `id`                | *int*               | :heavy_check_mark:  | Transaction ID.     | 1234                |
| `ledger`            | *str*               | :heavy_check_mark:  | Name of the ledger. | ledger001           |
| `force`             | *Optional[bool]*    | :heavy_minus_sign:  | Force revert        |                     |