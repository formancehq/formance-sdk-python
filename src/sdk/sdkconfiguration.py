"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass, field
from enum import Enum
from sdk.models import shared
from typing import Callable, Dict, List, Optional, Tuple, Union


SERVERS = [
    'http://localhost',
    # local server
    'https://{organization}.{environment}.formance.cloud',
    # A per-organization and per-environment API
]
"""Contains the list of servers available to the SDK"""


class ServerEnvironment(str, Enum):
    r"""The environment name. Defaults to the production environment."""
    SANDBOX = 'sandbox'
    EU_WEST_1 = 'eu-west-1'
    US_EAST_1 = 'us-east-1'


@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: Optional[str] = ''
    server_idx: Optional[int] = 0
    server_defaults: List[Dict[str, str]] = field(default_factory=List)
    language: str = 'python'
    openapi_doc_version: str = 'v2.1.0-beta.3'
    sdk_version: str = '4.1.0'
    gen_version: str = '2.428.1'
    user_agent: str = 'speakeasy-sdk/python 4.1.0 2.428.1 v2.1.0-beta.3 formance-sdk-python'
    retry_config: Optional[RetryConfig] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url != '':
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], self.server_defaults[self.server_idx]


    def get_hooks(self) -> SDKHooks:
        return self._hooks
