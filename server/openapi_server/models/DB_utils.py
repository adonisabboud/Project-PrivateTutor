import uuid
from typing import Optional, Union, List

from server.openapi_server.models.File import File
from server.openapi_server.models.Mongo import MongoDatabase
from server.openapi_server.models.meeting import Meeting
from server.openapi_server.models.person import Person
from server.openapi_server.models.student import Student
from server.openapi_server.models.teacher import Teacher
from bson.errors import InvalidId
from bson import ObjectId
from pymongo.collection import Collection
from pymongo.errors import PyMongoError
from pymongo import MongoClient, errors as pymongo_errors
from passlib.context import CryptContext
from datetime import datetime

from server.openapi_server.models.user import User

mongo_db = MongoDatabase()  # Create a global instance

def save_file_to_mongo(collection_name: str, file: File) -> dict:
    try:
        collection = mongo_db.get_collection(collection_name)
        document = file.to_dict()
        if '_id' in document and document['_id'] is None:
            del document['_id']
        if '_id' in document:
            result = collection.replace_one({'_id': document['_id']}, document, upsert=True)
        else:
            result = collection.insert_one(document)
        return {"acknowledged": result.acknowledged, "inserted_id": getattr(result, 'inserted_id', None)}
    except Exception as e:
        raise RuntimeError(f"Error saving file to MongoDB collection '{collection_name}': {e}")

def load_file_from_mongo(collection_name: str, file_id):
    try:
        collection = mongo_db.get_collection(collection_name)
        document = collection.find_one({'_id': file_id})
        if document:
            return File.from_dict(document)
        else:
            raise ValueError(f"File not found with ID: {file_id}")
    except Exception as e:
        raise RuntimeError(f"Error loading file from MongoDB collection '{collection_name}': {e}")
################################################################



def save_meeting_to_mongo(collection_name: str, meeting: Meeting) -> dict:
    """
    Saves a Meeting instance to the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param meeting: Meeting object to save.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        document = meeting.model_dump(by_alias=True)  # Use model_dump instead of dict

        if '_id' in document and document['_id']:
            document['_id'] = ObjectId(document['_id'])
            result = collection.replace_one({'_id': document['_id']}, document, upsert=True)
        else:
            result = collection.insert_one(document)

        return {"acknowledged": result.acknowledged, "modified_count": getattr(result, 'modified_count', 0), "inserted_id": str(getattr(result, 'inserted_id', ''))}
    except PyMongoError as e:
        raise RuntimeError(f"Error saving meeting to MongoDB in collection '{collection_name}': {e}")

def get_meeting_from_mongo(collection_name: str, meeting_id: str) -> Meeting:
    """
    Retrieves a Meeting instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param meeting_id: ID of the Meeting to retrieve.
    :return: The Meeting object, or None if not found.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        document = collection.find_one({'_id': ObjectId(meeting_id)})
        return Meeting(**document) if document else None
    except PyMongoError as e:
        raise RuntimeError(f"Error retrieving meeting from MongoDB in collection '{collection_name}': {e}")

def update_meeting_in_mongo(collection_name: str, meeting_id: str, updates: dict) -> dict:
    try:
        collection = mongo_db.get_collection(collection_name)
        result = collection.update_one({'_id': ObjectId(meeting_id)}, {'$set': updates})
        if result.matched_count == 0:
            # No documents matched, which could mean an invalid ID was provided
            return {"acknowledged": False, "error": "No document found with the provided ID."}
        return {"acknowledged": result.acknowledged, "modified_count": result.modified_count}
    except pymongo_errors.InvalidId:
        return {"acknowledged": False, "error": "Invalid ID format."}
    except pymongo_errors.PyMongoError as e:
        # Log this error or handle it as needed
        return {"acknowledged": False, "error": str(e)}

def delete_meeting_from_mongo(collection_name: str, meeting_id: str) -> dict:
    """
    Deletes a Meeting instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param meeting_id: ID of the Meeting to delete.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        result = collection.delete_one({'_id': ObjectId(meeting_id)})
        return {"acknowledged": result.acknowledged, "deleted_count": result.deleted_count}
    except PyMongoError as e:
        raise RuntimeError(f"Error deleting meeting from MongoDB: {e}")

######################################################################

def save_person_to_mongo(collection_name: str, person: Person) -> dict:
    """
    Saves a Person instance to the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param person: Person instance to save.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        document = person.model_dump(by_alias=True, exclude_none=True)

        result = collection.insert_one(document)
        return {"acknowledged": result.acknowledged, "inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error saving person to MongoDB: {e}")

