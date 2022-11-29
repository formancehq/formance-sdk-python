# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_auth_scopes_scope_id_transient_transient_scope_id.put import AddTransientScope
from Formance.paths.api_auth_scopes.post import CreateScope
from Formance.paths.api_auth_scopes_scope_id.delete import DeleteScope
from Formance.paths.api_auth_scopes_scope_id_transient_transient_scope_id.delete import DeleteTransientScope
from Formance.paths.api_auth_scopes.get import ListScopes
from Formance.paths.api_auth_scopes_scope_id.get import ReadScope
from Formance.paths.api_auth_scopes_scope_id.put import UpdateScope


class ScopesApi(
    AddTransientScope,
    CreateScope,
    DeleteScope,
    DeleteTransientScope,
    ListScopes,
    ReadScope,
    UpdateScope,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
