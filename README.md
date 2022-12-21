# Formance
Open, modular foundation for unique payments flows

# Introduction
This API is documented in **OpenAPI format**.

# Authentication
Formance Stack offers one forms of authentication:
  - OAuth2
OAuth2 - an open protocol to allow secure authorization in a simple
and standard method from web, mobile and desktop applications.
<SecurityDefinitions />


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: develop
- Package version: develop
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.formance.com](https://www.formance.com)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/formancehq/formance-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/formancehq/formance-sdk-python.git`)

Then import the package:
```python
import Formance
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import Formance
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import Formance
from pprint import pprint
from Formance.apis.tags import clients_api
from Formance.model.client_options import ClientOptions
from Formance.model.create_client_response import CreateClientResponse
from Formance.model.create_secret_response import CreateSecretResponse
from Formance.model.list_clients_response import ListClientsResponse
from Formance.model.read_client_response import ReadClientResponse
from Formance.model.secret_options import SecretOptions
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Formance.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Authorization
configuration = Formance.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with Formance.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)
    client_id = "clientId_example" # str | Client ID
scope_id = "scopeId_example" # str | Scope ID

    try:
        # Add scope to client
        api_instance.add_scope_to_client(client_idscope_id)
    except Formance.ApiException as e:
        print("Exception when calling ClientsApi->add_scope_to_client: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClientsApi* | [**add_scope_to_client**](docs/apis/tags/ClientsApi.md#add_scope_to_client) | **put** /api/auth/clients/{clientId}/scopes/{scopeId} | Add scope to client
*ClientsApi* | [**create_client**](docs/apis/tags/ClientsApi.md#create_client) | **post** /api/auth/clients | Create client
*ClientsApi* | [**create_secret**](docs/apis/tags/ClientsApi.md#create_secret) | **post** /api/auth/clients/{clientId}/secrets | Add a secret to a client
*ClientsApi* | [**delete_client**](docs/apis/tags/ClientsApi.md#delete_client) | **delete** /api/auth/clients/{clientId} | Delete client
*ClientsApi* | [**delete_scope_from_client**](docs/apis/tags/ClientsApi.md#delete_scope_from_client) | **delete** /api/auth/clients/{clientId}/scopes/{scopeId} | Delete scope from client
*ClientsApi* | [**delete_secret**](docs/apis/tags/ClientsApi.md#delete_secret) | **delete** /api/auth/clients/{clientId}/secrets/{secretId} | Delete a secret from a client
*ClientsApi* | [**list_clients**](docs/apis/tags/ClientsApi.md#list_clients) | **get** /api/auth/clients | List clients
*ClientsApi* | [**read_client**](docs/apis/tags/ClientsApi.md#read_client) | **get** /api/auth/clients/{clientId} | Read client
*ClientsApi* | [**update_client**](docs/apis/tags/ClientsApi.md#update_client) | **put** /api/auth/clients/{clientId} | Update client
*PaymentsApi* | [**connectors_stripe_transfer**](docs/apis/tags/PaymentsApi.md#connectors_stripe_transfer) | **post** /api/payments/connectors/stripe/transfer | Transfer funds between Stripe accounts
*PaymentsApi* | [**get_all_connectors**](docs/apis/tags/PaymentsApi.md#get_all_connectors) | **get** /api/payments/connectors | Get all installed connectors
*PaymentsApi* | [**get_all_connectors_configs**](docs/apis/tags/PaymentsApi.md#get_all_connectors_configs) | **get** /api/payments/connectors/configs | Get all available connectors configs
*PaymentsApi* | [**get_connector_task**](docs/apis/tags/PaymentsApi.md#get_connector_task) | **get** /api/payments/connectors/{connector}/tasks/{taskId} | Read a specific task of the connector
*PaymentsApi* | [**get_payment**](docs/apis/tags/PaymentsApi.md#get_payment) | **get** /api/payments/payments/{paymentId} | Returns a payment.
*PaymentsApi* | [**install_connector**](docs/apis/tags/PaymentsApi.md#install_connector) | **post** /api/payments/connectors/{connector} | Install connector
*PaymentsApi* | [**list_connector_tasks**](docs/apis/tags/PaymentsApi.md#list_connector_tasks) | **get** /api/payments/connectors/{connector}/tasks | List connector tasks
*PaymentsApi* | [**list_payments**](docs/apis/tags/PaymentsApi.md#list_payments) | **get** /api/payments/payments | Returns a list of payments.
*PaymentsApi* | [**read_connector_config**](docs/apis/tags/PaymentsApi.md#read_connector_config) | **get** /api/payments/connectors/{connector}/config | Read connector config
*PaymentsApi* | [**reset_connector**](docs/apis/tags/PaymentsApi.md#reset_connector) | **post** /api/payments/connectors/{connector}/reset | Reset connector
*PaymentsApi* | [**uninstall_connector**](docs/apis/tags/PaymentsApi.md#uninstall_connector) | **delete** /api/payments/connectors/{connector} | Uninstall connector
*ScopesApi* | [**add_transient_scope**](docs/apis/tags/ScopesApi.md#add_transient_scope) | **put** /api/auth/scopes/{scopeId}/transient/{transientScopeId} | Add a transient scope to a scope
*ScopesApi* | [**create_scope**](docs/apis/tags/ScopesApi.md#create_scope) | **post** /api/auth/scopes | Create scope
*ScopesApi* | [**delete_scope**](docs/apis/tags/ScopesApi.md#delete_scope) | **delete** /api/auth/scopes/{scopeId} | Delete scope
*ScopesApi* | [**delete_transient_scope**](docs/apis/tags/ScopesApi.md#delete_transient_scope) | **delete** /api/auth/scopes/{scopeId}/transient/{transientScopeId} | Delete a transient scope from a scope
*ScopesApi* | [**list_scopes**](docs/apis/tags/ScopesApi.md#list_scopes) | **get** /api/auth/scopes | List scopes
*ScopesApi* | [**read_scope**](docs/apis/tags/ScopesApi.md#read_scope) | **get** /api/auth/scopes/{scopeId} | Read scope
*ScopesApi* | [**update_scope**](docs/apis/tags/ScopesApi.md#update_scope) | **put** /api/auth/scopes/{scopeId} | Update scope
*SearchApi* | [**search**](docs/apis/tags/SearchApi.md#search) | **post** /api/search/ | Search
*UsersApi* | [**list_users**](docs/apis/tags/UsersApi.md#list_users) | **get** /api/auth/users | List users
*UsersApi* | [**read_user**](docs/apis/tags/UsersApi.md#read_user) | **get** /api/auth/users/{userId} | Read user
*WebhooksApi* | [**activate_one_config**](docs/apis/tags/WebhooksApi.md#activate_one_config) | **put** /api/webhooks/configs/{id}/activate | Activate one config
*WebhooksApi* | [**change_one_config_secret**](docs/apis/tags/WebhooksApi.md#change_one_config_secret) | **put** /api/webhooks/configs/{id}/secret/change | Change the signing secret of a config
*WebhooksApi* | [**deactivate_one_config**](docs/apis/tags/WebhooksApi.md#deactivate_one_config) | **put** /api/webhooks/configs/{id}/deactivate | Deactivate one config
*WebhooksApi* | [**delete_one_config**](docs/apis/tags/WebhooksApi.md#delete_one_config) | **delete** /api/webhooks/configs/{id} | Delete one config
*WebhooksApi* | [**get_many_configs**](docs/apis/tags/WebhooksApi.md#get_many_configs) | **get** /api/webhooks/configs | Get many configs
*WebhooksApi* | [**insert_one_config**](docs/apis/tags/WebhooksApi.md#insert_one_config) | **post** /api/webhooks/configs | Insert a new config 
*WebhooksApi* | [**test_one_config**](docs/apis/tags/WebhooksApi.md#test_one_config) | **get** /api/webhooks/configs/{id}/test | Test one config
*AccountsApi* | [**add_metadata_to_account**](docs/apis/tags/AccountsApi.md#add_metadata_to_account) | **post** /api/ledger/{ledger}/accounts/{address}/metadata | Add metadata to an account.
*AccountsApi* | [**count_accounts**](docs/apis/tags/AccountsApi.md#count_accounts) | **head** /api/ledger/{ledger}/accounts | Count the accounts from a ledger.
*AccountsApi* | [**get_account**](docs/apis/tags/AccountsApi.md#get_account) | **get** /api/ledger/{ledger}/accounts/{address} | Get account by its address.
*AccountsApi* | [**list_accounts**](docs/apis/tags/AccountsApi.md#list_accounts) | **get** /api/ledger/{ledger}/accounts | List accounts from a ledger.
*BalancesApi* | [**get_balances**](docs/apis/tags/BalancesApi.md#get_balances) | **get** /api/ledger/{ledger}/balances | Get the balances from a ledger&#x27;s account
*BalancesApi* | [**get_balances_aggregated**](docs/apis/tags/BalancesApi.md#get_balances_aggregated) | **get** /api/ledger/{ledger}/aggregate/balances | Get the aggregated balances from selected accounts
*DefaultApi* | [**get_server_info**](docs/apis/tags/DefaultApi.md#get_server_info) | **get** /api/search/_info | Get server info
*MappingApi* | [**get_mapping**](docs/apis/tags/MappingApi.md#get_mapping) | **get** /api/ledger/{ledger}/mapping | Get the mapping of a ledger.
*MappingApi* | [**update_mapping**](docs/apis/tags/MappingApi.md#update_mapping) | **put** /api/ledger/{ledger}/mapping | Update the mapping of a ledger.
*ScriptApi* | [**run_script**](docs/apis/tags/ScriptApi.md#run_script) | **post** /api/ledger/{ledger}/script | Execute a Numscript.
*ServerApi* | [**get_info**](docs/apis/tags/ServerApi.md#get_info) | **get** /api/ledger/_info | Show server information.
*StatsApi* | [**read_stats**](docs/apis/tags/StatsApi.md#read_stats) | **get** /api/ledger/{ledger}/stats | Get Stats
*TransactionsApi* | [**add_metadata_on_transaction**](docs/apis/tags/TransactionsApi.md#add_metadata_on_transaction) | **post** /api/ledger/{ledger}/transactions/{txid}/metadata | Set the metadata of a transaction by its ID.
*TransactionsApi* | [**count_transactions**](docs/apis/tags/TransactionsApi.md#count_transactions) | **head** /api/ledger/{ledger}/transactions | Count the transactions from a ledger.
*TransactionsApi* | [**create_transaction**](docs/apis/tags/TransactionsApi.md#create_transaction) | **post** /api/ledger/{ledger}/transactions | Create a new transaction to a ledger.
*TransactionsApi* | [**create_transactions**](docs/apis/tags/TransactionsApi.md#create_transactions) | **post** /api/ledger/{ledger}/transactions/batch | Create a new batch of transactions to a ledger.
*TransactionsApi* | [**get_transaction**](docs/apis/tags/TransactionsApi.md#get_transaction) | **get** /api/ledger/{ledger}/transactions/{txid} | Get transaction from a ledger by its ID.
*TransactionsApi* | [**list_transactions**](docs/apis/tags/TransactionsApi.md#list_transactions) | **get** /api/ledger/{ledger}/transactions | List transactions from a ledger.
*TransactionsApi* | [**revert_transaction**](docs/apis/tags/TransactionsApi.md#revert_transaction) | **post** /api/ledger/{ledger}/transactions/{txid}/revert | Revert a ledger transaction by its ID.

## Documentation For Models

 - [Account](docs/models/Account.md)
 - [AccountWithVolumesAndBalances](docs/models/AccountWithVolumesAndBalances.md)
 - [AccountsBalances](docs/models/AccountsBalances.md)
 - [AggregatedVolumes](docs/models/AggregatedVolumes.md)
 - [AssetsBalances](docs/models/AssetsBalances.md)
 - [Attempt](docs/models/Attempt.md)
 - [AttemptResponse](docs/models/AttemptResponse.md)
 - [BankingCircleConfig](docs/models/BankingCircleConfig.md)
 - [Client](docs/models/Client.md)
 - [ClientOptions](docs/models/ClientOptions.md)
 - [ClientSecret](docs/models/ClientSecret.md)
 - [Config](docs/models/Config.md)
 - [ConfigInfo](docs/models/ConfigInfo.md)
 - [ConfigInfoResponse](docs/models/ConfigInfoResponse.md)
 - [ConfigResponse](docs/models/ConfigResponse.md)
 - [ConfigUser](docs/models/ConfigUser.md)
 - [ConnectorBaseInfo](docs/models/ConnectorBaseInfo.md)
 - [ConnectorConfig](docs/models/ConnectorConfig.md)
 - [ConnectorTask](docs/models/ConnectorTask.md)
 - [Contract](docs/models/Contract.md)
 - [CreateClientRequest](docs/models/CreateClientRequest.md)
 - [CreateClientResponse](docs/models/CreateClientResponse.md)
 - [CreateScopeRequest](docs/models/CreateScopeRequest.md)
 - [CreateScopeResponse](docs/models/CreateScopeResponse.md)
 - [CreateSecretRequest](docs/models/CreateSecretRequest.md)
 - [CreateSecretResponse](docs/models/CreateSecretResponse.md)
 - [CurrencyCloudConfig](docs/models/CurrencyCloudConfig.md)
 - [Cursor](docs/models/Cursor.md)
 - [DummyPayConfig](docs/models/DummyPayConfig.md)
 - [ErrorCode](docs/models/ErrorCode.md)
 - [ErrorResponse](docs/models/ErrorResponse.md)
 - [GetPaymentResponse](docs/models/GetPaymentResponse.md)
 - [LedgerMetadata](docs/models/LedgerMetadata.md)
 - [LedgerStorage](docs/models/LedgerStorage.md)
 - [ListClientsResponse](docs/models/ListClientsResponse.md)
 - [ListConnectorsConfigsResponse](docs/models/ListConnectorsConfigsResponse.md)
 - [ListConnectorsResponse](docs/models/ListConnectorsResponse.md)
 - [ListPaymentsResponse](docs/models/ListPaymentsResponse.md)
 - [ListScopesResponse](docs/models/ListScopesResponse.md)
 - [ListUsersResponse](docs/models/ListUsersResponse.md)
 - [Mapping](docs/models/Mapping.md)
 - [MappingResponse](docs/models/MappingResponse.md)
 - [Metadata](docs/models/Metadata.md)
 - [ModulrConfig](docs/models/ModulrConfig.md)
 - [Payment](docs/models/Payment.md)
 - [Posting](docs/models/Posting.md)
 - [Query](docs/models/Query.md)
 - [ReadClientResponse](docs/models/ReadClientResponse.md)
 - [ReadScopeResponse](docs/models/ReadScopeResponse.md)
 - [ReadUserResponse](docs/models/ReadUserResponse.md)
 - [Response](docs/models/Response.md)
 - [Scope](docs/models/Scope.md)
 - [ScopeOptions](docs/models/ScopeOptions.md)
 - [Script](docs/models/Script.md)
 - [ScriptResult](docs/models/ScriptResult.md)
 - [Secret](docs/models/Secret.md)
 - [SecretOptions](docs/models/SecretOptions.md)
 - [ServerInfo](docs/models/ServerInfo.md)
 - [Stats](docs/models/Stats.md)
 - [StatsResponse](docs/models/StatsResponse.md)
 - [StripeConfig](docs/models/StripeConfig.md)
 - [StripeTask](docs/models/StripeTask.md)
 - [StripeTransferRequest](docs/models/StripeTransferRequest.md)
 - [Transaction](docs/models/Transaction.md)
 - [TransactionData](docs/models/TransactionData.md)
 - [TransactionResponse](docs/models/TransactionResponse.md)
 - [Transactions](docs/models/Transactions.md)
 - [TransactionsResponse](docs/models/TransactionsResponse.md)
 - [UpdateClientRequest](docs/models/UpdateClientRequest.md)
 - [UpdateClientResponse](docs/models/UpdateClientResponse.md)
 - [UpdateScopeRequest](docs/models/UpdateScopeRequest.md)
 - [UpdateScopeResponse](docs/models/UpdateScopeResponse.md)
 - [User](docs/models/User.md)
 - [Volume](docs/models/Volume.md)
 - [Volumes](docs/models/Volumes.md)
 - [WebhooksConfig](docs/models/WebhooksConfig.md)
 - [WebhooksCursor](docs/models/WebhooksCursor.md)
 - [WiseConfig](docs/models/WiseConfig.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## Authorization

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author

support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com
support@formance.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in Formance.apis and Formance.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from Formance.apis.default_api import DefaultApi`
- `from Formance.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import Formance
from Formance.apis import *
from Formance.models import *
```
