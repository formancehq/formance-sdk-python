# V3OpenBankingConnectionAttemptStatusEnum

Where a link attempt stands, from pending through to completed on success or exited when the user abandoned the flow or the provider reported an error

## Example Usage

```python
from formance_sdk_python.models.payments import V3OpenBankingConnectionAttemptStatusEnum

value = V3OpenBankingConnectionAttemptStatusEnum.PENDING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `COMPLETED` | completed   |
| `EXITED`    | exited      |