# coding: utf-8

"""
    Formance Stack API

    Open, modular foundation for unique payments flows  # Introduction This API is documented in **OpenAPI format**.  # Authentication Formance Stack offers one forms of authentication:   - OAuth2 OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. <SecurityDefinitions />   # noqa: E501

    The version of the OpenAPI document: v1.0.0-rc.3
    Contact: support@formance.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from Formance import schemas  # noqa: F401


class Connectors(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "STRIPE": "STRIPE",
            "DUMMY-PAY": "DUMMYPAY",
            "SIE": "SIE",
            "MODULR": "MODULR",
            "CURRENCY-CLOUD": "CURRENCYCLOUD",
            "BANKING-CIRCLE": "BANKINGCIRCLE",
        }
    
    @schemas.classproperty
    def STRIPE(cls):
        return cls("STRIPE")
    
    @schemas.classproperty
    def DUMMYPAY(cls):
        return cls("DUMMY-PAY")
    
    @schemas.classproperty
    def SIE(cls):
        return cls("SIE")
    
    @schemas.classproperty
    def MODULR(cls):
        return cls("MODULR")
    
    @schemas.classproperty
    def CURRENCYCLOUD(cls):
        return cls("CURRENCY-CLOUD")
    
    @schemas.classproperty
    def BANKINGCIRCLE(cls):
        return cls("BANKING-CIRCLE")
