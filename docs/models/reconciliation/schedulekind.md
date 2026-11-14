# ScheduleKind

Whether the rule runs only when triggered or on a recurring cron schedule

## Example Usage

```python
from formance_sdk_python.models.reconciliation import ScheduleKind

value = ScheduleKind.ON_DEMAND
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `ON_DEMAND` | on_demand   |
| `CRON`      | cron        |