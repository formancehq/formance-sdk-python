"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .sdk_orchestration_v1 import SDKOrchestrationV1
from .sdk_v2 import SDKV2
from .sdkconfiguration import SDKConfiguration

class Orchestration:
    v1: SDKOrchestrationV1
    v2: SDKV2
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.v1 = SDKOrchestrationV1(self.sdk_configuration)
        self.v2 = SDKV2(self.sdk_configuration)
        
    

