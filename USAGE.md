<!-- Start SDK Example Usage [usage] -->
```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.get_oidc_well_knowns()

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->