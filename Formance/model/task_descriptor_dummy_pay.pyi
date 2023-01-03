# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0-rc.4
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


class TaskDescriptorDummyPay(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            provider = schemas.StrSchema
            createdAt = schemas.DateTimeSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STOPPED(cls):
                    return cls("stopped")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def TERMINATED(cls):
                    return cls("terminated")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("failed")
            error = schemas.StrSchema
            state = schemas.DictSchema
            
            
            class descriptor(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        name = schemas.StrSchema
                        key = schemas.StrSchema
                        fileName = schemas.StrSchema
                        __annotations__ = {
                            "name": name,
                            "key": key,
                            "fileName": fileName,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "key", "fileName", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "key", "fileName", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
                    fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'descriptor':
                    return super().__new__(
                        cls,
                        *_args,
                        name=name,
                        key=key,
                        fileName=fileName,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "provider": provider,
                "createdAt": createdAt,
                "status": status,
                "error": error,
                "state": state,
                "descriptor": descriptor,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["provider", "createdAt", "status", "error", "state", "descriptor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["provider", "createdAt", "status", "error", "state", "descriptor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        provider: typing.Union[MetaOapg.properties.provider, str, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        descriptor: typing.Union[MetaOapg.properties.descriptor, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskDescriptorDummyPay':
        return super().__new__(
            cls,
            *_args,
            provider=provider,
            createdAt=createdAt,
            status=status,
            error=error,
            state=state,
            descriptor=descriptor,
            _configuration=_configuration,
            **kwargs,
        )
