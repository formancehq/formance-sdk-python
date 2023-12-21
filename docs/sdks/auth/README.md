# Auth
(*auth*)

### Available Operations

* [create_client](#create_client) - Create client
* [create_secret](#create_secret) - Add a secret to a client
* [delete_client](#delete_client) - Delete client
* [delete_secret](#delete_secret) - Delete a secret from a client
* [get_server_info](#get_server_info) - Get server info
* [list_clients](#list_clients) - List clients
* [list_users](#list_users) - List users
* [read_client](#read_client) - Read client
* [read_user](#read_user) - Read user
* [update_client](#update_client) - Update client

## create_client

Create client

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK()

req = shared.CreateClientRequest(
    metadata={
        "key": 'string',
    },
    name='string',
    post_logout_redirect_uris=[
        'string',
    ],
    redirect_uris=[
        'string',
    ],
    scopes=[
        'string',
    ],
)

res = s.auth.create_client(req)

if res.create_client_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.CreateClientRequest](../../models/shared/createclientrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateClientResponse](../../models/operations/createclientresponse.md)**


## create_secret

Add a secret to a client

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.CreateSecretRequest(
    create_secret_request=shared.CreateSecretRequest(
        metadata={
            "key": 'string',
        },
        name='string',
    ),
    client_id='string',
)

res = s.auth.create_secret(req)

if res.create_secret_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateSecretRequest](../../models/operations/createsecretrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateSecretResponse](../../models/operations/createsecretresponse.md)**


## delete_client

Delete client

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.DeleteClientRequest(
    client_id='string',
)

res = s.auth.delete_client(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteClientRequest](../../models/operations/deleteclientrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteClientResponse](../../models/operations/deleteclientresponse.md)**


## delete_secret

Delete a secret from a client

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.DeleteSecretRequest(
    client_id='string',
    secret_id='string',
)

res = s.auth.delete_secret(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSecretRequest](../../models/operations/deletesecretrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSecretResponse](../../models/operations/deletesecretresponse.md)**


## get_server_info

Get server info

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.auth.get_server_info()

if res.server_info is not None:
    # handle response
    pass
```


### Response

**[operations.GetServerInfoResponse](../../models/operations/getserverinforesponse.md)**


## list_clients

List clients

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.auth.list_clients()

if res.list_clients_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListClientsResponse](../../models/operations/listclientsresponse.md)**


## list_users

List users

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.auth.list_users()

if res.list_users_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**


## read_client

Read client

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.ReadClientRequest(
    client_id='string',
)

res = s.auth.read_client(req)

if res.read_client_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ReadClientRequest](../../models/operations/readclientrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ReadClientResponse](../../models/operations/readclientresponse.md)**


## read_user

Read user

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.ReadUserRequest(
    user_id='string',
)

res = s.auth.read_user(req)

if res.read_user_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ReadUserRequest](../../models/operations/readuserrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ReadUserResponse](../../models/operations/readuserresponse.md)**


## update_client

Update client

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.UpdateClientRequest(
    update_client_request=shared.UpdateClientRequest(
        metadata={
            "key": 'string',
        },
        name='string',
        post_logout_redirect_uris=[
            'string',
        ],
        redirect_uris=[
            'string',
        ],
        scopes=[
            'string',
        ],
    ),
    client_id='string',
)

res = s.auth.update_client(req)

if res.update_client_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateClientRequest](../../models/operations/updateclientrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateClientResponse](../../models/operations/updateclientresponse.md)**

