"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class V2ErrorsEnum(str, Enum):
    INTERNAL = 'INTERNAL'
    INSUFFICIENT_FUND = 'INSUFFICIENT_FUND'
    VALIDATION = 'VALIDATION'
    CONFLICT = 'CONFLICT'
    COMPILATION_FAILED = 'COMPILATION_FAILED'
    METADATA_OVERRIDE = 'METADATA_OVERRIDE'
    NOT_FOUND = 'NOT_FOUND'
    REVERT_OCCURRING = 'REVERT_OCCURRING'
    ALREADY_REVERT = 'ALREADY_REVERT'
    NO_POSTINGS = 'NO_POSTINGS'