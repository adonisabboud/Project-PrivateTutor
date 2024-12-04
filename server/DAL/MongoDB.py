import os
import logging
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Retrieve values from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_cluster = os.getenv('DB_CLUSTER')
db_name = os.getenv('DB_NAME')

# Create MongoDB URI using the environment variables
uri = f"mongodb+srv://{db_user}:{db_password}@{db_cluster}/?retryWrites=true&w=majority&appName={db_name}"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    logging.info(f"Pinged your deployment. You successfully connected to MongoDB on {db_name}!")
except Exception as e:
    logging.error("Failed to connect to MongoDB", exc_info=True)
