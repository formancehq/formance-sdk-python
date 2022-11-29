# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v0.2.2
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from Formance.paths.api_auth_users.get import ListUsers
from Formance.paths.api_auth_users_user_id.get import ReadUser


class UsersApi(
    ListUsers,
    ReadUser,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
