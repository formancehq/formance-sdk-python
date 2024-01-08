<!-- Start SDK Example Usage [usage] -->
```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.get_versions()

if res.get_versions_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->