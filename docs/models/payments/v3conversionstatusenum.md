# V3ConversionStatusEnum

Lifecycle of a conversion.
`PENDING` — accepted by the PSP, not yet settled.
`COMPLETED` — settled, terminal.
`FAILED` — rejected or reverted, terminal. See `error`.


## Example Usage

```python
from formance_sdk_python.models.payments import V3ConversionStatusEnum

value = V3ConversionStatusEnum.UNKNOWN
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `UNKNOWN`   | UNKNOWN     |
| `PENDING`   | PENDING     |
| `COMPLETED` | COMPLETED   |
| `FAILED`    | FAILED      |