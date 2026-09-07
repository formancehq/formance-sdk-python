# V3Task

An asynchronous unit of work, tracking an operation that completes in the background


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `connector_id`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Identifier of the connector the task runs against                      |
| `created_at`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_check_mark:                                                     | When the task was created                                              |
| `created_object_id`                                                    | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Identifier of the object the task created, once it has succeeded       |
| `error`                                                                | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | Why the task failed, absent when it succeeded                          |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique identifier of the task                                          |
| `status`                                                               | [payments.V3TaskStatusEnum](../../models/payments/v3taskstatusenum.md) | :heavy_check_mark:                                                     | Where a task stands, from processing through to succeeded or failed    |
| `updated_at`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_check_mark:                                                     | When the task was last updated                                         |