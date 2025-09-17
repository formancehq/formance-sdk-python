<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from formance_sdk_python import SDK
from formance_sdk_python.models import shared


with SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

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
from formance_sdk_python.models import shared

async def main():

    async with SDK(
        security=shared.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:

        res = await sdk.get_versions_async()

        assert res.get_versions_response is not None

        # Handle response
        print(res.get_versions_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->