# V3Schedule

A recurring job a connector runs to fetch data from its provider


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `connector_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | Identifier of the connector this schedule belongs to                 |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the schedule was created                                        |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique identifier of the schedule                                    |
| `paused_at`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the schedule was paused, absent while it is running             |
| `paused_reason`                                                      | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Why the schedule was paused                                          |