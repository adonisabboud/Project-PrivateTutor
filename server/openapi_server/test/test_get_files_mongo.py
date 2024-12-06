import unittest
from datetime import datetime
import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors

from server.openapi_server.models.File import File
from server.openapi_server.models.DB_utils import save_file_to_mongo, load_file_from_mongo


class TestFileExtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.mongo_uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_CLUSTER')}/{os.getenv('DB_NAME')}?retryWrites=true&w=majority"
        cls.client = MongoClient(cls.mongo_uri)
        cls.db = cls.client["test_database"]
        cls.collection = cls.db["test_files"]

        # Create and insert the file object
        cls.test_file = File(
            file_name="extract_test.txt",
            file_type="text/plain",
            file_content=b"Hello, world!",
            owner_id=3222221111,
            upload_date=datetime.now()
        )
        cls.result = save_file_to_mongo(cls.collection, cls.test_file)
        cls.inserted_id = cls.result.inserted_id

    @classmethod
    def tearDownClass(cls):
        # Cleanup: Remove the inserted file
        cls.collection.delete_one({'_id': cls.inserted_id})
        cls.client.close()

    def test_extract_file(self):
        # Attempt to retrieve the previously stored file by its ID
        extracted_file = load_file_from_mongo(self.collection, self.inserted_id)

        # Check that the extracted file matches the one we saved
        self.assertEqual(extracted_file.file_name, self.test_file.file_name)
        self.assertEqual(extracted_file.file_type, self.test_file.file_type)
        self.assertEqual(extracted_file.file_content, self.test_file.file_content)
        self.assertEqual(extracted_file.owner_id, self.test_file.owner_id)
        # Compare dates in a formatted string since direct datetime comparison might fail due to precision issues in serialization
        self.assertEqual(extracted_file.upload_date.strftime("%Y-%m-%d %H:%M:%S"),
                         self.test_file.upload_date.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    unittest.main()
