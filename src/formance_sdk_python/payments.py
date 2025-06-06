"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from formance_sdk_python.payments_v1 import PaymentsV1
from formance_sdk_python.v3 import V3


class Payments(BaseSDK):
    v1: PaymentsV1
    v3: V3

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.v1 = PaymentsV1(self.sdk_configuration)
        self.v3 = V3(self.sdk_configuration)
