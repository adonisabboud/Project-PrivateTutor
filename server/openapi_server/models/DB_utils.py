from pymongo import MongoClient, collection
from pymongo.collection import Collection

from server.openapi_server.models.File import File
from server.openapi_server.models.Mongo import MONGO_URI, DB_NAME
from server.openapi_server.models.meeting import Meeting
from server.openapi_server.models.person import Person
from server.openapi_server.models.student import Student
from server.openapi_server.models.teacher import Teacher


def connect_to_mongo(uri: str, db_name: str):
    client = MongoClient(uri)
    return client[db_name]


###################################################
def save_file_to_mongo(collection: Collection, file: File):
    """
    Saves a File instance to MongoDB.
    """
    document = file.to_dict()
    if '_id' in document:
        return collection.replace_one({'_id': document['_id']}, document, upsert=True)
    else:
        return collection.insert_one(document)

def load_file_from_mongo(collection: Collection, file_id):
    """
    Loads a File instance from MongoDB by ID.
    """
    document = collection.find_one({'_id': file_id})
    if document:
        return File.from_dict(document)
    else:
        raise ValueError("File not found with ID: {}".format(file_id))
###################################################
def save_to_mongo(collection: Collection, data):
    if hasattr(data, 'to_dict'):
        document = data.to_dict()
        document['type'] = data.__class__.__name__  # Add type information
        if '_id' in document:
            return collection.replace_one({'_id': document['_id']}, document, upsert=True)
        else:
            return collection.insert_one(document)
    else:
        raise ValueError("Provided data object does not have a to_dict() method")

def load_from_mongo(collection: Collection, query, model_classes):
    document = collection.find_one(query)
    if document:
        model_class = model_classes.get(document['type'])
        if model_class and hasattr(model_class, 'from_dict'):
            return model_class.from_dict(document)
        else:
            raise ValueError(f"No model class found for type {document['type']}")
    else:
        raise ValueError("No document found with the given query")

def list_collections_in_db(db):
    return db.list_collection_names()


