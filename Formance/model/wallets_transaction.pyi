# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: develop
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


class WalletsTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "postings",
            "txid",
            "timestamp",
        }
        
        class properties:
            timestamp = schemas.DateTimeSchema
            
            
            class postings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletsPosting']:
                        return WalletsPosting
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WalletsPosting'], typing.List['WalletsPosting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WalletsPosting':
                    return super().__getitem__(i)
            
            
            class txid(
                schemas.Int64Schema
            ):
                pass
            reference = schemas.StrSchema
            
            
            class metadata(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'metadata':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def preCommitVolumes() -> typing.Type['WalletsAggregatedVolumes']:
                return WalletsAggregatedVolumes
        
            @staticmethod
            def postCommitVolumes() -> typing.Type['WalletsAggregatedVolumes']:
                return WalletsAggregatedVolumes
            __annotations__ = {
                "timestamp": timestamp,
                "postings": postings,
                "txid": txid,
                "reference": reference,
                "metadata": metadata,
                "preCommitVolumes": preCommitVolumes,
                "postCommitVolumes": postCommitVolumes,
            }
    
    postings: MetaOapg.properties.postings
    txid: MetaOapg.properties.txid
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txid"]) -> MetaOapg.properties.txid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preCommitVolumes"]) -> 'WalletsAggregatedVolumes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postCommitVolumes"]) -> 'WalletsAggregatedVolumes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "postings", "txid", "reference", "metadata", "preCommitVolumes", "postCommitVolumes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txid"]) -> MetaOapg.properties.txid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preCommitVolumes"]) -> typing.Union['WalletsAggregatedVolumes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postCommitVolumes"]) -> typing.Union['WalletsAggregatedVolumes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "postings", "txid", "reference", "metadata", "preCommitVolumes", "postCommitVolumes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        postings: typing.Union[MetaOapg.properties.postings, list, tuple, ],
        txid: typing.Union[MetaOapg.properties.txid, decimal.Decimal, int, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        preCommitVolumes: typing.Union['WalletsAggregatedVolumes', schemas.Unset] = schemas.unset,
        postCommitVolumes: typing.Union['WalletsAggregatedVolumes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletsTransaction':
        return super().__new__(
            cls,
            *args,
            postings=postings,
            txid=txid,
            timestamp=timestamp,
            reference=reference,
            metadata=metadata,
            preCommitVolumes=preCommitVolumes,
            postCommitVolumes=postCommitVolumes,
            _configuration=_configuration,
            **kwargs,
        )

from Formance.model.wallets_aggregated_volumes import WalletsAggregatedVolumes
from Formance.model.wallets_posting import WalletsPosting
