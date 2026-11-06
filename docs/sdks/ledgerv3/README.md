# Ledger.V3

## Overview

### Available Operations

* [add_account_type](#add_account_type) - Add an account type
* [aggregate_volumes](#aggregate_volumes) - Aggregate volumes
* [analyze_accounts](#analyze_accounts) - Analyze accounts and suggest a Chart of Accounts
* [analyze_numscript](#analyze_numscript) - Analyze Numscript source
* [analyze_transactions](#analyze_transactions) - Analyze transaction flow patterns
* [bulk_operations](#bulk_operations) - Bulk operations
* [clusterz](#clusterz) - Cluster-availability probe
* [create_index](#create_index) - Create an index on a ledger
* [create_ledger](#create_ledger) - Create a new ledger
* [create_prepared_query](#create_prepared_query) - Create a prepared query
* [create_transaction](#create_transaction) - Create a new transaction
* [delete_account_metadata](#delete_account_metadata) - Delete account metadata
* [delete_ledger](#delete_ledger) - Delete a ledger
* [delete_ledger_metadata](#delete_ledger_metadata) - Delete ledger metadata
* [delete_prepared_query](#delete_prepared_query) - Delete a prepared query
* [delete_transaction_metadata](#delete_transaction_metadata) - Delete transaction metadata
* [drop_index](#drop_index) - Drop an index from a ledger
* [execute_prepared_query](#execute_prepared_query) - Execute a prepared query
* [get_account](#get_account) - Get an account
* [get_account_type](#get_account_type) - Get an account type
* [get_audit_entry](#get_audit_entry) - Get an audit entry
* [get_bucket_index](#get_bucket_index) - Get a single bucket-scoped index registry entry
* [get_bucket_index_entry_status](#get_bucket_index_entry_status) - Get the per-replica status of a single bucket-scoped index
* [get_events_sinks](#get_events_sinks) - List configured event sinks
* [get_index](#get_index) - Get a single index registry entry
* [get_index_entry_status](#get_index_entry_status) - Get the per-replica status of a single index
* [get_index_status](#get_index_status) - Get aggregated index registry status
* [get_ledger](#get_ledger) - Get a ledger
* [get_ledger_stats](#get_ledger_stats) - Get ledger statistics
* [get_log](#get_log) - Get a single system log by bucket-wide sequence
* [get_metadata_schema_status](#get_metadata_schema_status) - Get metadata schema
* [get_numscript](#get_numscript) - Get a numscript
* [get_numscript_usage](#get_numscript_usage) - Get template usage
* [get_transaction](#get_transaction) - Get a transaction
* [health](#health) - Health check
* [info](#info) - Get server build information
* [inspect_index](#inspect_index) - Inspect a metadata index
* [list_account_types](#list_account_types) - List account types
* [list_accounts](#list_accounts) - List accounts
* [list_all_ledgers](#list_all_ledgers) - List all ledgers
* [list_audit_entries](#list_audit_entries) - List audit entries
* [list_bucket_indexes](#list_bucket_indexes) - List bucket-wide indexes
* [list_ledger_indexes](#list_ledger_indexes) - List indexes for a ledger
* [list_ledger_logs](#list_ledger_logs) - List logs for a ledger
* [list_ledger_transactions](#list_ledger_transactions) - List transactions for a ledger
* [list_numscript_versions](#list_numscript_versions) - List numscript versions
* [list_numscripts](#list_numscripts) - List all numscripts
* [list_prepared_queries](#list_prepared_queries) - List prepared queries
* [list_signing_keys](#list_signing_keys) - List registered Ed25519 signing keys
* [livez](#livez) - Liveness probe
* [promote_ledger](#promote_ledger) - Promote a mirror ledger
* [readyz](#readyz) - Readiness probe
* [remove_account_type](#remove_account_type) - Remove an account type
* [remove_events_sink](#remove_events_sink) - Remove an event sink
* [remove_metadata_field_type](#remove_metadata_field_type) - Remove metadata field type
* [revert_transaction](#revert_transaction) - Revert a transaction
* [save_account_metadata](#save_account_metadata) - Save account metadata
* [save_ledger_metadata](#save_ledger_metadata) - Save ledger metadata
* [save_numscript](#save_numscript) - Save a numscript
* [save_transaction_metadata](#save_transaction_metadata) - Save transaction metadata
* [set_default_enforcement_mode](#set_default_enforcement_mode) - Set default enforcement mode
* [set_metadata_field_type](#set_metadata_field_type) - Set metadata field type
* [update_prepared_query](#update_prepared_query) - Update a prepared query

## add_account_type

Adds a new account type to a ledger's chart of accounts. Account types define
address patterns for account validation. Requires `ledger:WriteMetadata` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3AddAccountType" method="post" path="/api/ledger/v3/{ledgerName}/account-types" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3


with SDK() as sdk:

    res = sdk.ledger.v3.add_account_type(request={
        "add_account_type_request": {
            "name": "user-checking",
            "pattern": "users:{id}:checking",
            "persistence": ledger_v3.AddAccountTypeRequestPersistence.EPHEMERAL,
            "segment_types": {
                "id": {
                    "type": ledger_v3.SegmentTypeType.UUID,
                },
            },
        },
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3AddAccountTypeRequest](../../models/operations/v3addaccounttyperequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3AddAccountTypeSecurity](../../models/operations/v3addaccounttypesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3AddAccountTypeResponse](../../models/operations/v3addaccounttyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## aggregate_volumes

Returns aggregated volumes (input/output/balance per asset) across all accounts in the ledger.
Supports filtering accounts with the generic `filter` parameter, grouping by account prefixes,
and max-precision merging.
Requires `ledger:ReadAccount` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3AggregateVolumes" method="get" path="/api/ledger/v3/{ledgerName}/volumes" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.aggregate_volumes(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
    })

    assert res.aggregate_volumes_response is not None

    # Handle response
    print(res.aggregate_volumes_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V3AggregateVolumesRequest](../../models/operations/v3aggregatevolumesrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.V3AggregateVolumesSecurity](../../models/operations/v3aggregatevolumessecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V3AggregateVolumesResponse](../../models/operations/v3aggregatevolumesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## analyze_accounts

Scans all accounts in a ledger, discovers address patterns, and returns a
suggested Chart of Accounts. Useful after a mirror import to understand
account structure. Requires `ledger:read` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3AnalyzeAccounts" method="get" path="/api/ledger/v3/{ledgerName}/analyze-accounts" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.analyze_accounts(request={
        "ledger_name": "<value>",
    })

    assert res.analyze_accounts_response is not None

    # Handle response
    print(res.analyze_accounts_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V3AnalyzeAccountsRequest](../../models/operations/v3analyzeaccountsrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.V3AnalyzeAccountsSecurity](../../models/operations/v3analyzeaccountssecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.V3AnalyzeAccountsResponse](../../models/operations/v3analyzeaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## analyze_numscript

Validates Numscript v1 and returns the external input schema without reading or changing ledger state. Recognized source failures are returned as diagnostics with an empty input list. Sources over 64 KiB or with more than 32 block-comment open markers receive a syntax diagnostic; internal failures return a server error.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3AnalyzeNumscript" method="post" path="/api/ledger/v3/numscripts/analyze" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.analyze_numscript(request={
        "source": "<value>",
        "version": "v1",
    })

    assert res.analyze_numscript_response is not None

    # Handle response
    print(res.analyze_numscript_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [ledger_v3.AnalyzeNumscriptRequest](../../models/ledger_v3/analyzenumscriptrequest.md)         | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.V3AnalyzeNumscriptSecurity](../../models/operations/v3analyzenumscriptsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V3AnalyzeNumscriptResponse](../../models/operations/v3analyzenumscriptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## analyze_transactions

Scans all transactions in a ledger, discovers flow patterns by normalizing
account addresses, and returns statistics per flow type including temporal
distribution and volume metrics. Requires `ledger:read` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3AnalyzeTransactions" method="get" path="/api/ledger/v3/{ledgerName}/analyze-transactions" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.analyze_transactions(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
    })

    assert res.analyze_transactions_response is not None

    # Handle response
    print(res.analyze_transactions_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3AnalyzeTransactionsRequest](../../models/operations/v3analyzetransactionsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3AnalyzeTransactionsSecurity](../../models/operations/v3analyzetransactionssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3AnalyzeTransactionsResponse](../../models/operations/v3analyzetransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## bulk_operations

Execute multiple operations (create transactions, add metadata,
revert transactions, delete metadata) in a single request. Requires
`ledger:write` scope.

With `atomic=true`, all elements target the URL's ledger and are
submitted as one batch. `Idempotency-Key` identifies that whole batch;
per-element `ik` values are ignored. With `atomic=false`
(default), each element is submitted separately under its own
`ik`; the header is ignored.

`continueOnFailure` controls sequential continuation and business-error
status rollup. It does not allow partial application of an atomic
batch. Non-atomic failures can follow already committed elements:
inspect every result and preserve the original identities when retrying.
A timeout or infrastructure failure does not prove that work was not
committed. This contract does not enable automatic SDK retries.

The response status is decided in three tiers:

1. **Request-level failures** (before per-element processing):
   malformed body → `400`, missing/insufficient scope → `401` or
   `403`, too many elements → `413`. Exceeding the byte limit while
   decoding the body currently returns `400`.
   Returned unconditionally, `continueOnFailure` does not apply.
2. **Infrastructure failures during processing** (transport
   timeout, cache-horizon exceeded, storage error): the overall
   status is `503` for retryable failures and `500` otherwise,
   regardless of `continueOnFailure`. Callers
   must inspect the element outcomes before deciding what to retry.
3. **Per-element errors during processing**: each element's error
   carries the HTTP status it would surface as a single request
   (via the same mapping `handleError` uses). The top-level
   status is the "worst" of them, with `continueOnFailure`
   applying only to per-element business failures (4xx):
   - Business failures (validation, not-found, conflict,
     precondition, permission — 4xx): rolled up per
     `continueOnFailure`. `true` → `200`; `false` (default) →
     the highest 4xx among failing elements (typically `400`).
   - Resource exhaustion (`KindResourceExhausted`, `429`), including
     rate limits and permanent authoritative-sequence exhaustion:
     surface unconditionally as `429`.
   - Retryable infrastructure failures (leader loss,
     cache-horizon exceeded, `KindUnavailable`): surface as
     `503` with `Retry-After: 1`, regardless of
     `continueOnFailure`.
   - Non-retryable infrastructure failures (transport / storage
     errors, `KindInternal`, unclassified): surface as `500`.
   - Aborted elements (`context.Canceled` from the sequential
     runner after a prior failure): contribute nothing — the
     originating error drives the rollup.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3BulkOperations" method="post" path="/api/ledger/v3/{ledgerName}/bulk" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.bulk_operations(request={
        "formance_bigint_as_string": "true",
        "request_body": [],
        "ledger_name": "<value>",
    })

    assert res.bulk_response is not None

    # Handle response
    print(res.bulk_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3BulkOperationsRequest](../../models/operations/v3bulkoperationsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3BulkOperationsSecurity](../../models/operations/v3bulkoperationssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3BulkOperationsResponse](../../models/operations/v3bulkoperationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## clusterz

Returns 200 only when the node is part of a healthy cluster (Raft state
healthy and a leader elected). Disk and clock skew gate writes (see
admission), not cluster readiness. Returns 503 otherwise. Use this
for external monitoring or any client that needs to wait until the node
can actually serve cluster-dependent traffic. Kubernetes readiness
probes should target `/readyz` instead — this endpoint MUST NOT gate
StatefulSet ordering, otherwise the cluster cannot recover from a
full-kill cold start.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3Clusterz" method="get" path="/api/ledger/clusterz" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.clusterz()

    assert res.health_response is not None

    # Handle response
    print(res.health_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.V3ClusterzSecurity](../../models/operations/v3clusterzsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V3ClusterzResponse](../../models/operations/v3clusterzresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_index

Registers a new index on the ledger. An existing canonical index on
this ledger is rejected with `INDEX_ALREADY_EXISTS` (HTTP 409), even
while building or retyping, without changing its definition or progress.
Replaying an identical batch with its retained `Idempotency-Key` returns
the original result. The indexbuilder processes the accepted creation.
The request body carries the target `IndexID` in
canonical form (see `DELETE /v3/{ledgerName}/indexes/{canonicalId}`
for the format). Requires `ledger:WriteLedger` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreateIndex" method="post" path="/api/ledger/v3/{ledgerName}/indexes" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.create_index(request={
        "request_body": {
            "id": "metadata:TARGET_TYPE_ACCOUNT:color",
        },
        "ledger_name": "<value>",
    })

    assert res.create_index_response is not None

    # Handle response
    print(res.create_index_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.V3CreateIndexRequest](../../models/operations/v3createindexrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.V3CreateIndexSecurity](../../models/operations/v3createindexsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.V3CreateIndexResponse](../../models/operations/v3createindexresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ledger

Creates a new ledger with the specified name. Storage is configured at the server level.
Each ledger has its own Raft group for data consistency. Requires `ledger:write` scope.

The ledger name `_` is reserved: all system / non-ledger routes live
under the `/v3/_/…` segment (e.g. `/v3/_/audit-entries`), so a ledger
named `_` would be unreachable over REST. Creating it is rejected with a
validation error. The exact name `_system` is also reserved for system
events and rejected. Other underscore-prefixed names remain valid.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreateLedger" method="post" path="/api/ledger/v3/{ledgerName}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3


with SDK() as sdk:

    res = sdk.ledger.v3.create_ledger(request={
        "create_ledger_request": {
            "account_types": {
                "user-checking": {
                    "name": "user-checking",
                    "pattern": "users:{id}:checking",
                    "persistence": ledger_v3.AddAccountTypeRequestPersistence.EPHEMERAL,
                    "segment_types": {
                        "id": {
                            "type": ledger_v3.SegmentTypeType.UUID,
                        },
                    },
                },
            },
            "initial_schema": [
                {
                    "key": "color",
                    "target_type": ledger_v3.MetadataFieldTypeCommandTargetType.ACCOUNT,
                    "type": ledger_v3.MetadataFieldTypeCommandType.STRING,
                },
            ],
        },
        "ledger_name": "<value>",
    })

    assert res.create_ledger_response is not None

    # Handle response
    print(res.create_ledger_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V3CreateLedgerRequest](../../models/operations/v3createledgerrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.V3CreateLedgerSecurity](../../models/operations/v3createledgersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V3CreateLedgerResponse](../../models/operations/v3createledgerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_prepared_query

Creates a new prepared query for a ledger. A prepared query defines a reusable
filter that can be executed later with parameter substitution. Requires `ledger:WriteQuery` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreatePreparedQuery" method="post" path="/api/ledger/v3/{ledgerName}/prepared-queries" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3, operations


with SDK() as sdk:

    res = sdk.ledger.v3.create_prepared_query(request=operations.V3CreatePreparedQueryRequest(
        create_prepared_query_request=ledger_v3.CreatePreparedQueryRequest(
            name="<value>",
            target=ledger_v3.CreatePreparedQueryRequestTarget.ACCOUNTS,
        ),
        ledger_name="<value>",
    ))

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3CreatePreparedQueryRequest](../../models/operations/v3createpreparedqueryrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3CreatePreparedQuerySecurity](../../models/operations/v3createpreparedquerysecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3CreatePreparedQueryResponse](../../models/operations/v3createpreparedqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_transaction

Creates a new transaction in the specified ledger with the specified postings. Requires `ledger:write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3CreateTransaction" method="post" path="/api/ledger/v3/{ledgerName}/transactions" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.create_transaction(request={
        "create_transaction_request": {},
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
    })

    assert res.create_transaction_response is not None

    # Handle response
    print(res.create_transaction_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3CreateTransactionRequest](../../models/operations/v3createtransactionrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.V3CreateTransactionSecurity](../../models/operations/v3createtransactionsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3CreateTransactionResponse](../../models/operations/v3createtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_account_metadata

Deletes a metadata key for a specific account in the ledger. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeleteAccountMetadata" method="delete" path="/api/ledger/v3/{ledgerName}/accounts/{address}/metadata/{key}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.delete_account_metadata(request={
        "address": "users:001",
        "key": "formance.com/reviewed",
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V3DeleteAccountMetadataRequest](../../models/operations/v3deleteaccountmetadatarequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.V3DeleteAccountMetadataSecurity](../../models/operations/v3deleteaccountmetadatasecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.V3DeleteAccountMetadataResponse](../../models/operations/v3deleteaccountmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_ledger

Deletes a ledger by its name. This operation removes the ledger and its associated Raft group from the cluster. Requires `ledger:write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeleteLedger" method="delete" path="/api/ledger/v3/{ledgerName}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.delete_ledger(request={
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V3DeleteLedgerRequest](../../models/operations/v3deleteledgerrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.V3DeleteLedgerSecurity](../../models/operations/v3deleteledgersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V3DeleteLedgerResponse](../../models/operations/v3deleteledgerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_ledger_metadata

Deletes a metadata key from the ledger. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeleteLedgerMetadata" method="delete" path="/api/ledger/v3/{ledgerName}/metadata/{key}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.delete_ledger_metadata(request={
        "key": "formance.com/reviewed",
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3DeleteLedgerMetadataRequest](../../models/operations/v3deleteledgermetadatarequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.V3DeleteLedgerMetadataSecurity](../../models/operations/v3deleteledgermetadatasecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3DeleteLedgerMetadataResponse](../../models/operations/v3deleteledgermetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_prepared_query

Deletes a prepared query from a ledger. Requires `ledger:WriteQuery` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeletePreparedQuery" method="delete" path="/api/ledger/v3/{ledgerName}/prepared-queries/{queryName}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.delete_prepared_query(request={
        "ledger_name": "<value>",
        "query_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3DeletePreparedQueryRequest](../../models/operations/v3deletepreparedqueryrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3DeletePreparedQuerySecurity](../../models/operations/v3deletepreparedquerysecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3DeletePreparedQueryResponse](../../models/operations/v3deletepreparedqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_transaction_metadata

Deletes a metadata key for a specific transaction in the ledger. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3DeleteTransactionMetadata" method="delete" path="/api/ledger/v3/{ledgerName}/transactions/{transactionId}/metadata/{key}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.delete_transaction_metadata(request={
        "key": "formance.com/reviewed",
        "ledger_name": "<value>",
        "transaction_id": 831017,
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.V3DeleteTransactionMetadataRequest](../../models/operations/v3deletetransactionmetadatarequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.V3DeleteTransactionMetadataSecurity](../../models/operations/v3deletetransactionmetadatasecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.V3DeleteTransactionMetadataResponse](../../models/operations/v3deletetransactionmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## drop_index

Removes an index from a ledger. The path parameter carries the target
`IndexID` in canonical form (e.g. `metadata:TARGET_TYPE_ACCOUNT:color`,
`tx_builtin:TX_BUILTIN_INDEX_TIMESTAMP`). Requires `ledger:WriteLedger` scope.

The drop is idempotent. An `IndexID` that has no registry entry on the
ledger (never created, or already dropped) also answers `204`, and each
committed drop appends a `DROP_INDEX` entry to the ledger log. A
mistyped canonical id is therefore not reported; read the index with
`GET /v3/{ledgerName}/indexes/{canonicalId}` first when the caller must
know that it exists. `404` means that the ledger does not exist.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3DropIndex" method="delete" path="/api/ledger/v3/{ledgerName}/indexes/{canonicalId}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.drop_index(request={
        "canonical_id": "<id>",
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V3DropIndexRequest](../../models/operations/v3dropindexrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.V3DropIndexSecurity](../../models/operations/v3dropindexsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V3DropIndexResponse](../../models/operations/v3dropindexresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## execute_prepared_query

Executes a prepared query with optional parameter substitution. Supports LIST and
AGGREGATE_VOLUMES modes. LIST uses cursor pagination with an effective page size
of 100 when omitted or zero, capped at 1000 before collecting and enriching rows.
AGGREGATE_VOLUMES ignores pageSize and aggregates all matching accounts. Also
accepts pageSize, cursor and reverse as query parameters. Supplied pageSize and
reverse values, and nonempty cursor values, override the body. Requires `ledger:ReadQuery` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ExecutePreparedQuery" method="post" path="/api/ledger/v3/{ledgerName}/prepared-queries/{queryName}/execute" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.execute_prepared_query(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
        "query_name": "<value>",
    })

    assert res.execute_prepared_query_response is not None

    # Handle response
    print(res.execute_prepared_query_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3ExecutePreparedQueryRequest](../../models/operations/v3executepreparedqueryrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.V3ExecutePreparedQuerySecurity](../../models/operations/v3executepreparedquerysecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3ExecutePreparedQueryResponse](../../models/operations/v3executepreparedqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_account

Retrieves account information including metadata for a specific account address. Requires `ledger:read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetAccount_ledgerV3" method="get" path="/api/ledger/v3/{ledgerName}/accounts/{address}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_account(request={
        "formance_bigint_as_string": "true",
        "address": "users:001",
        "ledger_name": "<value>",
    })

    assert res.get_account_response is not None

    # Handle response
    print(res.get_account_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.V3GetAccountLedgerV3Request](../../models/operations/v3getaccountledgerv3request.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.V3GetAccountLedgerV3Security](../../models/operations/v3getaccountledgerv3security.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.V3GetAccountLedgerV3Response](../../models/operations/v3getaccountledgerv3response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_account_type

Retrieves a specific account type by name from a ledger. Requires `ledger:ReadAccount` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetAccountType" method="get" path="/api/ledger/v3/{ledgerName}/account-types/{typeName}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_account_type(request={
        "ledger_name": "<value>",
        "type_name": "<value>",
    })

    assert res.get_account_type_response is not None

    # Handle response
    print(res.get_account_type_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetAccountTypeRequest](../../models/operations/v3getaccounttyperequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3GetAccountTypeSecurity](../../models/operations/v3getaccounttypesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetAccountTypeResponse](../../models/operations/v3getaccounttyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_audit_entry

Returns a single audit entry by its global sequence, with per-order
`items` populated (the list endpoint omits `items` for compactness).
Requires `ledger:ReadAudit` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetAuditEntry" method="get" path="/api/ledger/v3/_/audit-entries/{sequence}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_audit_entry(request={
        "sequence": 98403,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V3GetAuditEntryRequest](../../models/operations/v3getauditentryrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.V3GetAuditEntrySecurity](../../models/operations/v3getauditentrysecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V3GetAuditEntryResponse](../../models/operations/v3getauditentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_bucket_index

Returns the `Index` registry entry for a bucket-scoped index
(`Ledger == ""`, e.g. audit indexes). Ledger-scoped lookups go
through `GET /v3/{ledgerName}/indexes/{canonicalId}` — the two
keyspaces are distinct so a bucket-scoped lookup with the same
canonical will NotFound if only the ledger-scoped entry exists.
Requires `ledger:ReadOps` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetBucketIndex" method="get" path="/api/ledger/v3/_/indexes/{canonicalId}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_bucket_index(request={
        "canonical_id": "<id>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetBucketIndexRequest](../../models/operations/v3getbucketindexrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3GetBucketIndexSecurity](../../models/operations/v3getbucketindexsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetBucketIndexResponse](../../models/operations/v3getbucketindexresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_bucket_index_entry_status

Returns the `IndexEntry` (registry entry + backfill cursor +
per-replica IndexVersionState) for a bucket-scoped index.
Requires `ledger:ReadOps` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetBucketIndexEntryStatus" method="get" path="/api/ledger/v3/_/indexes/{canonicalId}/status" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_bucket_index_entry_status(request={
        "canonical_id": "<id>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.V3GetBucketIndexEntryStatusRequest](../../models/operations/v3getbucketindexentrystatusrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.V3GetBucketIndexEntryStatusSecurity](../../models/operations/v3getbucketindexentrystatussecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.V3GetBucketIndexEntryStatusResponse](../../models/operations/v3getbucketindexentrystatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_events_sinks

Returns every event sink configured on the cluster. Requires
`ledger:ReadOps` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetEventsSinks" method="get" path="/api/ledger/v3/_/events-sinks" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_events_sinks(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetEventsSinksRequest](../../models/operations/v3geteventssinksrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3GetEventsSinksSecurity](../../models/operations/v3geteventssinkssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetEventsSinksResponse](../../models/operations/v3geteventssinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_index

Returns the `Index` registry entry (id, ledger, createdAt,
forwardEncodingVersion) for a single index, serialized in
protobuf-JSON camelCase. Requires `ledger:ReadLedger` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetIndex" method="get" path="/api/ledger/v3/{ledgerName}/indexes/{canonicalId}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_index(request={
        "canonical_id": "<id>",
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.V3GetIndexRequest](../../models/operations/v3getindexrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.V3GetIndexSecurity](../../models/operations/v3getindexsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.V3GetIndexResponse](../../models/operations/v3getindexresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_index_entry_status

Returns the `IndexEntry` for a single index — the registry entry
joined with the backfill cursor and the per-replica
IndexVersionState (current + pending version). Use this to poll
for backfill completion after a `POST /v3/{ledgerName}/indexes`.
Requires `ledger:ReadLedger` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetIndexEntryStatus" method="get" path="/api/ledger/v3/{ledgerName}/indexes/{canonicalId}/status" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_index_entry_status(request={
        "canonical_id": "<id>",
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3GetIndexEntryStatusRequest](../../models/operations/v3getindexentrystatusrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3GetIndexEntryStatusSecurity](../../models/operations/v3getindexentrystatussecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3GetIndexEntryStatusResponse](../../models/operations/v3getindexentrystatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_index_status

Returns the aggregated index registry status: per-index backfill cursor,
per-replica IndexVersionState (current/pending), and cluster-wide
counters (LastIndexedSequence, LastLogSequence, Lag, IndexFileSize).
The optional `ledger` query parameter narrows the per-index entries to
a single ledger; the aggregated counters always cover the bucket.
Requires `ledger:ReadOps` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetIndexStatus" method="get" path="/api/ledger/v3/_/indexes/status" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_index_status(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetIndexStatusRequest](../../models/operations/v3getindexstatusrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3GetIndexStatusSecurity](../../models/operations/v3getindexstatussecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetIndexStatusResponse](../../models/operations/v3getindexstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ledger

Retrieves a ledger by its name. Requires `ledger:read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetLedger" method="get" path="/api/ledger/v3/{ledgerName}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_ledger(request={
        "ledger_name": "<value>",
    })

    assert res.get_ledger_response is not None

    # Handle response
    print(res.get_ledger_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.V3GetLedgerRequest](../../models/operations/v3getledgerrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.V3GetLedgerSecurity](../../models/operations/v3getledgersecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.V3GetLedgerResponse](../../models/operations/v3getledgerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ledger_stats

Returns aggregate usage statistics (transaction, volume, reference, posting, log, revert and Numscript-execution counts, plus ephemeral-evicted and transient-used volume tallies) for a ledger. Requires `ledger:read` scope. On live reads, `transactionCount` and `logCount` are FSM-backed. The seven usage-derived counters (`postingCount`, `revertCount`, `numscriptExecutionCount`, `referenceCount`, `ephemeralEvictedCount`, `transientUsedCount`, `volumeCount`) are materialised asynchronously in the serving replica's usagestore and may lag committed state even after the request's ReadIndex barrier. Note: for checkpoint-scoped (historical) reads, only `transactionCount` and `logCount` are checkpoint-consistent; the usage-derived counters (`postingCount`, `revertCount`, `numscriptExecutionCount`, `referenceCount`, `ephemeralEvictedCount`, `transientUsedCount`, `volumeCount`) are sourced from the live usagestore projection, which is not checkpoint-aware, and are returned as `0` at a checkpoint rather than a live value — treat `0` on a checkpoint read as "not available at this checkpoint".

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetLedgerStats" method="get" path="/api/ledger/v3/{ledgerName}/stats" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_ledger_stats(request={
        "ledger_name": "<value>",
    })

    assert res.get_ledger_stats_response is not None

    # Handle response
    print(res.get_ledger_stats_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetLedgerStatsRequest](../../models/operations/v3getledgerstatsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3GetLedgerStatsSecurity](../../models/operations/v3getledgerstatssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetLedgerStatsResponse](../../models/operations/v3getledgerstatsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_log

Returns the system log entry with the given bucket-wide sequence number.
Requires `ledger:ReadOps` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetLog" method="get" path="/api/ledger/v3/_/logs/{sequence}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_log(request={
        "formance_bigint_as_string": "true",
        "sequence": 593519,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.V3GetLogRequest](../../models/operations/v3getlogrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.V3GetLogSecurity](../../models/operations/v3getlogsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.V3GetLogResponse](../../models/operations/v3getlogresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadata_schema_status

Returns the declared type of every metadata field on a ledger. Requires `ledger:read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetMetadataSchemaStatus" method="get" path="/api/ledger/v3/{ledgerName}/metadata-schema" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_metadata_schema_status(request={
        "ledger_name": "<value>",
    })

    assert res.metadata_schema_status_response is not None

    # Handle response
    print(res.metadata_schema_status_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V3GetMetadataSchemaStatusRequest](../../models/operations/v3getmetadataschemastatusrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.V3GetMetadataSchemaStatusSecurity](../../models/operations/v3getmetadataschemastatussecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.V3GetMetadataSchemaStatusResponse](../../models/operations/v3getmetadataschemastatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_numscript

Retrieves a numscript by name from a ledger. Use the `version` query parameter to get a specific
semver version. If omitted or empty, the latest version is returned.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetNumscript" method="get" path="/api/ledger/v3/{ledgerName}/numscripts/{name}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_numscript(request={
        "ledger_name": "<value>",
        "name": "<value>",
    })

    assert res.get_numscript_response is not None

    # Handle response
    print(res.get_numscript_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V3GetNumscriptRequest](../../models/operations/v3getnumscriptrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.V3GetNumscriptSecurity](../../models/operations/v3getnumscriptsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V3GetNumscriptResponse](../../models/operations/v3getnumscriptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_numscript_usage

Returns the invocation counter and last-used timestamp for a Numscript template. Values are
materialised asynchronously by the `usagebuilder` subsystem from the FSM audit chain and may
lag the live FSM while the worker drains pending batches. A never-invoked template returns a
zero-valued response (not 404), so clients handle "never used" uniformly.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetNumscriptUsage" method="get" path="/api/ledger/v3/{ledgerName}/numscripts/{name}/usage" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_numscript_usage(request={
        "ledger_name": "<value>",
        "name": "<value>",
    })

    assert res.get_template_usage_response is not None

    # Handle response
    print(res.get_template_usage_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3GetNumscriptUsageRequest](../../models/operations/v3getnumscriptusagerequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.V3GetNumscriptUsageSecurity](../../models/operations/v3getnumscriptusagesecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3GetNumscriptUsageResponse](../../models/operations/v3getnumscriptusageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_transaction

Retrieves a transaction by its ID from the specified ledger. Requires `ledger:read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3GetTransaction" method="get" path="/api/ledger/v3/{ledgerName}/transactions/{transactionId}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.get_transaction(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
        "transaction_id": 431503,
    })

    assert res.get_transaction_response is not None

    # Handle response
    print(res.get_transaction_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3GetTransactionRequest](../../models/operations/v3gettransactionrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3GetTransactionSecurity](../../models/operations/v3gettransactionsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3GetTransactionResponse](../../models/operations/v3gettransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## health

Returns the health status of the node. Returns 503 if the node is not connected to the cluster.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3Health" method="get" path="/api/ledger/health" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.health()

    assert res.health_response is not None

    # Handle response
    print(res.health_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [operations.V3HealthSecurity](../../models/operations/v3healthsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.V3HealthResponse](../../models/operations/v3healthresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## info

Returns the server build metadata (version, commit, build date, Go runtime version). Unauthenticated.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3Info" method="get" path="/api/ledger/_info" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.info()

    assert res.server_info is not None

    # Handle response
    print(res.server_info)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `security`                                                             | [operations.V3InfoSecurity](../../models/operations/v3infosecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.V3InfoResponse](../../models/operations/v3inforesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## inspect_index

Scans a metadata index and returns distinct values, facets (value + count),
or a summary (cardinality, min/max, existence counts). The index must be
in READY state. Only metadata indexes are inspectable (builtin indexes
return 400). Requires `ledger:read` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3InspectIndex" method="get" path="/api/ledger/v3/{ledgerName}/indexes/{canonicalId}/inspect" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.inspect_index(request={
        "canonical_id": "<id>",
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.V3InspectIndexRequest](../../models/operations/v3inspectindexrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.V3InspectIndexSecurity](../../models/operations/v3inspectindexsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.V3InspectIndexResponse](../../models/operations/v3inspectindexresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_account_types

Returns all account types defined on a ledger, sorted by name.
Requires `ledger:ReadAccount` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListAccountTypes" method="get" path="/api/ledger/v3/{ledgerName}/account-types" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_account_types(request={
        "ledger_name": "<value>",
    })

    assert res.list_account_types_response is not None

    # Handle response
    print(res.list_account_types_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V3ListAccountTypesRequest](../../models/operations/v3listaccounttypesrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.V3ListAccountTypesSecurity](../../models/operations/v3listaccounttypessecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V3ListAccountTypesResponse](../../models/operations/v3listaccounttypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounts

Lists accounts in a ledger in alphabetical order with cursor
pagination and an optional generic `filter` (e.g. address-prefix
selection via `filter=address ^= "users:"`). Requires `ledger:read`
scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListAccounts_ledgerV3" method="get" path="/api/ledger/v3/{ledgerName}/accounts" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_accounts(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3ListAccountsLedgerV3Request](../../models/operations/v3listaccountsledgerv3request.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.V3ListAccountsLedgerV3Security](../../models/operations/v3listaccountsledgerv3security.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3ListAccountsLedgerV3Response](../../models/operations/v3listaccountsledgerv3response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_all_ledgers

Lists the ledgers in the cluster, paged by name (ascending unless
`reverse=true`). Requires `ledger:read` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListAllLedgers" method="get" path="/api/ledger/v3/" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_all_ledgers(request={})

    assert res.list_all_ledgers_response is not None

    # Handle response
    print(res.list_all_ledgers_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3ListAllLedgersRequest](../../models/operations/v3listallledgersrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3ListAllLedgersSecurity](../../models/operations/v3listallledgerssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3ListAllLedgersResponse](../../models/operations/v3listallledgersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_audit_entries

Lists audit trail entries (one per proposal, success or failure) across
the whole bucket, paged by audit sequence (ascending unless
`reverse=true`). Audit reads are
not ledger-scoped in the path — a single proposal can touch several
ledgers — so ledger scope, outcome and other dimensions are expressed
through the `filter` query parameter.

This endpoint always performs a live read and does not expose pinned
checkpoint reads. Filters containing indexed audit conditions wait for
the audit projection to certify the request's fixed main-store horizon;
matching entries are loaded from that same main snapshot. Unfiltered
reads and sequence-only bounds scan the audit zone directly without
waiting for the audit projection.

Requires `ledger:ReadAudit` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListAuditEntries" method="get" path="/api/ledger/v3/_/audit-entries" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_audit_entries(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V3ListAuditEntriesRequest](../../models/operations/v3listauditentriesrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.V3ListAuditEntriesSecurity](../../models/operations/v3listauditentriessecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V3ListAuditEntriesResponse](../../models/operations/v3listauditentriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_bucket_indexes

Streams the bucket-scoped index registry. The `scope` query parameter
selects the flavor: `all` (default, matches the ListIndexesRequest
proto default) streams every entry across ledgers, skipping orphan
entries whose owning ledger no longer exists; `bucket` surfaces only
bucket-scoped entries (empty ledger, e.g. audit indexes). Use
`GET /v3/{ledgerName}/indexes` for the per-ledger view. Requires
`ledger:ReadOps` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListBucketIndexes" method="get" path="/api/ledger/v3/_/indexes" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_bucket_indexes(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3ListBucketIndexesRequest](../../models/operations/v3listbucketindexesrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.V3ListBucketIndexesSecurity](../../models/operations/v3listbucketindexessecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3ListBucketIndexesResponse](../../models/operations/v3listbucketindexesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ledger_indexes

Streams the indexes registered on a specific ledger. Requires
`ledger:ReadLedger` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListLedgerIndexes" method="get" path="/api/ledger/v3/{ledgerName}/indexes" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_ledger_indexes(request={
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3ListLedgerIndexesRequest](../../models/operations/v3listledgerindexesrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.V3ListLedgerIndexesSecurity](../../models/operations/v3listledgerindexessecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3ListLedgerIndexesResponse](../../models/operations/v3listledgerindexesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ledger_logs

Lists log entries for a specific ledger, paged by ledger-local log ID
(ascending unless `reverse=true`).
Requires the builtin `LOG` index to be enabled on the ledger via `CreateIndex`.
Requires `ledger:read` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListLedgerLogs" method="get" path="/api/ledger/v3/{ledgerName}/logs" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_ledger_logs(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3ListLedgerLogsRequest](../../models/operations/v3listledgerlogsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3ListLedgerLogsSecurity](../../models/operations/v3listledgerlogssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3ListLedgerLogsResponse](../../models/operations/v3listledgerlogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ledger_transactions

Lists transactions for a specific ledger. The default order is
newest-first (descending transaction id); pass `reverse=true` to
get oldest-first (ascending). Supports cursor pagination (`pageSize`,
`cursor`), an optional date range (`startDate`/`endDate`),
and the generic `filter` parameter (e.g. reference selection via
`filter={"$match":{"reference":"..."}}`, URL-encoded). Requires
`ledger:ReadTransaction` scope.

This is a live read, linearizable by default. `X-Consistency: stale`
reads the receiving node's local state, which may lag the leader. Every
projection used by the filter is automatically aligned. Unlike the
gRPC API, it does not accept the `checkpointId` option to pin the read
to a specific historical snapshot — use gRPC for checkpoint-pinned
reads. (Tracked follow-up, same carve-out as the audit reads.)


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListLedgerTransactions" method="get" path="/api/ledger/v3/{ledgerName}/transactions" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_ledger_transactions(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.V3ListLedgerTransactionsRequest](../../models/operations/v3listledgertransactionsrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.V3ListLedgerTransactionsSecurity](../../models/operations/v3listledgertransactionssecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.V3ListLedgerTransactionsResponse](../../models/operations/v3listledgertransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_numscript_versions

Returns the numscript's history: its current latest (greatest stored
semver) and every stored version, highest-first.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListNumscriptVersions" method="get" path="/api/ledger/v3/{ledgerName}/numscripts/{name}/versions" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_numscript_versions(request={
        "ledger_name": "<value>",
        "name": "<value>",
    })

    assert res.list_numscript_versions_response is not None

    # Handle response
    print(res.list_numscript_versions_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.V3ListNumscriptVersionsRequest](../../models/operations/v3listnumscriptversionsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.V3ListNumscriptVersionsSecurity](../../models/operations/v3listnumscriptversionssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.V3ListNumscriptVersionsResponse](../../models/operations/v3listnumscriptversionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_numscripts

Lists every numscript of a ledger at its greatest stored version, paged
by name (ascending unless `reverse=true`).


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListNumscripts" method="get" path="/api/ledger/v3/{ledgerName}/numscripts" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_numscripts(request={
        "ledger_name": "<value>",
    })

    assert res.list_numscripts_response is not None

    # Handle response
    print(res.list_numscripts_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.V3ListNumscriptsRequest](../../models/operations/v3listnumscriptsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.V3ListNumscriptsSecurity](../../models/operations/v3listnumscriptssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.V3ListNumscriptsResponse](../../models/operations/v3listnumscriptsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_prepared_queries

Returns a list of all prepared queries for a ledger. Requires `ledger:ReadQuery` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListPreparedQueries" method="get" path="/api/ledger/v3/{ledgerName}/prepared-queries" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_prepared_queries(request={
        "ledger_name": "<value>",
    })

    assert res.list_prepared_queries_response is not None

    # Handle response
    print(res.list_prepared_queries_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3ListPreparedQueriesRequest](../../models/operations/v3listpreparedqueriesrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3ListPreparedQueriesSecurity](../../models/operations/v3listpreparedqueriessecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3ListPreparedQueriesResponse](../../models/operations/v3listpreparedqueriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_keys

Lists the Ed25519 signing keys registered on the cluster, paged by key
id (ascending unless `reverse=true`). Requires `ledger:ReadOps` scope.

This route performs a live read, linearizable by default.
`X-Consistency: stale` reads the receiving node's local state, which
may lag the leader. Signing-key reads are live-only on both transports.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3ListSigningKeys" method="get" path="/api/ledger/v3/_/signing-keys" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.list_signing_keys(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.V3ListSigningKeysRequest](../../models/operations/v3listsigningkeysrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.V3ListSigningKeysSecurity](../../models/operations/v3listsigningkeyssecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.V3ListSigningKeysResponse](../../models/operations/v3listsigningkeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## livez

Returns 200 as long as the process is alive. Suitable for Kubernetes liveness probes.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3Livez" method="get" path="/api/ledger/livez" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.livez()

    assert res.health_response is not None

    # Handle response
    print(res.health_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `security`                                                               | [operations.V3LivezSecurity](../../models/operations/v3livezsecurity.md) | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.V3LivezResponse](../../models/operations/v3livezresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## promote_ledger

Promotes a mirror-mode ledger to normal mode. After promotion, the mirror sync
worker is stopped and the ledger accepts direct write operations. Requires `ledger:write` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3PromoteLedger" method="post" path="/api/ledger/v3/{ledgerName}/promote" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.promote_ledger(request={
        "ledger_name": "<value>",
    })

    assert res.promote_ledger_response is not None

    # Handle response
    print(res.promote_ledger_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V3PromoteLedgerRequest](../../models/operations/v3promoteledgerrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.V3PromoteLedgerSecurity](../../models/operations/v3promoteledgersecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V3PromoteLedgerResponse](../../models/operations/v3promoteledgerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## readyz

Returns 200 once the local Raft loop has started, regardless of whether
a leader has been elected. Suitable for Kubernetes readiness probes and
StatefulSet `OrderedReady` ordering: it is intentionally permissive so
peer pods can be brought up during a cold start where quorum cannot
form until they exist. Use `/clusterz` for the stricter
cluster-availability signal.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3Readyz" method="get" path="/api/ledger/readyz" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.readyz()

    assert res.health_response is not None

    # Handle response
    print(res.health_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [operations.V3ReadyzSecurity](../../models/operations/v3readyzsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.V3ReadyzResponse](../../models/operations/v3readyzresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_account_type

Removes an account type from a ledger's chart of accounts. Requires `ledger:WriteMetadata` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3RemoveAccountType" method="delete" path="/api/ledger/v3/{ledgerName}/account-types/{typeName}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.remove_account_type(request={
        "ledger_name": "<value>",
        "type_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3RemoveAccountTypeRequest](../../models/operations/v3removeaccounttyperequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.V3RemoveAccountTypeSecurity](../../models/operations/v3removeaccounttypesecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3RemoveAccountTypeResponse](../../models/operations/v3removeaccounttyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_events_sink

Removes a named event sink from the cluster. Requires `ledger:WriteOps`
scope. A non-empty controllerId must match the sink's controllerId;
a mismatch returns `SINK_CONTROLLER_MISMATCH` (409). An omitted or empty
controllerId removes the sink without an ownership precondition.
A missing sink returns `SINK_NOT_FOUND` (404). Malformed query encoding
or repeated controllerId parameters return `INVALID_REQUEST` (400)
before Apply, instead of becoming unconditional removal.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3RemoveEventsSink" method="delete" path="/api/ledger/v3/_/events-sinks/{sinkName}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.remove_events_sink(request={
        "sink_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.V3RemoveEventsSinkRequest](../../models/operations/v3removeeventssinkrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.V3RemoveEventsSinkSecurity](../../models/operations/v3removeeventssinksecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.V3RemoveEventsSinkResponse](../../models/operations/v3removeeventssinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_metadata_field_type

Removes the type declaration for a metadata key on a ledger.
Existing metadata values remain unchanged and any attached index is dropped. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).


### Example Usage

<!-- UsageSnippet language="python" operationID="v3RemoveMetadataFieldType" method="delete" path="/api/ledger/v3/{ledgerName}/metadata-schema/{targetType}/{key}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3


with SDK() as sdk:

    res = sdk.ledger.v3.remove_metadata_field_type(request={
        "key": "formance.com/reviewed",
        "ledger_name": "<value>",
        "target_type": ledger_v3.TargetTypeParameter.LEDGER,
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V3RemoveMetadataFieldTypeRequest](../../models/operations/v3removemetadatafieldtyperequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.V3RemoveMetadataFieldTypeSecurity](../../models/operations/v3removemetadatafieldtypesecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.V3RemoveMetadataFieldTypeResponse](../../models/operations/v3removemetadatafieldtyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## revert_transaction

Reverts a transaction by creating a reverse transaction that undoes its effects. Requires `ledger:write` scope.
The body is optional; an absent or empty body uses default options. Supplied
options and metadata are decoded for both known-length and HTTP/1.1 chunked
requests. Malformed or truncated JSON, extra values, trailing non-whitespace
and options of the wrong JSON type (for example `"atEffectiveDate": "true"`
or a non-object `metadata`) return 400 before applying the revert. A JSON
`null` option uses its default. The complete body, including trailing
whitespace, counts towards the 4 MiB limit; exceeding it returns 413.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3RevertTransaction" method="post" path="/api/ledger/v3/{ledgerName}/transactions/{transactionId}/revert" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.revert_transaction(request={
        "formance_bigint_as_string": "true",
        "ledger_name": "<value>",
        "transaction_id": 541831,
    })

    assert res.reverted_transaction_response is not None

    # Handle response
    print(res.reverted_transaction_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.V3RevertTransactionRequest](../../models/operations/v3reverttransactionrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.V3RevertTransactionSecurity](../../models/operations/v3reverttransactionsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.V3RevertTransactionResponse](../../models/operations/v3reverttransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## save_account_metadata

Saves metadata for a specific account in the ledger. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3SaveAccountMetadata" method="post" path="/api/ledger/v3/{ledgerName}/accounts/{address}/metadata" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.save_account_metadata(request={
        "request_body": {
            "account_type": "asset",
            "label": "Bank Account",
            "active": True,
            "balance_threshold": 1000,
        },
        "address": "users:001",
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3SaveAccountMetadataRequest](../../models/operations/v3saveaccountmetadatarequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3SaveAccountMetadataSecurity](../../models/operations/v3saveaccountmetadatasecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3SaveAccountMetadataResponse](../../models/operations/v3saveaccountmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## save_ledger_metadata

Saves metadata key-value pairs on the ledger itself. Requires `ledger:WriteMetadata`; `ledger:write` grants it under the default scope mapping. Custom scope mappings can differ.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3SaveLedgerMetadata" method="post" path="/api/ledger/v3/{ledgerName}/metadata" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.save_ledger_metadata(request={
        "request_body": {
            "environment": "production",
            "team": "payments",
            "region": "eu-west-1",
        },
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.V3SaveLedgerMetadataRequest](../../models/operations/v3saveledgermetadatarequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.V3SaveLedgerMetadataSecurity](../../models/operations/v3saveledgermetadatasecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.V3SaveLedgerMetadataResponse](../../models/operations/v3saveledgermetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## save_numscript

Appends an immutable version to a ledger's numscript library. The `version`
field must be an explicit full semver (e.g. "1.0.0"); it creates a new
version and fails if that version already exists. The per-name latest is
always the greatest stored semver.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3SaveNumscript" method="put" path="/api/ledger/v3/{ledgerName}/numscripts/{name}" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.save_numscript(request={
        "save_numscript_request": {
            "content": "<value>",
            "version": "1.0.0",
        },
        "ledger_name": "<value>",
        "name": "<value>",
    })

    assert res.get_numscript_response is not None

    # Handle response
    print(res.get_numscript_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.V3SaveNumscriptRequest](../../models/operations/v3savenumscriptrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.V3SaveNumscriptSecurity](../../models/operations/v3savenumscriptsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.V3SaveNumscriptResponse](../../models/operations/v3savenumscriptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## save_transaction_metadata

Saves metadata for a specific transaction in the ledger. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3SaveTransactionMetadata" method="post" path="/api/ledger/v3/{ledgerName}/transactions/{transactionId}/metadata" -->
```python
from formance_sdk_python import SDK


with SDK() as sdk:

    res = sdk.ledger.v3.save_transaction_metadata(request={
        "request_body": {
            "reason": "correction",
            "source": "support",
            "priority": 1,
        },
        "ledger_name": "<value>",
        "transaction_id": 736514,
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.V3SaveTransactionMetadataRequest](../../models/operations/v3savetransactionmetadatarequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.V3SaveTransactionMetadataSecurity](../../models/operations/v3savetransactionmetadatasecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.V3SaveTransactionMetadataResponse](../../models/operations/v3savetransactionmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set_default_enforcement_mode

Sets the default enforcement mode for accounts that do not match any defined
account type. Must be STRICT or AUDIT. STRICT rejects an order that uses an
unmatched account with `400 ACCOUNT_NOT_MATCHING_TYPE`. AUDIT accepts the
order and does not report the unmatched account: the response carries no
warning. Requires `ledger:WriteMetadata` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3SetDefaultEnforcementMode" method="put" path="/api/ledger/v3/{ledgerName}/account-types/default-enforcement-mode" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3


with SDK() as sdk:

    res = sdk.ledger.v3.set_default_enforcement_mode(request={
        "set_default_enforcement_mode_request": {
            "enforcement_mode": ledger_v3.EnforcementMode.AUDIT,
        },
        "ledger_name": "<value>",
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.V3SetDefaultEnforcementModeRequest](../../models/operations/v3setdefaultenforcementmoderequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.V3SetDefaultEnforcementModeSecurity](../../models/operations/v3setdefaultenforcementmodesecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.V3SetDefaultEnforcementModeResponse](../../models/operations/v3setdefaultenforcementmoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set_metadata_field_type

Declares or changes the type used to encode a metadata key in an attached query index.
Metadata values are neither validated nor converted by this declaration, and existing primary values remain unchanged.
Any attached index is rewritten asynchronously. Requires `ledger:WriteMetadata` scope (included in the default `ledger:write` mapping).


### Example Usage

<!-- UsageSnippet language="python" operationID="v3SetMetadataFieldType" method="put" path="/api/ledger/v3/{ledgerName}/metadata-schema/{targetType}/{key}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3


with SDK() as sdk:

    res = sdk.ledger.v3.set_metadata_field_type(request={
        "set_metadata_type_request": {
            "type": ledger_v3.SetMetadataTypeRequestType.BOOL,
        },
        "key": "formance.com/reviewed",
        "ledger_name": "<value>",
        "target_type": ledger_v3.TargetTypeParameter.LEDGER,
    })

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.V3SetMetadataFieldTypeRequest](../../models/operations/v3setmetadatafieldtyperequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.V3SetMetadataFieldTypeSecurity](../../models/operations/v3setmetadatafieldtypesecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.V3SetMetadataFieldTypeResponse](../../models/operations/v3setmetadatafieldtyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_prepared_query

Updates the filter of an existing prepared query. Requires `ledger:WriteQuery` scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="v3UpdatePreparedQuery" method="put" path="/api/ledger/v3/{ledgerName}/prepared-queries/{queryName}" -->
```python
from formance_sdk_python import SDK
from formance_sdk_python.models import ledger_v3, operations


with SDK() as sdk:

    res = sdk.ledger.v3.update_prepared_query(request=operations.V3UpdatePreparedQueryRequest(
        update_prepared_query_request=ledger_v3.UpdatePreparedQueryRequest(),
        ledger_name="<value>",
        query_name="<value>",
    ))

    assert res.error_response is not None

    # Handle response
    print(res.error_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.V3UpdatePreparedQueryRequest](../../models/operations/v3updatepreparedqueryrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.V3UpdatePreparedQuerySecurity](../../models/operations/v3updatepreparedquerysecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.V3UpdatePreparedQueryResponse](../../models/operations/v3updatepreparedqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |