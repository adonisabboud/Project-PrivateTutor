from fastapi import APIRouter, HTTPException
from typing import List
from server.openapi_server.models.DB_utils import (
    save_student_to_mongo,
    get_student_from_mongo,
    update_student_in_mongo,
    delete_student_from_mongo,
    mongo_db
)
from server.openapi_server.models.student import Student
from bson.errors import InvalidId
from bson import ObjectId

students_router = APIRouter()

@students_router.get("/", response_model=List[Student])
def get_all_students():
    """Retrieve all students."""
    try:
        collection = mongo_db.get_collection("students")
        students = list(collection.find({}, {'_id': 0}))  # Exclude MongoDB's `_id` field
        return [Student(**student) for student in students]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving students: {str(e)}")

@students_router.get("/{student_id}", response_model=Student)
def get_student_by_id(student_id: str):
    """Retrieve a specific student by ID."""
    try:
        try:
            object_id = ObjectId(student_id)  # Validate and convert the ID
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid student ID format.")
        student = get_student_from_mongo("students", str(object_id))
        if not student:
            raise HTTPException(status_code=404, detail="Student not found.")
        return student
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving student: {str(e)}")

@students_router.post("/", response_model=dict)
def create_student(student: Student):
    """Create a new student."""
    try:
        result = save_student_to_mongo('students', student)
        if result.get("acknowledged"):
            return {"message": "Student created successfully", "id": str(result.get("inserted_id"))}
        raise HTTPException(status_code=500, detail="Failed to create student.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating student: {str(e)}")

@students_router.put("/{id}", response_model=dict)
def update_student(id: str, student: Student):
    """Update an existing student."""
    try:
        try:
            object_id = ObjectId(id)  # Validate and convert the ID
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid student ID format.")
        result = update_student_in_mongo('students', str(object_id), student.model_dump(exclude_unset=True))
        if result.get("acknowledged") and result.get("modified_count"):
            return {"message": "Student updated successfully."}
        raise HTTPException(status_code=404, detail="Student not found or no changes detected.")
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating student: {str(e)}")

@students_router.delete("/{student_id}", response_model=dict)
def delete_student(student_id: str):
    """Delete a student by ID."""
    try:
        try:
            object_id = ObjectId(student_id)  # Validate and convert the ID
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid student ID format.")
        result = delete_student_from_mongo("students", str(object_id))
        if result["deleted_count"] == 0:
            raise HTTPException(status_code=404, detail="Student not found.")
        return {"message": "Student deleted successfully."}
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting student: {str(e)}")
