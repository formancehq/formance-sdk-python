# AuditFailure

Stable reason, subcode, and facts for a failed proposal. Presentation text is rendered when read and is not stored in the audit chain.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `code`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Stable failure subcode                                               |
| `facts`                                                              | Dict[str, *str*]                                                     | :heavy_minus_sign:                                                   | Validated facts used to render the failure                           |
| `reason`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Typed error reason identifier (e.g. ERROR_REASON_INSUFFICIENT_FUNDS) |