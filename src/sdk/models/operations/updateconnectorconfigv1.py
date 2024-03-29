"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import adyenconfig as shared_adyenconfig
from ...models.shared import atlarconfig as shared_atlarconfig
from ...models.shared import bankingcircleconfig as shared_bankingcircleconfig
from ...models.shared import connector as shared_connector
from ...models.shared import currencycloudconfig as shared_currencycloudconfig
from ...models.shared import dummypayconfig as shared_dummypayconfig
from ...models.shared import mangopayconfig as shared_mangopayconfig
from ...models.shared import modulrconfig as shared_modulrconfig
from ...models.shared import moneycorpconfig as shared_moneycorpconfig
from ...models.shared import stripeconfig as shared_stripeconfig
from ...models.shared import wiseconfig as shared_wiseconfig
from typing import Union


@dataclasses.dataclass
class UpdateConnectorConfigV1Request:
    connector_config: Union[shared_stripeconfig.StripeConfig, shared_dummypayconfig.DummyPayConfig, shared_wiseconfig.WiseConfig, shared_modulrconfig.ModulrConfig, shared_currencycloudconfig.CurrencyCloudConfig, shared_bankingcircleconfig.BankingCircleConfig, shared_mangopayconfig.MangoPayConfig, shared_moneycorpconfig.MoneycorpConfig, shared_atlarconfig.AtlarConfig, shared_adyenconfig.AdyenConfig] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    connector: shared_connector.Connector = dataclasses.field(metadata={'path_param': { 'field_name': 'connector', 'style': 'simple', 'explode': False }})
    r"""The name of the connector."""
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    r"""The connector ID."""
    



@dataclasses.dataclass
class UpdateConnectorConfigV1Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

