"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from formance_sdk_python.sdk_v1 import SDKV1
from formance_sdk_python.v2 import V2


class Ledger(BaseSDK):
    v2: V2
    v1: SDKV1

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.v2 = V2(self.sdk_configuration)
        self.v1 = SDKV1(self.sdk_configuration)
