"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CurrencyCloudConfig:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey') }})
    login_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loginID') }})
    r"""Username of the API Key holder"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""The endpoint to use for the API. Defaults to https://devapi.currencycloud.com"""
    polling_period: Optional[str] = dataclasses.field(default='120s', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pollingPeriod'), 'exclude': lambda f: f is None }})
    r"""The frequency at which the connector will fetch transactions"""
    

