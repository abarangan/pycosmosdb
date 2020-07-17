from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json

# Load config file with database connection info
with open('config.json') as config_file:
    config = json.load(config_file)

# init client
client = CosmosClient(config["endpoint"], config["key"])

# get database
database = client.get_database_client(config["database_name"])

#get container
container = database.get_container_client(config["container_name"])

# Query these items using the SQL query syntax.
# Specifying the partition key value in the query allows Cosmos DB to retrieve data only from the relevant partitions, which improves performance
# <query_items>
for item in container.query_items(
                query=config["query"],
                enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))
