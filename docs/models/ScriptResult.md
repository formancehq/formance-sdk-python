# Formance.model.script_result.ScriptResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**details** | str,  | str,  |  | [optional] 
**error_code** | str,  | str,  |  | [optional] must be one of ["INTERNAL", "INSUFFICIENT_FUND", "COMPILATION_FAILED", "NO_SCRIPT", ] 
**error_message** | str,  | str,  |  | [optional] 
**transaction** | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

