# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0-rc.3
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


class ScriptResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            details = schemas.StrSchema
            
            
            class error_code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "INTERNAL": "INTERNAL",
                        "INSUFFICIENT_FUND": "INSUFFICIENT_FUND",
                        "COMPILATION_FAILED": "COMPILATION_FAILED",
                        "NO_SCRIPT": "NO_SCRIPT",
                    }
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("INTERNAL")
                
                @schemas.classproperty
                def INSUFFICIENT_FUND(cls):
                    return cls("INSUFFICIENT_FUND")
                
                @schemas.classproperty
                def COMPILATION_FAILED(cls):
                    return cls("COMPILATION_FAILED")
                
                @schemas.classproperty
                def NO_SCRIPT(cls):
                    return cls("NO_SCRIPT")
            error_message = schemas.StrSchema
        
            @staticmethod
            def transaction() -> typing.Type['Transaction']:
                return Transaction
            __annotations__ = {
                "details": details,
                "error_code": error_code,
                "error_message": error_message,
                "transaction": transaction,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code"]) -> MetaOapg.properties.error_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_message"]) -> MetaOapg.properties.error_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction"]) -> 'Transaction': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["details", "error_code", "error_message", "transaction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code"]) -> typing.Union[MetaOapg.properties.error_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_message"]) -> typing.Union[MetaOapg.properties.error_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction"]) -> typing.Union['Transaction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["details", "error_code", "error_message", "transaction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        details: typing.Union[MetaOapg.properties.details, str, schemas.Unset] = schemas.unset,
        error_code: typing.Union[MetaOapg.properties.error_code, str, schemas.Unset] = schemas.unset,
        error_message: typing.Union[MetaOapg.properties.error_message, str, schemas.Unset] = schemas.unset,
        transaction: typing.Union['Transaction', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScriptResult':
        return super().__new__(
            cls,
            *_args,
            details=details,
            error_code=error_code,
            error_message=error_message,
            transaction=transaction,
            _configuration=_configuration,
            **kwargs,
        )

from Formance.model.transaction import Transaction
