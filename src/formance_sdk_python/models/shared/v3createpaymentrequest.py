"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3createpaymentadjustmentrequest import (
    V3CreatePaymentAdjustmentRequest,
    V3CreatePaymentAdjustmentRequestTypedDict,
)
from .v3paymenttypeenum import V3PaymentTypeEnum
from datetime import datetime
from formance_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from formance_sdk_python.utils import validate_int
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import BeforeValidator
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3CreatePaymentRequestTypedDict(TypedDict):
    amount: int
    asset: str
    connector_id: str
    created_at: datetime
    initial_amount: int
    reference: str
    scheme: str
    type: V3PaymentTypeEnum
    adjustments: NotRequired[List[V3CreatePaymentAdjustmentRequestTypedDict]]
    destination_account_id: NotRequired[str]
    metadata: NotRequired[Nullable[Dict[str, str]]]
    source_account_id: NotRequired[str]


class V3CreatePaymentRequest(BaseModel):
    amount: Annotated[int, BeforeValidator(validate_int)]

    asset: str

    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    initial_amount: Annotated[
        Annotated[int, BeforeValidator(validate_int)],
        pydantic.Field(alias="initialAmount"),
    ]

    reference: str

    scheme: str

    type: V3PaymentTypeEnum

    adjustments: Optional[List[V3CreatePaymentAdjustmentRequest]] = None

    destination_account_id: Annotated[
        Optional[str], pydantic.Field(alias="destinationAccountID")
    ] = None

    metadata: OptionalNullable[Dict[str, str]] = UNSET

    source_account_id: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountID")
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "adjustments",
            "destinationAccountID",
            "metadata",
            "sourceAccountID",
        ]
        nullable_fields = ["metadata"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
