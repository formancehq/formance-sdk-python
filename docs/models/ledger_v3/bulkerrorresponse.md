# BulkErrorResponse

Bulk processing returns per-element outcomes in data, including any
preceding successes and subsequent aborted elements. Failures before
processing and panic recovery can return only errorCode/errorMessage.
These object shapes overlap: use a non-exclusive union and preserve
the bulk fields when decoding a processing failure.



## Supported Types

### `ledger_v3.BulkResponse`

```python
value: ledger_v3.BulkResponse = /* values here */
```

### `ledger_v3.ErrorResponse`

```python
value: ledger_v3.ErrorResponse = /* values here */
```

