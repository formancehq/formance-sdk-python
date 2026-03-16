# V2LogData

The payload of the log entry. Structure depends on the log type:
- NEW_TRANSACTION: V2LogDataNewTransaction
- SET_METADATA: V2LogDataSetMetadata
- REVERTED_TRANSACTION: V2LogDataRevertedTransaction
- DELETE_METADATA: V2LogDataDeleteMetadata
- INSERTED_SCHEMA: V2LogDataInsertedSchema



## Supported Types

### `shared.V2LogDataNewTransaction`

```python
value: shared.V2LogDataNewTransaction = /* values here */
```

### `shared.V2LogDataSetMetadata`

```python
value: shared.V2LogDataSetMetadata = /* values here */
```

### `shared.V2LogDataRevertedTransaction`

```python
value: shared.V2LogDataRevertedTransaction = /* values here */
```

### `shared.V2LogDataDeleteMetadata`

```python
value: shared.V2LogDataDeleteMetadata = /* values here */
```

### `shared.V2LogDataInsertedSchema`

```python
value: shared.V2LogDataInsertedSchema = /* values here */
```

