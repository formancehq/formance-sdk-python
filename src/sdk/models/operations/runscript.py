"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import script as shared_script
from ...models.shared import scriptresponse as shared_scriptresponse
from typing import Optional


@dataclasses.dataclass
class RunScriptRequest:
    script: shared_script.Script = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    preview: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'preview', 'style': 'form', 'explode': True }})
    r"""Set the preview mode. Preview mode doesn't add the logs to the database or publish a message to the message broker."""
    



@dataclasses.dataclass
class RunScriptResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    script_response: Optional[shared_scriptresponse.ScriptResponse] = dataclasses.field(default=None)
    r"""On success, it will return a 200 status code, and the resulting transaction under the `transaction` field.

    On failure, it will also return a 200 status code, and the following fields:
      - `details`: contains a URL. When there is an error parsing Numscript, the result can be difficult to read—the provided URL will render the error in an easy-to-read format.
      - `errorCode` and `error_code` (deprecated): contains the string code of the error
      - `errorMessage` and `error_message` (deprecated): contains a human-readable indication of what went wrong, for example that an account had insufficient funds, or that there was an error in the provided Numscript.
    """
    

