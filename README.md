# pycosmosdb
Simple example of querying cosmos DB from a python script.  Tested in Python 2.7.16 and 3.8.3.

Requires azure-cosmos, the Azure Cosmos DB client library for Python.
<https://azuresdkdocs.blob.core.windows.net/$web/python/azure-cosmos/4.0.0b4/index.html>

Install with Azure library with:

pip install azure-cosmos


Also requires config.json to live in the same directory with the following database connection values defined:

```json
{
    "endpoint": "URI",
    "key": "KEY",
    "database_name": "DATABASE-NAME",
    "container_name": "CONTAINER-ID",
    "query": "QUERY-TO-ISSUE"
}
```
