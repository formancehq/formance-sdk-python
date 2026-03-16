<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from formance_sdk_python import SDK

async def main():

    async with SDK() as sdk:

        res = await sdk.get_versions_async()

        assert res.get_versions_response is not None

        # Handle response
        print(res.get_versions_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->