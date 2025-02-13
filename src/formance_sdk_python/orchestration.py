"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from formance_sdk_python.sdk_orchestration_v1 import SDKOrchestrationV1
from formance_sdk_python.sdk_v2 import SDKV2


class Orchestration(BaseSDK):
    v1: SDKOrchestrationV1
    v2: SDKV2

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.v1 = SDKOrchestrationV1(self.sdk_configuration)
        self.v2 = SDKV2(self.sdk_configuration)
