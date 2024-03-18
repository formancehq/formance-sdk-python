# Account


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `address`                                                | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | users:001                                                |
| `metadata`                                               | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | N/A                                                      | {<br/>"admin": true,<br/>"a": {<br/>"nested": {<br/>"key": "value"<br/>}<br/>}<br/>} |
| `type`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      | virtual                                                  |