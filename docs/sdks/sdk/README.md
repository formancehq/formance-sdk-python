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

* [get_oidc_well_knowns](#get_oidc_well_knowns) - Retrieve OpenID connect well-knowns.
* [get_versions](#get_versions) - Show stack version information

## get_oidc_well_knowns

Retrieve OpenID connect well-knowns.

### Example Usage

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

### Response

**[operations.GetOIDCWellKnownsResponse](../../models/operations/getoidcwellknownsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get_versions

Show stack version information

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
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
| errors.SDKError | 4xx-5xx         | */*             |
