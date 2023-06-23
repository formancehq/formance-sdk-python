"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .auth import Auth
from .ledger import Ledger
from .orchestration import Orchestration
from .payments import Payments
from .sdkconfiguration import SDKConfiguration
from .search import Search
from .wallets import Wallets
from .webhooks import Webhooks
from sdk import utils
from sdk.models import operations, shared
from typing import Optional

class SDK:
    r"""Formance Stack API: Open, modular foundation for unique payments flows
    
    # Introduction
    This API is documented in **OpenAPI format**.
    
    # Authentication
    Formance Stack offers one forms of authentication:
      - OAuth2
    OAuth2 - an open protocol to allow secure authorization in a simple
    and standard method from web, mobile and desktop applications.
    <SecurityDefinitions />
    """
    auth: Auth
    ledger: Ledger
    orchestration: Orchestration
    payments: Payments
    search: Search
    wallets: Wallets
    webhooks: Webhooks

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 organization: str = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param organization: Allows setting the organization variable for url substitution
        :type organization: str
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = utils.configure_security_client(client, security)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults = [
            {
            },
            {
                'organization': organization or '',
            },
        ]

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, server_defaults)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.auth = Auth(self.sdk_configuration)
        self.ledger = Ledger(self.sdk_configuration)
        self.orchestration = Orchestration(self.sdk_configuration)
        self.payments = Payments(self.sdk_configuration)
        self.search = Search(self.sdk_configuration)
        self.wallets = Wallets(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
    
    def get_versions(self) -> operations.GetVersionsResponse:
        r"""Show stack version information"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/versions'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetVersionsResponse])
                res.get_versions_response = out

        return res

    