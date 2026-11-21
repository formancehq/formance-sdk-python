# PreparedQueryTarget

Target entity type. `LOGS`, `ACCOUNTS` and `TRANSACTIONS` are all usable prepared-query targets (create, list/get and execute).

## Example Usage

```python
from formance_sdk_python.models.ledger_v3 import PreparedQueryTarget

value = PreparedQueryTarget.ACCOUNTS
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ACCOUNTS`     | ACCOUNTS       |
| `TRANSACTIONS` | TRANSACTIONS   |
| `LOGS`         | LOGS           |