# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0-rc.2
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from Formance import schemas  # noqa: F401


class BankingCircleConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "endpoint",
            "password",
            "authorizationEndpoint",
            "username",
        }
        
        class properties:
            username = schemas.StrSchema
            password = schemas.StrSchema
            endpoint = schemas.StrSchema
            authorizationEndpoint = schemas.StrSchema
            __annotations__ = {
                "username": username,
                "password": password,
                "endpoint": endpoint,
                "authorizationEndpoint": authorizationEndpoint,
            }
    
    endpoint: MetaOapg.properties.endpoint
    password: MetaOapg.properties.password
    authorizationEndpoint: MetaOapg.properties.authorizationEndpoint
    username: MetaOapg.properties.username
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorizationEndpoint"]) -> MetaOapg.properties.authorizationEndpoint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["username", "password", "endpoint", "authorizationEndpoint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorizationEndpoint"]) -> MetaOapg.properties.authorizationEndpoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["username", "password", "endpoint", "authorizationEndpoint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        authorizationEndpoint: typing.Union[MetaOapg.properties.authorizationEndpoint, str, ],
        username: typing.Union[MetaOapg.properties.username, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankingCircleConfig':
        return super().__new__(
            cls,
            *_args,
            endpoint=endpoint,
            password=password,
            authorizationEndpoint=authorizationEndpoint,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
