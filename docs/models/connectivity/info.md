# Info


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `build_date`                                                 | *str*                                                        | :heavy_check_mark:                                           | Source commit timestamp (`org.opencontainers.image.created`) |
| `commit`                                                     | *str*                                                        | :heavy_check_mark:                                           | Git commit SHA of the build                                  |
| `version`                                                    | *str*                                                        | :heavy_check_mark:                                           | Build version of the API binary (the image tag)              |