# SignedMonetaryAmount

Arbitrary-precision SignedBigInt value encoded as a JSON number by
default, or a canonical decimal string when Formance-Bigint-As-String
is enabled. The same rule applies to every response SignedBigInt value,
including nested fields, regardless of business meaning.



## Supported Types

### `int`

```python
value: int = /* values here */
```

### `str`

```python
value: str = /* values here */
```

