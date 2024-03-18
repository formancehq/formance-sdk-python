# BankAccountRequest


## Fields

| Field              | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `connector_id`     | *str*              | :heavy_check_mark: | N/A                |                    |
| `country`          | *str*              | :heavy_check_mark: | N/A                | GB                 |
| `name`             | *str*              | :heavy_check_mark: | N/A                | My account         |
| `account_number`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |
| `iban`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |
| `metadata`         | Dict[str, *str*]   | :heavy_minus_sign: | N/A                |                    |
| `swift_bic_code`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |