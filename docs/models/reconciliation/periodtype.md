# PeriodType

How long a reconciliation period lasts. Scopes each failing fingerprint
into a period so a March break and an April break are distinct,
independently-closable cases.

Omit the key to get `continuous`, a single unbounded period (live
monitoring). There is deliberately no schema-level `default`: SDK
generators materialize defaults into the serialized body, which would
make an omitted key indistinguishable from an explicit one and collide
with the deprecated `cadence` alias. The server owns the default.

This is not how often the rule runs — that is `schedule`, and the two are
independent: an hourly schedule with a `monthly` period type is normal.
The period type determines the `periodID` an alert is filed under:
`monthly` yields `2026-07`.


## Example Usage

```python
from formance_sdk_python.models.reconciliation import PeriodType

value = PeriodType.CONTINUOUS
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CONTINUOUS` | continuous   |
| `DAILY`      | daily        |
| `WEEKLY`     | weekly       |
| `MONTHLY`    | monthly      |