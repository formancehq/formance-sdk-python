# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v0.2.2
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


class Payment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date",
            "amount",
            "scheme",
            "provider",
            "id",
            "asset",
            "type",
            "status",
        }
        
        class properties:
            provider = schemas.StrSchema
            
            
            class scheme(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "visa": "VISA",
                        "mastercard": "MASTERCARD",
                        "apple pay": "APPLE_PAY",
                        "google pay": "GOOGLE_PAY",
                        "sepa debit": "SEPA_DEBIT",
                        "sepa credit": "SEPA_CREDIT",
                        "sepa": "SEPA",
                        "a2a": "A2A",
                        "ach debit": "ACH_DEBIT",
                        "ach": "ACH",
                        "rtp": "RTP",
                        "other": "OTHER",
                    }
                
                @schemas.classproperty
                def VISA(cls):
                    return cls("visa")
                
                @schemas.classproperty
                def MASTERCARD(cls):
                    return cls("mastercard")
                
                @schemas.classproperty
                def APPLE_PAY(cls):
                    return cls("apple pay")
                
                @schemas.classproperty
                def GOOGLE_PAY(cls):
                    return cls("google pay")
                
                @schemas.classproperty
                def SEPA_DEBIT(cls):
                    return cls("sepa debit")
                
                @schemas.classproperty
                def SEPA_CREDIT(cls):
                    return cls("sepa credit")
                
                @schemas.classproperty
                def SEPA(cls):
                    return cls("sepa")
                
                @schemas.classproperty
                def A2A(cls):
                    return cls("a2a")
                
                @schemas.classproperty
                def ACH_DEBIT(cls):
                    return cls("ach debit")
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ach")
                
                @schemas.classproperty
                def RTP(cls):
                    return cls("rtp")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
            status = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pay-in": "PAYIN",
                        "payout": "PAYOUT",
                        "other": "OTHER",
                    }
                
                @schemas.classproperty
                def PAYIN(cls):
                    return cls("pay-in")
                
                @schemas.classproperty
                def PAYOUT(cls):
                    return cls("payout")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
            id = schemas.StrSchema
            amount = schemas.IntSchema
            asset = schemas.StrSchema
            date = schemas.DateTimeSchema
            reference = schemas.StrSchema
            raw = schemas.AnyTypeSchema
            __annotations__ = {
                "provider": provider,
                "scheme": scheme,
                "status": status,
                "type": type,
                "id": id,
                "amount": amount,
                "asset": asset,
                "date": date,
                "reference": reference,
                "raw": raw,
            }
    
    date: MetaOapg.properties.date
    amount: MetaOapg.properties.amount
    scheme: MetaOapg.properties.scheme
    provider: MetaOapg.properties.provider
    id: MetaOapg.properties.id
    asset: MetaOapg.properties.asset
    type: MetaOapg.properties.type
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheme"]) -> MetaOapg.properties.scheme: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset"]) -> MetaOapg.properties.asset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw"]) -> MetaOapg.properties.raw: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["provider", "scheme", "status", "type", "id", "amount", "asset", "date", "reference", "raw", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheme"]) -> MetaOapg.properties.scheme: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset"]) -> MetaOapg.properties.asset: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw"]) -> typing.Union[MetaOapg.properties.raw, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["provider", "scheme", "status", "type", "id", "amount", "asset", "date", "reference", "raw", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, datetime, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        scheme: typing.Union[MetaOapg.properties.scheme, str, ],
        provider: typing.Union[MetaOapg.properties.provider, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        asset: typing.Union[MetaOapg.properties.asset, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        raw: typing.Union[MetaOapg.properties.raw, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Payment':
        return super().__new__(
            cls,
            *_args,
            date=date,
            amount=amount,
            scheme=scheme,
            provider=provider,
            id=id,
            asset=asset,
            type=type,
            status=status,
            reference=reference,
            raw=raw,
            _configuration=_configuration,
            **kwargs,
        )
