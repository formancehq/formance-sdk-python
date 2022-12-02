# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v0.2.8
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


class StripeConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "apiKey",
        }
        
        class properties:
            apiKey = schemas.StrSchema
            pollingPeriod = schemas.StrSchema
            pageSize = schemas.NumberSchema
            __annotations__ = {
                "apiKey": apiKey,
                "pollingPeriod": pollingPeriod,
                "pageSize": pageSize,
            }
    
    apiKey: MetaOapg.properties.apiKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pollingPeriod"]) -> MetaOapg.properties.pollingPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiKey", "pollingPeriod", "pageSize", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pollingPeriod"]) -> typing.Union[MetaOapg.properties.pollingPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageSize"]) -> typing.Union[MetaOapg.properties.pageSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiKey", "pollingPeriod", "pageSize", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, ],
        pollingPeriod: typing.Union[MetaOapg.properties.pollingPeriod, str, schemas.Unset] = schemas.unset,
        pageSize: typing.Union[MetaOapg.properties.pageSize, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StripeConfig':
        return super().__new__(
            cls,
            *_args,
            apiKey=apiKey,
            pollingPeriod=pollingPeriod,
            pageSize=pageSize,
            _configuration=_configuration,
            **kwargs,
        )
