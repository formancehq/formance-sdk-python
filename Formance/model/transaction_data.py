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


class TransactionData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "postings",
        }
        
        class properties:
            
            
            class postings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Posting']:
                        return Posting
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Posting'], typing.List['Posting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Posting':
                    return super().__getitem__(i)
            timestamp = schemas.DateTimeSchema
            reference = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['LedgerMetadata']:
                return LedgerMetadata
            __annotations__ = {
                "postings": postings,
                "timestamp": timestamp,
                "reference": reference,
                "metadata": metadata,
            }
    
    postings: MetaOapg.properties.postings
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'LedgerMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["postings", "timestamp", "reference", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['LedgerMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["postings", "timestamp", "reference", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        postings: typing.Union[MetaOapg.properties.postings, list, tuple, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, schemas.Unset] = schemas.unset,
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['LedgerMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionData':
        return super().__new__(
            cls,
            *_args,
            postings=postings,
            timestamp=timestamp,
            reference=reference,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from Formance.model.ledger_metadata import LedgerMetadata
from Formance.model.posting import Posting
