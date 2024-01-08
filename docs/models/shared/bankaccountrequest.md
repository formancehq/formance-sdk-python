# BankAccountRequest


## Fields

| Field              | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `account_number`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |
| `connector_id`     | *str*              | :heavy_check_mark: | N/A                |                    |
| `country`          | *str*              | :heavy_check_mark: | N/A                | GB                 |
| `iban`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |
| `metadata`         | Dict[str, *str*]   | :heavy_minus_sign: | N/A                |                    |
| `name`             | *str*              | :heavy_check_mark: | N/A                | My account         |
| `swift_bic_code`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |