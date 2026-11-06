# Action

The type of operation to perform. The REST bulk endpoint accepts
these four actions only; account-type actions
(`ADD_ACCOUNT_TYPE` / `REMOVE_ACCOUNT_TYPE`) are gRPC-only and
are rejected here.


## Example Usage

```python
from formance_sdk_python.models.ledger_v3 import Action

value = Action.CREATE_TRANSACTION
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `CREATE_TRANSACTION` | CREATE_TRANSACTION   |
| `ADD_METADATA`       | ADD_METADATA         |
| `REVERT_TRANSACTION` | REVERT_TRANSACTION   |
| `DELETE_METADATA`    | DELETE_METADATA      |