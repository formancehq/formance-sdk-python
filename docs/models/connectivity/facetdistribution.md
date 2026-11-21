# FacetDistribution

Distinct-connector counts per facet value, computed from the
namespaced `facet:value` tags of the connectors matching the query.



## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `facets`                                                            | Dict[str, Dict[str, *int*]]                                         | :heavy_check_mark:                                                  | Facet name to value-to-count map, e.g. `{"provider": {"psp": 6}}`.<br/> |
| `total`                                                             | *int*                                                               | :heavy_check_mark:                                                  | Published connectors matching the query.                            |