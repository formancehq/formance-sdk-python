# SDK


## Overview

Formance Stack API: Open, modular foundation for unique payments flows

# Introduction
This API is documented in **OpenAPI format**.

# Authentication
Formance Stack offers one forms of authentication:
  - OAuth2
OAuth2 - an open protocol to allow secure authorization in a simple
and standard method from web, mobile and desktop applications.
<SecurityDefinitions />


### Available Operations

* [get_versions](#get_versions) - Show stack version information
* [get_api_auth_well_known_openid_configuration](#get_api_auth_well_known_openid_configuration)

## get_versions

Show stack version information

### Example Usage

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


### Response

**[operations.GetVersionsResponse](../../models/operations/getversionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_api_auth_well_known_openid_configuration

### Example Usage

```python
import sdk

s = sdk.SDK(
    authorization="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.get_api_auth_well_known_openid_configuration()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIAuthWellKnownOpenidConfigurationResponse](../../models/operations/getapiauthwellknownopenidconfigurationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
