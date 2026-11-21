# ConnectorVersionSummary


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `digest`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Image digest pinning this version immutably, when known              |
| `release_date`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `version`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Version tag (e.g. `v1.4.2`)                                          |