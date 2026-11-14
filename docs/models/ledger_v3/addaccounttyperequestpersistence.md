# AddAccountTypeRequestPersistence

How account volumes are stored.
NORMAL: fully persisted (default).
EPHEMERAL: persisted, purged when zero balance after commit.
TRANSIENT: never persisted, must be zero at end of batch.


## Example Usage

```python
from formance_sdk_python.models.ledger_v3 import AddAccountTypeRequestPersistence

value = AddAccountTypeRequestPersistence.NORMAL
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `NORMAL`    | NORMAL      |
| `EPHEMERAL` | EPHEMERAL   |
| `TRANSIENT` | TRANSIENT   |