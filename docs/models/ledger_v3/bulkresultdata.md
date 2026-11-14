# BulkResultData

Operation result data. Shape depends on the originating action:
  - `CREATE_TRANSACTION` success: a `TransactionResponse` — the
    created Transaction object.
  - Any skippable action skip (when the item opted into
    `skippableReasons` and the FSM matched one): an
    `OrderSkippedResponse` with `skipped: true`, `reason`, and
    reason-specific `context`. Emitted for every REST-supported
    skippable action — CREATE_TRANSACTION, REVERT_TRANSACTION,
    DELETE_METADATA — not just create.
  - Other successful non-create actions: `null`.
Branch on `OrderSkippedResponse.skipped` to distinguish a skip
from a successful transaction.



## Supported Types

### `ledger_v3.LedgerV3TransactionResponseTransactionResponse`

```python
value: ledger_v3.LedgerV3TransactionResponseTransactionResponse = /* values here */
```

### `ledger_v3.OrderSkippedResponse`

```python
value: ledger_v3.OrderSkippedResponse = /* values here */
```

