# CreateLedgerRequestMode

Ledger mode. MIRROR creates a read-only ledger that syncs from an external v2 source. Values are case-sensitive; any other value is rejected with 400 INVALID_REQUEST.

## Example Usage

```python
from formance_sdk_python.models.ledger_v3 import CreateLedgerRequestMode

value = CreateLedgerRequestMode.NORMAL
```


## Values

| Name     | Value    |
| -------- | -------- |
| `NORMAL` | NORMAL   |
| `MIRROR` | MIRROR   |