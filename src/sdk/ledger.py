"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .sdk_v1 import SDKV1
from .sdkconfiguration import SDKConfiguration
from .v2 import V2

class Ledger:
    v1: SDKV1
    v2: V2
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.v1 = SDKV1(self.sdk_configuration)
        self.v2 = V2(self.sdk_configuration)
        
    

