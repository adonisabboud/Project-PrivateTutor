from fastapi import APIRouter, HTTPException
from server.openapi_server.models.DB_utils import (
    save_meeting_to_mongo,
    get_meeting_from_mongo,
    update_meeting_in_mongo,
    delete_meeting_from_mongo,
    mongo_db
)
from server.openapi_server.models.meeting import Meeting

meetings_router = APIRouter()

@meetings_router.get("/", response_model=list[Meeting])
def get_all_meetings():
    """Retrieve all meetings."""
    try:
        collection = mongo_db.get_collection("meetings")
        meetings = list(collection.find({}, {'_id': 0}))  # Exclude MongoDB's `_id` field
        return [Meeting.parse_obj(meeting) for meeting in meetings]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@meetings_router.post("/", response_model=dict)
def create_meeting(meeting: Meeting):
    """Create a new meeting."""
    try:
        result = save_meeting_to_mongo('meetings', meeting)
        if result.get("acknowledged"):
            return {"message": "Meeting created successfully", "id": str(result.get("inserted_id"))}
        raise HTTPException(status_code=500, detail="Failed to create meeting")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@meetings_router.put("/{id}", response_model=dict)
def update_meeting(id: str, meeting: Meeting):
    """Update an existing meeting."""
    try:
        result = update_meeting_in_mongo('meetings', id, meeting.to_dict())
        if result.get("acknowledged") and result.get("modified_count"):
            return {"message": "Meeting updated successfully"}
        raise HTTPException(status_code=404, detail="Meeting not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@meetings_router.delete("/{id}", response_model=dict)
def delete_meeting(id: str):
    """Delete a meeting by ID."""
    try:
        result = delete_meeting_from_mongo('meetings', id)
        if result.get("deleted_count"):
            return {"message": "Meeting deleted successfully"}
        raise HTTPException(status_code=404, detail="Meeting not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