def get_person_from_mongo(collection_name: str, person_id: str) -> Optional[Person]:
    """
    Retrieves a Person instance from the MongoDB collection.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        try:
            object_id = ObjectId(person_id)  # Convert person_id to ObjectId
        except InvalidId as e:
            raise RuntimeError(f"Invalid ObjectId: {e}")

        document = collection.find_one({"_id": object_id})
        if document:
            return Person(**document)  # Pass document directly to the model
        return None
    except Exception as e:
        raise RuntimeError(f"Error retrieving person from MongoDB in collection '{collection_name}': {e}")

def update_person_in_mongo(collection_name: str, person_id: str, updates: dict) -> dict:
    """
    Updates a Person instance in the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param person_id: ID of the Person to update.
    :param updates: Dictionary containing fields to update.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(person_id)
        result = collection.update_one({"_id": object_id}, {"$set": updates})
        return {
            "acknowledged": result.acknowledged,
            "modified_count": result.modified_count,
        }
    except Exception as e:
        raise RuntimeError(f"Error updating person in MongoDB: {e}")


def delete_person_from_mongo(collection_name: str, person_id: str) -> dict:
    """
    Deletes a Person instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param person_id: ID of the Person to delete.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(person_id)
        result = collection.delete_one({"_id": object_id})
        return {
            "acknowledged": result.acknowledged,
            "deleted_count": result.deleted_count,
        }
    except Exception as e:
        raise RuntimeError(f"Error deleting person from MongoDB: {e}")

##################################################################
def save_student_to_mongo(collection_name: str, student: Student) -> dict:
    """
    Saves a Student instance to the MongoDB collection.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        document = student.model_dump()
        if "_id" in document and document["_id"]:
            # Ensure `_id` is an ObjectId
            document["_id"] = ObjectId(document["_id"])
            result = collection.replace_one({"_id": document["_id"]}, document, upsert=True)
            return {
                "acknowledged": result.acknowledged,
                "modified_count": result.modified_count,
                "inserted_id": str(document["_id"]) if result.upserted_id else None,
            }
        else:
            # Insert if no `_id` exists
            result = collection.insert_one(document)
            return {
                "acknowledged": result.acknowledged,
                "inserted_id": str(result.inserted_id),
            }
    except Exception as e:
        raise RuntimeError(f"Error saving student to MongoDB in collection '{collection_name}': {e}")

def get_student_from_mongo(collection_name: str, student_id: str) -> Optional[Student]:
    """
    Retrieves a Student instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param student_id: ID of the Student to retrieve.
    :return: The Student object, or None if not found.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(student_id)
        document = collection.find_one({'_id': object_id})
        if document:
            # Convert '_id' back to a string for compatibility with the Student model
            document["id"] = str(document["_id"])
            del document["_id"]
            return Student.model_validate(document)
        else:
            return None
    except Exception as e:
        raise RuntimeError(f"Error retrieving student from MongoDB in collection '{collection_name}': {e}")

def update_student_in_mongo(collection_name: str, student_id: str, updates: dict) -> dict:
    """
    Updates a Student instance in the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param student_id: ID of the Student to update.
    :param updates: Dictionary containing fields to update.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(student_id)
        result = collection.update_one({'_id': object_id}, {'$set': updates})
        return {
            "acknowledged": result.acknowledged,
            "modified_count": result.modified_count
        }
    except Exception as e:
        raise RuntimeError(f"Error updating student in MongoDB: {e}")

