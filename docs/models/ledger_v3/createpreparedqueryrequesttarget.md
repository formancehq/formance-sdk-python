# CreatePreparedQueryRequestTarget

Target entity type. `LOGS` queries return log entries; the log-only filter fields (`logId`, `date`, `ledger`) are valid only when the target is `LOGS`.

## Example Usage

```python
from formance_sdk_python.models.ledger_v3 import CreatePreparedQueryRequestTarget

value = CreatePreparedQueryRequestTarget.ACCOUNTS
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ACCOUNTS`     | ACCOUNTS       |
| `TRANSACTIONS` | TRANSACTIONS   |
| `LOGS`         | LOGS           |