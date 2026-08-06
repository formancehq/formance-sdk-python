# SnoozeAlertRequest

Mute an alert's notifications until `until` (which must be in the future).


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `by`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  | ops@buildr.com                                                       |
| `note`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `until`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |