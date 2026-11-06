# Workflow

A workflow definition and the stages it runs


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `config`                                                                     | [orchestration.WorkflowConfig](../../models/orchestration/workflowconfig.md) | :heavy_check_mark:                                                           | The stages a workflow runs, in order                                         |
| `created_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | When the workflow was created                                                |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique identifier of the workflow                                            |
| `updated_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | When the workflow was last modified                                          |