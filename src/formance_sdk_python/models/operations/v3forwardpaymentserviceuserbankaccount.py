"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    v3forwardpaymentserviceuserbankaccountrequest as shared_v3forwardpaymentserviceuserbankaccountrequest,
    v3forwardpaymentserviceuserbankaccountresponse as shared_v3forwardpaymentserviceuserbankaccountresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3ForwardPaymentServiceUserBankAccountRequestTypedDict(TypedDict):
    bank_account_id: str
    r"""The bank account ID"""
    payment_service_user_id: str
    r"""The payment service user ID"""
    v3_forward_payment_service_user_bank_account_request: NotRequired[
        shared_v3forwardpaymentserviceuserbankaccountrequest.V3ForwardPaymentServiceUserBankAccountRequestTypedDict
    ]


class V3ForwardPaymentServiceUserBankAccountRequest(BaseModel):
    bank_account_id: Annotated[
        str,
        pydantic.Field(alias="bankAccountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The bank account ID"""

    payment_service_user_id: Annotated[
        str,
        pydantic.Field(alias="paymentServiceUserID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The payment service user ID"""

    v3_forward_payment_service_user_bank_account_request: Annotated[
        Optional[
            shared_v3forwardpaymentserviceuserbankaccountrequest.V3ForwardPaymentServiceUserBankAccountRequest
        ],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class V3ForwardPaymentServiceUserBankAccountResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v3_forward_payment_service_user_bank_account_response: NotRequired[
        shared_v3forwardpaymentserviceuserbankaccountresponse.V3ForwardPaymentServiceUserBankAccountResponseTypedDict
    ]
    r"""Accepted"""


class V3ForwardPaymentServiceUserBankAccountResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v3_forward_payment_service_user_bank_account_response: Optional[
        shared_v3forwardpaymentserviceuserbankaccountresponse.V3ForwardPaymentServiceUserBankAccountResponse
    ] = None
    r"""Accepted"""
