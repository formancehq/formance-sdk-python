# Cadence

Reconciliation rhythm. Scopes each failing fingerprint into a period so a
March break and an April break are distinct, independently-closable cases.
`continuous` (default) is a single unbounded period (live monitoring).


## Example Usage

```python
from formance_sdk_python.models.reconciliation import Cadence

value = Cadence.CONTINUOUS
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CONTINUOUS` | continuous   |
| `DAILY`      | daily        |
| `WEEKLY`     | weekly       |
| `MONTHLY`    | monthly      |