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

students_router = APIRouter()

@students_router.get("/", response_model=List[Student])
def get_all_students():
    """Retrieve all students."""
    try:
        collection = mongo_db.get_collection("students")
        students = list(collection.find({}, {'_id': 0}))  # Exclude MongoDB's `_id` field
        return [Student.from_dict(student) for student in students]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@students_router.post("/", response_model=dict)
def create_student(student: Student):
    """Create a new student."""
    try:
        result = save_student_to_mongo('students', student)
        if result.get("acknowledged"):
            return {"message": "Student created successfully", "id": str(result.get("inserted_id"))}
        raise HTTPException(status_code=500, detail="Failed to create student")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@students_router.put("/{id}", response_model=dict)
def update_student(id: str, student: Student):
    """Update an existing student."""
    try:
        result = update_student_in_mongo('students', id, student.to_dict())
        if result.get("acknowledged") and result.get("modified_count"):
            return {"message": "Student updated successfully"}
        raise HTTPException(status_code=404, detail="Student not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@students_router.delete("/{id}", response_model=dict)
def delete_student(id: str):
    """Delete a student by ID."""
    try:
        result = delete_student_from_mongo('students', id)
        if result.get("deleted_count"):
            return {"message": "Student deleted successfully"}
        raise HTTPException(status_code=404, detail="Student not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
