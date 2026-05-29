# V3OrderTypeEnum

Exchange order type. Determines which price fields are meaningful on
`V3Order`: LIMIT-family types use `limitPrice`; STOP-family types use
`stopPrice`; TWAP/VWAP are time-weighted execution algorithms.


## Example Usage

```python
from formance_sdk_python.models.payments import V3OrderTypeEnum

value = V3OrderTypeEnum.UNKNOWN
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `UNKNOWN`             | UNKNOWN               |
| `MARKET`              | MARKET                |
| `LIMIT`               | LIMIT                 |
| `STOP_LIMIT`          | STOP_LIMIT            |
| `STOP`                | STOP                  |
| `TWAP`                | TWAP                  |
| `VWAP`                | VWAP                  |
| `PEG`                 | PEG                   |
| `BLOCK`               | BLOCK                 |
| `RFQ`                 | RFQ                   |
| `TRAILING_STOP`       | TRAILING_STOP         |
| `TRAILING_STOP_LIMIT` | TRAILING_STOP_LIMIT   |
| `TAKE_PROFIT`         | TAKE_PROFIT           |
| `TAKE_PROFIT_LIMIT`   | TAKE_PROFIT_LIMIT     |
| `LIMIT_MAKER`         | LIMIT_MAKER           |