def delete_student_from_mongo(collection_name: str, student_id: str) -> dict:
    """
    Deletes a Student instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param student_id: ID of the Student to delete.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection = mongo_db.get_collection(collection_name)

        # Validate ObjectId
        try:
            object_id = ObjectId(student_id)
        except InvalidId:
            return {
                "acknowledged": False,
                "error": f"Invalid ObjectId: {student_id}"
            }

        # Perform the delete operation
        result = collection.delete_one({"_id": object_id})

        # Check if a document was deleted
        if result.deleted_count == 0:
            return {
                "acknowledged": result.acknowledged,
                "deleted_count": result.deleted_count,
                "error": "No student found with the provided ID."
            }

        # Success response
        return {
            "acknowledged": result.acknowledged,
            "deleted_count": result.deleted_count,
            "message": "Student deleted successfully."
        }
    except Exception as e:
        raise RuntimeError(f"Error deleting student from MongoDB: {e}")




################################################################
def save_teacher_to_mongo(collection_name: str, teacher: Teacher) -> dict:
    """
    Saves a Teacher instance to the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param teacher: Teacher object to save.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        document = teacher.model_dump()
        if '_id' in document and document['_id']:
            # Ensure `_id` is an ObjectId
            document['_id'] = ObjectId(document['_id'])
            result = collection.replace_one({'_id': document['_id']}, document, upsert=True)
            return {"acknowledged": result.acknowledged, "modified_count": result.modified_count}
        else:
            # Insert if no `_id` exists
            document.pop('_id', None)  # Ensure no invalid `_id` field
            result = collection.insert_one(document)
            return {"acknowledged": result.acknowledged, "inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error saving teacher to MongoDB in collection '{collection_name}': {e}")


def get_teacher_from_mongo(collection_name: str, teacher_id: str) -> Teacher:
    """
    Retrieves a Teacher instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param teacher_id: ID of the Teacher to retrieve.
    :return: The Teacher object, or None if not found.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(teacher_id)
        document = collection.find_one({'_id': object_id})
        if document:
            document['id'] = str(document.pop('_id'))  # Convert ObjectId back to string for Pydantic
            return Teacher.model_validate(document)
        else:
            return None
    except Exception as e:
        raise RuntimeError(f"Error retrieving teacher from MongoDB in collection '{collection_name}': {e}")


def update_teacher_in_mongo(collection_name: str, teacher_id: str, updates: dict) -> dict:
    """
    Updates a Teacher instance in the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param teacher_id: ID of the Teacher to update.
    :param updates: Dictionary containing fields to update.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(teacher_id)
        result = collection.update_one({'_id': object_id}, {'$set': updates})
        return {
            "acknowledged": result.acknowledged,
            "modified_count": result.modified_count
        }
    except Exception as e:
        raise RuntimeError(f"Error updating teacher in MongoDB: {e}")


