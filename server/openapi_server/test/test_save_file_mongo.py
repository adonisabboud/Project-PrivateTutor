import unittest
from datetime import datetime
import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors

from server.openapi_server.models.File import File
from server.openapi_server.models.DB_utils import save_file_to_mongo, load_file_from_mongo

class TestFileStoring(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.mongo_uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_CLUSTER')}/{os.getenv('DB_NAME')}?retryWrites=true&w=majority"
        cls.client = MongoClient(cls.mongo_uri)
        cls.db = cls.client["test_database"]
        cls.collection = cls.db["test_files"]

        # Inserting a file for testing
        cls.test_file = File(
            file_name="tesing_storing_files_mongo.txt",
            file_type="text/plain",
            file_content=b"TESTing bla bla bla store files mongo",
            owner_id=7654321,
            upload_date=datetime.now()
        )
        cls.result = save_file_to_mongo(cls.collection, cls.test_file)
        cls.inserted_id = cls.result.inserted_id

    @classmethod
    def tearDownClass(cls):
        # Remove only the test file inserted during setup
        if cls.inserted_id:
            cls.collection.delete_one({'_id': cls.inserted_id})
        cls.client.close()

    def test_store_file(self):
        # Extract the file using its ID and validate
        extracted_file = load_file_from_mongo(self.collection, self.inserted_id)
        self.assertEqual(extracted_file.file_name, self.test_file.file_name, "File name mismatch.")
        self.assertEqual(extracted_file.file_type, self.test_file.file_type, "File type mismatch.")
        self.assertEqual(extracted_file.file_content, self.test_file.file_content, "File content mismatch.")
        self.assertEqual(extracted_file.owner_id, self.test_file.owner_id, "Owner ID mismatch.")

if __name__ == '__main__':
    unittest.main()
