# State

Last recorded ingestion state; it can be stale. paused can represent requested suspension before ingestion exists. finished is successful bounded completion.

## Example Usage

```python
from formance_sdk_python.models.connectivity import State

value = State.RUNNING
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `RUNNING`  | running    |
| `ERROR`    | error      |
| `FAILED`   | failed     |
| `STOPPED`  | stopped    |
| `PAUSED`   | paused     |
| `FINISHED` | finished   |
| `UNKNOWN`  | unknown    |