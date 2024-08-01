<!-- Start SDK Example Usage [usage] -->
```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
)


res = s.get_oidc_well_knowns()

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->