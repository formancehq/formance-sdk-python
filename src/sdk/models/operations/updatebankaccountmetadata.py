"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import updatebankaccountmetadatarequest as shared_updatebankaccountmetadatarequest


@dataclasses.dataclass
class UpdateBankAccountMetadataRequest:
    update_bank_account_metadata_request: shared_updatebankaccountmetadatarequest.UpdateBankAccountMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    bank_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'bankAccountId', 'style': 'simple', 'explode': False }})
    r"""The bank account ID."""
    



@dataclasses.dataclass
class UpdateBankAccountMetadataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

