# V3AddressRequest

A postal address to record on the payment service user


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `city`                                                | *Optional[str]*                                       | :heavy_minus_sign:                                    | City of the address                                   |
| `country`                                             | *Optional[str]*                                       | :heavy_minus_sign:                                    | Country of the address, as an ISO 3166-1 alpha-2 code |
| `postal_code`                                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | Postal or ZIP code of the address                     |
| `region`                                              | *Optional[str]*                                       | :heavy_minus_sign:                                    | Region, state or province of the address              |
| `street_name`                                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | Street name of the address                            |
| `street_number`                                       | *Optional[str]*                                       | :heavy_minus_sign:                                    | Street number of the address                          |