# SegmentTypeType

regex: custom regular expression (requires `regex`).
uuid: RFC 4122 UUID format.
uint64: decimal uint64.
bytes: hex-encoded bytes (even length).


## Example Usage

```python
from formance_sdk_python.models.ledger_v3 import SegmentTypeType

value = SegmentTypeType.REGEX
```


## Values

| Name     | Value    |
| -------- | -------- |
| `REGEX`  | regex    |
| `UUID`   | uuid     |
| `UINT64` | uint64   |
| `BYTES`  | bytes    |