"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import paymentresponse as shared_paymentresponse
from typing import Optional


@dataclasses.dataclass
class GetPaymentRequest:
    payment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'paymentId', 'style': 'simple', 'explode': False }})
    r"""The payment ID."""
    



@dataclasses.dataclass
class GetPaymentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    payment_response: Optional[shared_paymentresponse.PaymentResponse] = dataclasses.field(default=None)
    r"""OK"""
    

