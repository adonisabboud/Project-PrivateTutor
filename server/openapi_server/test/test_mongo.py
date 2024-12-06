import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

class TestMongoDBConnection(unittest.TestCase):
    def test_connection(self):
        client = None
        try:
            client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000)
        except ConnectionFailure:
            self.fail("MongoDB connection failed - general connection failure")
        except ServerSelectionTimeoutError:
            self.fail("MongoDB connection failed - server selection timeout")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {str(e)}")
        finally:
            if client:
                client.close()
                print("MongoDB connection closed")


