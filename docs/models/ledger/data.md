# Data

The payload of the log entry. Structure depends on the log type:
- NEW_TRANSACTION: V2LogDataNewTransaction
- SET_METADATA: V2LogDataSetMetadata
- REVERTED_TRANSACTION: V2LogDataRevertedTransaction
- DELETE_METADATA: V2LogDataDeleteMetadata
- INSERTED_SCHEMA: V2LogDataInsertedSchema



## Supported Types

### `ledger.V2LogDataNewTransaction`

```python
value: ledger.V2LogDataNewTransaction = /* values here */
```

### `ledger.V2LogDataSetMetadata`

```python
value: ledger.V2LogDataSetMetadata = /* values here */
```

### `ledger.V2LogDataRevertedTransaction`

```python
value: ledger.V2LogDataRevertedTransaction = /* values here */
```

### `ledger.V2LogDataDeleteMetadata`

```python
value: ledger.V2LogDataDeleteMetadata = /* values here */
```

### `ledger.V2LogDataInsertedSchema`

```python
value: ledger.V2LogDataInsertedSchema = /* values here */
```

