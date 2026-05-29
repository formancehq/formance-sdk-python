# V3TimeInForceEnum

How long an order is valid on the exchange.
`GOOD_UNTIL_CANCELLED` — rests until explicitly cancelled.
`GOOD_UNTIL_DATE_TIME` — rests until `expiresAt`.
`IMMEDIATE_OR_CANCEL` — fill immediately, cancel any unfilled portion.
`FILL_OR_KILL` — fill fully and immediately, or cancel entirely.


## Example Usage

```python
from formance_sdk_python.models.payments import V3TimeInForceEnum

value = V3TimeInForceEnum.UNKNOWN
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `UNKNOWN`              | UNKNOWN                |
| `GOOD_UNTIL_CANCELLED` | GOOD_UNTIL_CANCELLED   |
| `GOOD_UNTIL_DATE_TIME` | GOOD_UNTIL_DATE_TIME   |
| `IMMEDIATE_OR_CANCEL`  | IMMEDIATE_OR_CANCEL    |
| `FILL_OR_KILL`         | FILL_OR_KILL           |