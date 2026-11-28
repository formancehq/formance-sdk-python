# Connectivity.V1

## Overview

### Available Operations

* [connectivity_info](#connectivity_info) - Build information
* [create_connection](#create_connection) - Create a Connection
* [delete_connection](#delete_connection) - Delete a Connection
* [get_connection](#get_connection) - Get a Connection
* [get_connector](#get_connector) - Get a Connector (lean connector metadata)
* [get_connector_facets](#get_connector_facets) - Facet-value distribution over the published catalogue
* [get_connector_version](#get_connector_version) - Get one Connector version (including its configSchema and additionalMetadata)
* [get_query_capabilities](#get_query_capabilities) - The filterable keys, operators and value enums per resource
* [healthcheck](#healthcheck) - Health probe
* [list_connections](#list_connections) - List connector instances for this tenant
* [list_connector_versions](#list_connector_versions) - List the installable versions of a Connector
* [list_connectors](#list_connectors) - List published Connectors with their catalogue identity
* [patch_connection](#patch_connection) - Merge-patch a connector instance configuration
* [replace_connection](#replace_connection) - Replace a connector instance configuration

## connectivity_info

Version probe used by the stack gateway to report this module in the
`/versions` aggregation. Response shape follows the platform-wide
ServiceInfo contract.


### Example Usage

<!-- UsageSnippet language="python" operationID="connectivityInfo" method="get" path="/api/connectivity/_info" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.connectivity_info()

    assert res.info is not None

    # Handle response
    print(res.info)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ConnectivityInfoResponse](../../models/operations/connectivityinforesponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## create_connection

Creates a new `Connection` in the caller's environment.
`configuration.connector`, `configuration.ledger` and exactly one of `configuration.version` or
`configuration.channel` are required. `env` and `files` are string key/value maps;
properties marked `format: password` by the selected connector schema
are stored confidentially and omitted from read responses.
Storage metadata and configuration references are rejected on input.
A field outside the tenant contract,
including unsupported instance fields such as `image`, `additionalEnv`,
`additionalFiles` or `replicas`, is rejected with
`400 unsupported_field`.


### Example Usage: channel

<!-- UsageSnippet language="python" operationID="createConnection" method="post" path="/api/connectivity/connections" example="channel" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import connectivity


with SDK() as sdk:

    res = sdk.connectivity.v1.create_connection(request={
        "configuration": {
            "channel": connectivity.ConnectionCreateChannel.STABLE,
            "connector": "stripe",
            "env": {
                "STRIPE_API_KEY": "<your-api-key>",
            },
            "ledger": "main",
            "poll_interval": "30s",
        },
        "name": "stripe-main",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```
### Example Usage: version

<!-- UsageSnippet language="python" operationID="createConnection" method="post" path="/api/connectivity/connections" example="version" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.create_connection(request={
        "configuration": {
            "connector": "bitcoin",
            "env": {
                "RPC_URL": "http://bitcoind:8332",
            },
            "files": {
                "/etc/bitcoin/ca.pem": "<PEM certificate content>",
            },
            "initial_cursor": "AAAAAAAAA+g=",
            "ledger": "btc",
            "version": "v1.4.2",
        },
        "name": "bitcoin-main",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [connectivity.ConnectionCreate](../../models/connectivity/connectioncreate.md)             | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.CreateConnectionSecurity](../../models/operations/createconnectionsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateConnectionResponse](../../models/operations/createconnectionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## delete_connection

Delete a Connection

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConnection" method="delete" path="/api/connectivity/connections/{name}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.delete_connection(request={
        "name": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteConnectionRequest](../../models/operations/deleteconnectionrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.DeleteConnectionSecurity](../../models/operations/deleteconnectionsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.DeleteConnectionResponse](../../models/operations/deleteconnectionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## get_connection

Get a Connection

### Example Usage

<!-- UsageSnippet language="python" operationID="getConnection" method="get" path="/api/connectivity/connections/{name}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.get_connection(request={
        "name": "<value>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetConnectionRequest](../../models/operations/getconnectionrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.GetConnectionSecurity](../../models/operations/getconnectionsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## get_connector

Get a Connector (lean connector metadata)

### Example Usage

<!-- UsageSnippet language="python" operationID="getConnector" method="get" path="/api/connectivity/connectors/{name}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.get_connector(request={
        "name": "<value>",
    })

    assert res.connector is not None

    # Handle response
    print(res.connector)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetConnectorRequest](../../models/operations/getconnectorrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.GetConnectorSecurity](../../models/operations/getconnectorsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetConnectorResponse](../../models/operations/getconnectorresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## get_connector_facets

Counts distinct published `Connector`s per `facet:value` tag (split on
the first `:`; flat tags carry no facet and are excluded), narrowed by
the same `query` filter as the list. `_facets` can never collide with
a connector: names are DNS labels, which cannot contain `_`.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorFacets" method="get" path="/api/connectivity/connectors/_facets" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.get_connector_facets(request={})

    assert res.facet_distribution is not None

    # Handle response
    print(res.facet_distribution)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetConnectorFacetsRequest](../../models/operations/getconnectorfacetsrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.GetConnectorFacetsSecurity](../../models/operations/getconnectorfacetssecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetConnectorFacetsResponse](../../models/operations/getconnectorfacetsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## get_connector_version

Get one Connector version (including its configSchema and additionalMetadata)

### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorVersion" method="get" path="/api/connectivity/connectors/{name}/versions/{version}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.get_connector_version(request={
        "name": "<value>",
        "version": "<value>",
    })

    assert res.connector_version is not None

    # Handle response
    print(res.connector_version)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetConnectorVersionRequest](../../models/operations/getconnectorversionrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetConnectorVersionSecurity](../../models/operations/getconnectorversionsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetConnectorVersionResponse](../../models/operations/getconnectorversionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## get_query_capabilities

Serialized from the same allowlist the server enforces on `?query=`,
so a UI can build its filter bar dynamically and never drift from
what the API accepts.


### Example Usage

<!-- UsageSnippet language="python" operationID="getQueryCapabilities" method="get" path="/api/connectivity/_query/capabilities" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.get_query_capabilities()

    assert res.query_capabilities is not None

    # Handle response
    print(res.query_capabilities)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `security`                                                                                         | [operations.GetQueryCapabilitiesSecurity](../../models/operations/getquerycapabilitiessecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetQueryCapabilitiesResponse](../../models/operations/getquerycapabilitiesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## healthcheck

Single health endpoint, probed by the stack gateway for the `/versions`
aggregation and by service readiness/liveness probes. Ready
means the service can reach its storage dependency.


### Example Usage

<!-- UsageSnippet language="python" operationID="healthcheck" method="get" path="/api/connectivity/_healthcheck" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.healthcheck()

    assert res.health is not None

    # Handle response
    print(res.health)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.HealthcheckResponse](../../models/operations/healthcheckresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| connectivity.HealthError | 500                      | application/json         |
| connectivity.Error       | 4XX                      | application/json         |
| connectivity.Error       | 5XX                      | application/json         |

## list_connections

List connector instances for this tenant

### Example Usage

<!-- UsageSnippet language="python" operationID="listConnections" method="get" path="/api/connectivity/connections" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.list_connections(request={})

    assert res.connection_cursor is not None

    # Handle response
    print(res.connection_cursor)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListConnectionsRequest](../../models/operations/listconnectionsrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ListConnectionsSecurity](../../models/operations/listconnectionssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListConnectionsResponse](../../models/operations/listconnectionsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## list_connector_versions

Returns the `ConnectorVersion`s published for this Connector, sorted
ascending by semantic version. Use `configuration.version` to pin a Connection,
or `configuration.channel` to track a maturity channel.


### Example Usage

<!-- UsageSnippet language="python" operationID="listConnectorVersions" method="get" path="/api/connectivity/connectors/{name}/versions" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.list_connector_versions(request={
        "name": "<value>",
    })

    assert res.connector_version_cursor is not None

    # Handle response
    print(res.connector_version_cursor)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListConnectorVersionsRequest](../../models/operations/listconnectorversionsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListConnectorVersionsSecurity](../../models/operations/listconnectorversionssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListConnectorVersionsResponse](../../models/operations/listconnectorversionsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## list_connectors

Returns the published `Connector`s, each carrying the identity of its
newest Validated version (branding, tagline, tags, `latestVersion`) so
a catalogue UI renders and filters from this single request.


### Example Usage

<!-- UsageSnippet language="python" operationID="listConnectors" method="get" path="/api/connectivity/connectors" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.list_connectors(request={})

    assert res.connector_cursor is not None

    # Handle response
    print(res.connector_cursor)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListConnectorsRequest](../../models/operations/listconnectorsrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ListConnectorsSecurity](../../models/operations/listconnectorssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListConnectorsResponse](../../models/operations/listconnectorsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## patch_connection

JSON merge patch (RFC 7396) over tenant `configuration` fields only. Other fields
are rejected with `400 unsupported_field`. `env` and `files` are string
maps: omitted entries are preserved, including secret-backed values;
`null` deletes a field or map entry. A supplied literal replaces the
stored source. `connector` and `ledger` are not PATCH fields: any presence, including
unchanged values and null, returns `400 unsupported_field`. The merged
result must retain exactly one of `version` and `channel`, so
switching selectors sends `null` for the other one.


### Example Usage: rotatePassword

<!-- UsageSnippet language="python" operationID="patchConnection" method="patch" path="/api/connectivity/connections/{name}" example="rotatePassword" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.patch_connection(request={
        "connection_patch": {
            "configuration": {
                "env": {
                    "STRIPE_API_KEY": "<new-api-key>",
                },
            },
        },
        "name": "<value>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```
### Example Usage: suspend

<!-- UsageSnippet language="python" operationID="patchConnection" method="patch" path="/api/connectivity/connections/{name}" example="suspend" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.patch_connection(request={
        "connection_patch": {
            "configuration": {
                "suspend": True,
            },
        },
        "name": "<value>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```
### Example Usage: switchToChannel

<!-- UsageSnippet language="python" operationID="patchConnection" method="patch" path="/api/connectivity/connections/{name}" example="switchToChannel" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import connectivity


with SDK() as sdk:

    res = sdk.connectivity.v1.patch_connection(request={
        "connection_patch": {
            "configuration": {
                "channel": connectivity.ConnectionPatchChannel.STABLE,
                "version": None,
            },
        },
        "name": "<value>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchConnectionRequest](../../models/operations/patchconnectionrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.PatchConnectionSecurity](../../models/operations/patchconnectionsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchConnectionResponse](../../models/operations/patchconnectionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |

## replace_connection

Full-replace semantics on mutable tenant `configuration`: omitted mutable
fields are cleared. The API does not write fields outside its tenant scope.
`status` is preserved. `connector` and `ledger` are immutable once set:
omission preserves them, first assignment and unchanged values are accepted,
and changes or null return `422 connector_immutable` or `422 ledger_immutable`. Read responses omit reference-backed entries,
so PUT must supply the complete configuration, including required secrets.
Use PATCH to preserve omitted configuration. Fields outside the tenant contract are rejected with
`400 unsupported_field`.


### Example Usage

<!-- UsageSnippet language="python" operationID="replaceConnection" method="put" path="/api/connectivity/connections/{name}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.connectivity.v1.replace_connection(request={
        "connection_update": {
            "configuration": {},
        },
        "name": "<value>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ReplaceConnectionRequest](../../models/operations/replaceconnectionrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ReplaceConnectionSecurity](../../models/operations/replaceconnectionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ReplaceConnectionResponse](../../models/operations/replaceconnectionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| connectivity.Error | 4XX                | application/json   |
| connectivity.Error | 5XX                | application/json   |