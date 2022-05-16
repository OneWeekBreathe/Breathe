from starlette.config import Config
from api._version import __version__

config = Config(".env")

# API settings
API_PREFIX = "/api"
PROJECT_NAME: str = config("PROJECT_NAME", default="Breathe API")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
VERSION = __version__
API_DESCRIPTION = "Breathe Python API"

# State store configuration
# Cosmos DB endpoint
STATE_STORE_ENDPOINT: str = config("STATE_STORE_ENDPOINT", default="")
# Cosmos DB access key
STATE_STORE_KEY: str = config("STATE_STORE_KEY", default="")     
# Cosmos DB account name
COSMOSDB_ACCOUNT_NAME: str = config("COSMOSDB_ACCOUNT_NAME", default="")
STATE_STORE_DATABASE = "Breathe"
SUBSCRIPTION_ID: str = config("SUBSCRIPTION_ID", default="")
RESOURCE_GROUP_NAME: str = config("RESOURCE_GROUP_NAME", default="")
RESOURCE_LOCATION: str = config("RESOURCE_LOCATION", default="")
