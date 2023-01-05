# Formance.model.debit_wallet_request.DebitWalletRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | [**Monetary**](Monetary.md) | [**Monetary**](Monetary.md) |  | 
**pending** | bool,  | BoolClass,  | Set to true to create a pending hold. If false, the wallet will be debited immediately. | [optional] 
**metadata** | [**WalletsMetadata**](WalletsMetadata.md) | [**WalletsMetadata**](WalletsMetadata.md) |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**destination** | [**Subject**](Subject.md) | [**Subject**](Subject.md) |  | [optional] 
**balance** | str,  | str,  | The targeted balance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

