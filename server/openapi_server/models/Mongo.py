import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
try:
    load_dotenv()
    print("Environment variables loaded successfully.")
except Exception as e:
    print(f"Error loading .env file: {e}")
    exit(1)

# Get MongoDB credentials from .env
try:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_CLUSTER = os.getenv("DB_CLUSTER")
    DB_NAME = os.getenv("DB_NAME")

    if not all([DB_USER, DB_PASSWORD, DB_CLUSTER, DB_NAME]):
        raise ValueError("Missing required environment variables.")

    print("All required environment variables are present.")
except ValueError as ve:
    print(f"Configuration error: {ve}")
    exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    exit(1)

# Construct the MongoDB URI
try:
    MONGO_URI = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_CLUSTER}/{DB_NAME}?retryWrites=true&w=majority"
    print("MongoDB URI constructed successfully.")
except Exception as e:
    print(f"Error constructing MongoDB URI: {e}")
    exit(1)

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Example: Print the list of collections in the database
try:
    collections = db.list_collection_names()
    print("Collections in the database:", collections)
except Exception as e:
    print(f"Error retrieving collections: {e}")
