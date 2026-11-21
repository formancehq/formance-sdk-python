# PostingAmount

Unsigned amount from 0 through 2^256-1. Requests accept JSON integer
tokens or canonical decimal strings independently of the response
header; the server enforces the bound for both forms. Responses use
numbers by default and strings with Formance-Bigint-As-String enabled,
as do all response Uint256 values regardless of business meaning.



## Supported Types

### `int`

```python
value: int = /* values here */
```

### `str`

```python
value: str = /* values here */
```

