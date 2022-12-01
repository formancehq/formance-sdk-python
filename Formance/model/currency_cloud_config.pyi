# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v0.2.4
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


class CurrencyCloudConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "loginID",
            "apiKey",
        }
        
        class properties:
            apiKey = schemas.StrSchema
            loginID = schemas.StrSchema
            pollingPeriod = schemas.StrSchema
            endpoint = schemas.StrSchema
            __annotations__ = {
                "apiKey": apiKey,
                "loginID": loginID,
                "pollingPeriod": pollingPeriod,
                "endpoint": endpoint,
            }
    
    loginID: MetaOapg.properties.loginID
    apiKey: MetaOapg.properties.apiKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loginID"]) -> MetaOapg.properties.loginID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pollingPeriod"]) -> MetaOapg.properties.pollingPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiKey", "loginID", "pollingPeriod", "endpoint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loginID"]) -> MetaOapg.properties.loginID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pollingPeriod"]) -> typing.Union[MetaOapg.properties.pollingPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> typing.Union[MetaOapg.properties.endpoint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiKey", "loginID", "pollingPeriod", "endpoint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        loginID: typing.Union[MetaOapg.properties.loginID, str, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, ],
        pollingPeriod: typing.Union[MetaOapg.properties.pollingPeriod, str, schemas.Unset] = schemas.unset,
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CurrencyCloudConfig':
        return super().__new__(
            cls,
            *_args,
            loginID=loginID,
            apiKey=apiKey,
            pollingPeriod=pollingPeriod,
            endpoint=endpoint,
            _configuration=_configuration,
            **kwargs,
        )
