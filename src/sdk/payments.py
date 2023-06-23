"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from sdk import utils
from sdk.models import operations, shared
from typing import Optional

class Payments:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def connectors_stripe_transfer(self, request: shared.StripeTransferRequest) -> operations.ConnectorsStripeTransferResponse:
        r"""Transfer funds between Stripe accounts
        Execute a transfer between two Stripe accounts.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/payments/connectors/stripe/transfers'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConnectorsStripeTransferResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.StripeTransferResponse])
                res.stripe_transfer_response = out

        return res

    
    def connectors_transfer(self, request: operations.ConnectorsTransferRequest) -> operations.ConnectorsTransferResponse:
        r"""Transfer funds between Connector accounts
        Execute a transfer between two accounts.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ConnectorsTransferRequest, base_url, '/api/payments/connectors/{connector}/transfers', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "transfer_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConnectorsTransferResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TransferResponse])
                res.transfer_response = out

        return res

    
    def get_connector_task(self, request: operations.GetConnectorTaskRequest) -> operations.GetConnectorTaskResponse:
        r"""Read a specific task of the connector
        Get a specific task associated to the connector.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetConnectorTaskRequest, base_url, '/api/payments/connectors/{connector}/tasks/{taskId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetConnectorTaskResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TaskResponse])
                res.task_response = out

        return res

    
    def get_payment(self, request: operations.GetPaymentRequest) -> operations.GetPaymentResponse:
        r"""Get a payment"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetPaymentRequest, base_url, '/api/payments/payments/{paymentId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPaymentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PaymentResponse])
                res.payment_response = out

        return res

    
    def install_connector(self, request: operations.InstallConnectorRequest) -> operations.InstallConnectorResponse:
        r"""Install a connector
        Install a connector by its name and config.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.InstallConnectorRequest, base_url, '/api/payments/connectors/{connector}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InstallConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def list_all_connectors(self) -> operations.ListAllConnectorsResponse:
        r"""List all installed connectors
        List all installed connectors.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/payments/connectors'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllConnectorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectorsResponse])
                res.connectors_response = out

        return res

    
    def list_configs_available_connectors(self) -> operations.ListConfigsAvailableConnectorsResponse:
        r"""List the configs of each available connector
        List the configs of each available connector.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/payments/connectors/configs'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListConfigsAvailableConnectorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectorsConfigsResponse])
                res.connectors_configs_response = out

        return res

    
    def list_connector_tasks(self, request: operations.ListConnectorTasksRequest) -> operations.ListConnectorTasksResponse:
        r"""List tasks from a connector
        List all tasks associated with this connector.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListConnectorTasksRequest, base_url, '/api/payments/connectors/{connector}/tasks', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListConnectorTasksRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListConnectorTasksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TasksCursor])
                res.tasks_cursor = out

        return res

    
    def list_connectors_transfers(self, request: operations.ListConnectorsTransfersRequest) -> operations.ListConnectorsTransfersResponse:
        r"""List transfers and their statuses
        List transfers
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListConnectorsTransfersRequest, base_url, '/api/payments/connectors/{connector}/transfers', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListConnectorsTransfersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TransfersResponse])
                res.transfers_response = out

        return res

    
    def list_payments(self, request: operations.ListPaymentsRequest) -> operations.ListPaymentsResponse:
        r"""List payments"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/payments/payments'
        headers = {}
        query_params = utils.get_query_params(operations.ListPaymentsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListPaymentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PaymentsCursor])
                res.payments_cursor = out

        return res

    
    def paymentsget_server_info(self) -> operations.PaymentsgetServerInfoResponse:
        r"""Get server info"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/payments/_info'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PaymentsgetServerInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerInfo])
                res.server_info = out

        return res

    
    def paymentslist_accounts(self, request: operations.PaymentslistAccountsRequest) -> operations.PaymentslistAccountsResponse:
        r"""List accounts"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/payments/accounts'
        headers = {}
        query_params = utils.get_query_params(operations.PaymentslistAccountsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PaymentslistAccountsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountsCursor])
                res.accounts_cursor = out

        return res

    
    def read_connector_config(self, request: operations.ReadConnectorConfigRequest) -> operations.ReadConnectorConfigResponse:
        r"""Read the config of a connector
        Read connector config
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ReadConnectorConfigRequest, base_url, '/api/payments/connectors/{connector}/config', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReadConnectorConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectorConfigResponse])
                res.connector_config_response = out

        return res

    
    def reset_connector(self, request: operations.ResetConnectorRequest) -> operations.ResetConnectorResponse:
        r"""Reset a connector
        Reset a connector by its name.
        It will remove the connector and ALL PAYMENTS generated with it.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ResetConnectorRequest, base_url, '/api/payments/connectors/{connector}/reset', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ResetConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def uninstall_connector(self, request: operations.UninstallConnectorRequest) -> operations.UninstallConnectorResponse:
        r"""Uninstall a connector
        Uninstall a connector by its name.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UninstallConnectorRequest, base_url, '/api/payments/connectors/{connector}', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UninstallConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def update_metadata(self, request: operations.UpdateMetadataRequest) -> operations.UpdateMetadataResponse:
        r"""Update metadata"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateMetadataRequest, base_url, '/api/payments/payments/{paymentId}/metadata', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "payment_metadata", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    