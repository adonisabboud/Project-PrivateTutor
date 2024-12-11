from fastapi import APIRouter, HTTPException
from server.openapi_server.models.DB_utils import (
    save_teacher_to_mongo,
    get_teacher_from_mongo,
    update_teacher_in_mongo,
    delete_teacher_from_mongo,
    mongo_db
)
from server.openapi_server.models.teacher import Teacher

teachers_router = APIRouter()

@teachers_router.get("/", response_model=list[Teacher])
def get_all_teachers():
    """Retrieve all teachers."""
    try:
        collection = mongo_db.get_collection("teachers")
        teachers = list(collection.find({}, {'_id': 0}))  # Exclude `_id` field from the results
        return [Teacher(**teacher) for teacher in teachers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@teachers_router.post("/", response_model=Teacher)
def create_teacher(teacher: Teacher):
    """Create a new teacher."""
    try:
        result = save_teacher_to_mongo('teachers', teacher)
        if result.get("acknowledged"):
            teacher.id = str(result.get("inserted_id"))  # Set the generated ID in the Teacher object
            return teacher
        raise HTTPException(status_code=500, detail="Failed to create teacher")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@teachers_router.put("/{id}", response_model=Teacher)
def update_teacher(id: str, teacher: Teacher):
    """Update a teacher's details."""
    try:
        result = update_teacher_in_mongo('teachers', id, teacher.dict())
        if result.get("acknowledged") and result.get("modified_count"):
            return teacher
        raise HTTPException(status_code=404, detail="Teacher not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@teachers_router.delete("/{id}")
def delete_teacher(id: str):
    """Delete a teacher by ID."""
    try:
        result = delete_teacher_from_mongo('teachers', id)
        if result.get("deleted_count"):
            return {"message": "Teacher deleted successfully"}
        raise HTTPException(status_code=404, detail="Teacher not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
