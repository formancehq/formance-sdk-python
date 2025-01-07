"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    runworkflowresponse as shared_runworkflowresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import httpx
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RunWorkflowRequestTypedDict(TypedDict):
    workflow_id: str
    r"""The flow id"""
    request_body: NotRequired[Dict[str, str]]
    wait: NotRequired[bool]
    r"""Wait end of the workflow before return"""


class RunWorkflowRequest(BaseModel):
    workflow_id: Annotated[
        str,
        pydantic.Field(alias="workflowID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The flow id"""

    request_body: Annotated[
        Optional[Dict[str, str]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    wait: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Wait end of the workflow before return"""


class RunWorkflowResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    run_workflow_response: NotRequired[
        shared_runworkflowresponse.RunWorkflowResponseTypedDict
    ]
    r"""The workflow instance"""


class RunWorkflowResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    run_workflow_response: Optional[shared_runworkflowresponse.RunWorkflowResponse] = (
        None
    )
    r"""The workflow instance"""