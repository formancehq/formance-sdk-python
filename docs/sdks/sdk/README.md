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

## get_versions

Show stack version information

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersions" method="get" path="/versions" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.get_versions()

    assert res.get_versions_response is not None

    # Handle response
    print(res.get_versions_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.GetVersionsResponse](../../models/operations/getversionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |