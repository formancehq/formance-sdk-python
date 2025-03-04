"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2bulkelementaddmetadata import (
    V2BulkElementAddMetadata,
    V2BulkElementAddMetadataTypedDict,
)
from .v2bulkelementcreatetransaction import (
    V2BulkElementCreateTransaction,
    V2BulkElementCreateTransactionTypedDict,
)
from .v2bulkelementdeletemetadata import (
    V2BulkElementDeleteMetadata,
    V2BulkElementDeleteMetadataTypedDict,
)
from .v2bulkelementreverttransaction import (
    V2BulkElementRevertTransaction,
    V2BulkElementRevertTransactionTypedDict,
)
from formance_sdk_python.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType


V2BulkElementTypedDict = TypeAliasType(
    "V2BulkElementTypedDict",
    Union[
        V2BulkElementCreateTransactionTypedDict,
        V2BulkElementAddMetadataTypedDict,
        V2BulkElementRevertTransactionTypedDict,
        V2BulkElementDeleteMetadataTypedDict,
    ],
)


V2BulkElement = Annotated[
    Union[
        Annotated[V2BulkElementAddMetadata, Tag("ADD_METADATA")],
        Annotated[V2BulkElementCreateTransaction, Tag("CREATE_TRANSACTION")],
        Annotated[V2BulkElementDeleteMetadata, Tag("DELETE_METADATA")],
        Annotated[V2BulkElementRevertTransaction, Tag("REVERT_TRANSACTION")],
    ],
    Discriminator(lambda m: get_discriminator(m, "action", "action")),
]
