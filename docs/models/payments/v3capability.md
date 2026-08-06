# V3Capability

Plugin capability advertised by a connector. Distinct from the Formance gateway "module capabilities" (which are version-gated); these reflect what the underlying PSP integration actually exposes.


## Example Usage

```python
from formance_sdk_python.models.payments import V3Capability

value = V3Capability.FETCH_ACCOUNTS
```


## Values

| Name                              | Value                             |
| --------------------------------- | --------------------------------- |
| `FETCH_ACCOUNTS`                  | FETCH_ACCOUNTS                    |
| `FETCH_BALANCES`                  | FETCH_BALANCES                    |
| `FETCH_EXTERNAL_ACCOUNTS`         | FETCH_EXTERNAL_ACCOUNTS           |
| `FETCH_PAYMENTS`                  | FETCH_PAYMENTS                    |
| `FETCH_OTHERS`                    | FETCH_OTHERS                      |
| `FETCH_ORDERS`                    | FETCH_ORDERS                      |
| `FETCH_CONVERSIONS`               | FETCH_CONVERSIONS                 |
| `CREATE_WEBHOOKS`                 | CREATE_WEBHOOKS                   |
| `TRANSLATE_WEBHOOKS`              | TRANSLATE_WEBHOOKS                |
| `CREATE_BANK_ACCOUNT`             | CREATE_BANK_ACCOUNT               |
| `CREATE_TRANSFER`                 | CREATE_TRANSFER                   |
| `CREATE_PAYOUT`                   | CREATE_PAYOUT                     |
| `ALLOW_FORMANCE_ACCOUNT_CREATION` | ALLOW_FORMANCE_ACCOUNT_CREATION   |
| `ALLOW_FORMANCE_PAYMENT_CREATION` | ALLOW_FORMANCE_PAYMENT_CREATION   |