def delete_teacher_from_mongo(collection_name: str, teacher_id: str) -> dict:
    """
    Deletes a Teacher instance from the MongoDB collection.

    :param collection_name: Name of the MongoDB collection.
    :param teacher_id: ID of the Teacher to delete.
    :return: A dictionary containing the result of the operation.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        object_id = ObjectId(teacher_id)
        result = collection.delete_one({'_id': object_id})
        return {
            "acknowledged": result.acknowledged,
            "deleted_count": result.deleted_count
        }
    except Exception as e:
        raise RuntimeError(f"Error deleting teacher from MongoDB: {e}")

#################################################################
def save_to_mongo(collection_name: str, data):
    try:
        collection = mongo_db.get_collection(collection_name)
        if hasattr(data, 'to_dict'):
            document = data.to_dict()
            document['type'] = data.__class__.__name__
            if '_id' in document:
                return collection.replace_one({'_id': document['_id']}, document, upsert=True)
            else:
                return collection.insert_one(document)
        else:
            raise ValueError("Provided data object does not have a to_dict() method")
    except Exception as e:
        raise RuntimeError(f"Error saving data to MongoDB collection '{collection_name}': {e}")

def load_from_mongo(collection_name: str, query, model_classes):
    try:
        collection = mongo_db.get_collection(collection_name)
        document = collection.find_one(query)
        if document:
            model_class = model_classes.get(document['type'])
            if model_class and hasattr(model_class, 'from_dict'):
                return model_class.from_dict(document)
            else:
                raise ValueError(f"No model class found for type {document['type']}")
        else:
            raise ValueError("No document found with the given query")
    except Exception as e:
        raise RuntimeError(f"Error loading data from MongoDB collection '{collection_name}': {e}")

def insert_data(collection_name: str, data):
    try:
        collection = mongo_db.get_collection(collection_name)
        if isinstance(data, list):
            result = collection.insert_many(data)
        else:
            result = collection.insert_one(data)
        return result
    except Exception as e:
        raise RuntimeError(f"Error inserting data into MongoDB collection '{collection_name}': {e}")

def find_data(collection_name: str, query):
    try:
        collection = mongo_db.get_collection(collection_name)
        documents = collection.find(query)
        return list(documents)
    except Exception as e:
        raise RuntimeError(f"Error finding data in MongoDB collection '{collection_name}': {e}")

def find_one_data(collection_name: str, query):
    try:
        collection = mongo_db.get_collection(collection_name)
        document = collection.find_one(query)
        return document
    except Exception as e:
        raise RuntimeError(f"Error finding a document in MongoDB collection '{collection_name}': {e}")



#############################################################################################################################

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_object_id(user_id: str) -> ObjectId:
    """
    Validate and convert a string to ObjectId.

    :param user_id: The ID to validate.
    :return: ObjectId if valid.
    :raises ValueError: If the ID is invalid.
    """
    if not ObjectId.is_valid(user_id):
        raise ValueError(f"{user_id} is not a valid MongoDB ObjectId.")
    return ObjectId(user_id)


def hash_password(password: str) -> str:
    """Hash a plain-text password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def create_user(collection_name: str, user: User) -> str:
    """
    Create a new user in the specified MongoDB collection.
    :param collection_name: Name of the MongoDB collection.
    :param user: User object to be created.
    :return: ID of the created user as a string.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        # Ensure email is unique
        if collection.find_one({"email": user.email}):
            raise ValueError("A user with this email already exists.")

        # Prepare the user document for insertion
        user_data = user.model_dump(by_alias=True, exclude_none=True)
        user_data["password"] = hash_password(user.password)  # Hash the password
        user_data["created_at"] = datetime.utcnow()  # Add creation timestamp

        result = collection.insert_one(user_data)
        return str(result.inserted_id)  # Return the ObjectId as a string
    except PyMongoError as e:
        raise RuntimeError(f"Error creating user: {e}")


def get_user_by_id(collection_name: str, user_id: str) -> Optional[User]:
    """
    Fetch a user by their MongoDB ObjectId.
    """
    try:
        object_id = validate_object_id(user_id)
        collection = mongo_db.get_collection(collection_name)
        user_doc = collection.find_one({"_id": object_id})  # Query using `_id`
        if user_doc:
            return User(**user_doc)  # No need to map `_id` to `id`
        return None
    except PyMongoError as e:
        raise RuntimeError(f"Error fetching user by ID from collection '{collection_name}': {e}")


def get_users_by_username(collection_name: str, username: str) -> List[User]:
    """
    Retrieve all users with the given username from the specified MongoDB collection.
    """
    try:
        collection = mongo_db.get_collection(collection_name)
        user_docs = collection.find({"username": username})
        return [User(**doc) for doc in user_docs]  # No need to map `_id` to `id`
    except PyMongoError as e:
        raise RuntimeError(f"Error retrieving users by username from collection '{collection_name}': {e}")


def authenticate_user(collection_name: str, email: str, password: str) -> Optional[User]:
    """
    Authenticate a user by verifying their email and password.
    :param collection_name: Name of the MongoDB collection.
    :param email: Email of the user (unique).
    :param password: Plain-text password to verify.
    :return: User object if authentication is successful, otherwise None.
    """
    try:
        collection: Collection = mongo_db.get_collection(collection_name)
        user_doc = collection.find_one({"email": email})  # Query by email
        if user_doc and "password" in user_doc and verify_password(password, user_doc["password"]):
            return User(**user_doc)
        return None
    except Exception as e:
        raise RuntimeError(f"Error during authentication: {e}")


def update_user(collection_name: str, user_id: str, updates: dict) -> bool:
    """
    Update a user's information.
    :param collection_name: Name of the MongoDB collection.
    :param user_id: ObjectId of the user to update.
    :param updates: Dictionary of fields to update.
    :return: True if the update was successful, False otherwise.
    """
    try:
        object_id = validate_object_id(user_id)
        collection = mongo_db.get_collection(collection_name)
        result = collection.update_one({"_id": object_id}, {"$set": updates})
        return result.modified_count > 0
    except (PyMongoError, ValueError) as e:
        raise RuntimeError(f"Error updating user in collection '{collection_name}': {e}")


def delete_user(collection_name: str, user_id: str) -> bool:
    """
    Delete a user from the database.
    :param collection_name: Name of the MongoDB collection.
    :param user_id: ObjectId of the user to delete.
    :return: True if the deletion was successful, False otherwise.
    """
    try:
        object_id = validate_object_id(user_id)
        collection = mongo_db.get_collection(collection_name)
        result = collection.delete_one({"_id": object_id})
        return result.deleted_count > 0
    except (PyMongoError, ValueError) as e:
        raise RuntimeError(f"Error deleting user from collection '{collection_name}': {e}")
