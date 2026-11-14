# V2VolumesWithBalance


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `account`                                               | *str*                                                   | :heavy_check_mark:                                      | The account address these volumes belong to             |
| `asset`                                                 | *str*                                                   | :heavy_check_mark:                                      | The asset these volumes are denominated in              |
| `balance`                                               | *int*                                                   | :heavy_check_mark:                                      | Net balance for this asset, equal to input minus output |
| `input`                                                 | *int*                                                   | :heavy_check_mark:                                      | Total amount credited to the account for this asset     |
| `output`                                                | *int*                                                   | :heavy_check_mark:                                      | Total amount debited from the account for this asset    |