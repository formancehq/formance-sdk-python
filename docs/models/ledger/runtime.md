# Runtime

The numscript runtime used to execute the script. Uses "machine" by default, unless the "--experimental-numscript-interpreter" feature flag is passed.

## Example Usage

```python
from formance_sdk_python.models.ledger import Runtime

value = Runtime.EXPERIMENTAL_INTERPRETER
```


## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `EXPERIMENTAL_INTERPRETER` | experimental-interpreter   |
| `MACHINE`                  | machine                    |