# WorkflowInstanceHistory


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `error`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Why the stage failed, absent when it succeeded                       |
| `input`                                                              | [orchestration.Stage](../../models/orchestration/stage.md)           | :heavy_check_mark:                                                   | One step of a workflow, whose shape depends on the stage type        |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name of the stage this history entry records                         |
| `started_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the stage started                                               |
| `terminated`                                                         | *bool*                                                               | :heavy_check_mark:                                                   | Whether the stage has finished                                       |
| `terminated_at`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When the stage finished, absent while it is still running            |