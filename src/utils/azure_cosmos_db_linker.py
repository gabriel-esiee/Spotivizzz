import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos import CosmosClient, PartitionKey, DatabaseProxy
import datetime
import json
import pandas as pd

# --- Credentials
endpoint = 'https://clement-zelter.documents.azure.com:443/'
key = 'r9O4hjKqJpxtDYWxBqXbiOH1OqpLWr4Eg4c10ZGXixKdwD9UhAquaj9ZppDlUc6ZQxodme81VgoGACDbTTPyzg=='

client = CosmosClient(url=endpoint, credential=key)


def get_item_from_azure_database(database_name, container_name, item_id):
    """Get an item from its ID in an Azure Cosmos DB

    Parameters:
    -----------

    database_name: (str) name of the database to get the item from
    container_name: (str) name of the container in the database to get the item from
    item_id: (str) ID of the item (found at the end of the item JSON)

    Returns: Pandas DataFrame of the item
    """

    DATABASE_NAME = database_name
    CONTAINER_NAME = container_name

    # --- GET DATABASE
    try:
        database = client.get_database_client(DATABASE_NAME)
        print(f"{DATABASE_NAME} already existed")
    except:
        print(f"database_name doesn't fit any database in your cosmos db")
        return

    # --- GET CONTAINER
    try:
        container = database.get_container_client(CONTAINER_NAME)
    except:
        print(f"container_name doesn't fit any container in your {database_name} database")
        return
    

    # --- GET ITEMS
    try:
        for item in container.query_items(
                query=f'SELECT * FROM c WHERE c.id ="{item_id}"',
                enable_cross_partition_query=True):
            json_str = json.dumps(item, indent=True)
    except:
        print(f"item_id doesn't match any id in your items in {container_name} container")
        return

    #convert to panda dataframe
    data = pd.read_json(json_str, orient='column')

    #clean from the azure cosmos automatic ids
    n = 6
    data.drop(columns=data.columns[-n:], axis=1,  inplace=True)

    return data


def put_item_in_azure_data_base(item, database_name, container_name):
    """Put an item as JSON in an Azure Cosmos DB

    Parameters:
    -----------

    item: (Panda DataFrame) The item to store in the Azure Cosmos DB (converted from DataFrame to JSON)
    database_name: (str) name of the database where to put the item in
    container_name: (str) name of the container where to put the item in

    Returns: the item ID
    """

    DATABASE_NAME = database_name
    CONTAINER_NAME = container_name

    # --- CONVERTED PD DATAFRAME TO JSON

    item_json = item.to_json( orient= 'columns')


    # --- GET DATABASE
    try:
        database = client.get_database_client(DATABASE_NAME)
        print(f"{DATABASE_NAME} already existed")
    except:
        print(f"database_name doesn't fit any database in your cosmos db")
        return

    # --- GET CONTAINER
    try:
        container = database.get_container_client(CONTAINER_NAME)
    except:
        print(f"container_name doesn't fit any container in your {database_name} database")
        return

    
    # Si l'item existe déjà, le remplacer
    # A faire: mettre dans la database
    # Retourner l'ID de l'item

    return
