# ResumeActivityRequestBody


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `paused_at`                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                           | :heavy_check_mark:                                                                             | Nonzero RFC3339 timestamp from the paused activity projection identifying the pause generation |
| `temporal_run_id`                                                                              | *str*                                                                                          | :heavy_check_mark:                                                                             | Expected Temporal run id from the paused activity projection                                   |