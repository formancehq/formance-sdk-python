# V2TriggerTest

Result of evaluating a trigger against a sample event, without running the workflow


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `filter_`                                                                     | [Optional[orchestration.Filter]](../../models/orchestration/filter_.md)       | :heavy_minus_sign:                                                            | How the trigger's filter evaluated against the sample event                   |
| `variables`                                                                   | Dict[str, [orchestration.Variables](../../models/orchestration/variables.md)] | :heavy_minus_sign:                                                            | The variables the trigger would build from the sample event                   |