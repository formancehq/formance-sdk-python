# Ack

Record of who acknowledged an alert and when


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the alert was acknowledged                                      |                                                                      |
| `by`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Who acknowledged the alert                                           | ops@buildr.com                                                       |
| `note`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Free-text note left by whoever acknowledged the alert                |                                                                      |