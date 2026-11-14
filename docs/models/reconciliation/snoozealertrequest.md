# SnoozeAlertRequest

Mute an alert's notifications until `until` (which must be in the future).


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `by`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | Who is snoozing the alert                                             | ops@buildr.com                                                        |
| `note`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Free-text note to record with the snooze                              |                                                                       |
| `until`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)  | :heavy_check_mark:                                                    | When the mute expires and notifications resume. Must be in the future |                                                                       |