# Snooze

A time-boxed, operator-initiated mute of an alert's notifications. While
`until` is in the future the alert keeps failing and keeps counting
against period-green — only its notifications are suppressed.



## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)  | :heavy_check_mark:                                                    | When the alert was snoozed                                            |                                                                       |
| `by`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | Who snoozed the alert                                                 | ops@buildr.com                                                        |
| `note`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Free-text note left by whoever snoozed the alert                      |                                                                       |
| `until`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)  | :heavy_check_mark:                                                    | When the mute expires and notifications resume. Must be in the future |                                                                       |