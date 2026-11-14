# V2StageDelay


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `duration`                                                                                | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Wait for this long, expressed as a Go duration such as 10s. Mutually exclusive with until |
| `until`                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                      | :heavy_minus_sign:                                                                        | Wait until this absolute point in time. Mutually exclusive with duration                  |