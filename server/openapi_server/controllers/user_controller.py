from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId
from server.openapi_server.models.DB_utils import (
    create_user,
    get_users_by_username,
    authenticate_user,
    update_user,
    delete_user,
    get_user_by_id,
)
from server.openapi_server.models.user import User

user_router = APIRouter()

def custom_jsonable_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, list):  # Handle lists of ObjectId
        return [custom_jsonable_encoder(item) for item in obj]
    if isinstance(obj, dict):  # Handle nested dictionaries
        return {key: custom_jsonable_encoder(value) for key, value in obj.items()}
    return jsonable_encoder(obj)

# Request Models
class CreateUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    roles: list[str]
    name: str = Field(..., max_length=100)

class AuthenticateUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

class UpdateUserRequest(BaseModel):
    about_section: str = Field(..., max_length=500)

# Endpoints

@user_router.post("/", status_code=201)
async def create_user_endpoint(request: CreateUserRequest):
    """Create a new user."""
    try:
        user = User(**request.dict())
        user_id = create_user("users", user)
        return {"message": "User created successfully", "user_id": str(user_id)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the user: {e}")

@user_router.delete("/{user_id}")
async def delete_user_endpoint(user_id: str):
    """Delete a user."""
    try:
        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=400, detail="Invalid user ID format.")
        result = delete_user("users", user_id)
        if result:
            return {"message": "User deleted successfully"}
        raise HTTPException(status_code=404, detail="User not found")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the user: {e}")

@user_router.get("/id/{user_id}")
async def get_user_by_id_endpoint(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format.")
    try:
        user = get_user_by_id("users", user_id)
        if user:
            return custom_jsonable_encoder(user.dict(by_alias=True))
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving the user: {e}")

@user_router.get("/{username}")
async def get_users_by_username_endpoint(username: str):
    """Retrieve all users by their username."""
    try:
        users = get_users_by_username("users", username)
        if users:
            return custom_jsonable_encoder([user.dict(by_alias=True) for user in users])
        raise HTTPException(status_code=404, detail="No users found with this username")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@user_router.post("/login")
async def authenticate_user_endpoint(request: AuthenticateUserRequest):
    """Authenticate a user by email and password."""
    try:
        user = authenticate_user("users", request.email, request.password)
        if user:
            return {
                "message": "Authentication successful",
                "user_id": str(user.id),
                "email": user.email,
                "roles": user.roles,
            }
        raise HTTPException(status_code=401, detail="Invalid credentials")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during authentication: {e}")

@user_router.put("/{user_id}")
async def update_user_endpoint(user_id: str, request: UpdateUserRequest):
    """Update a user's details."""
    try:
        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=400, detail="Invalid user ID format.")
        updates = request.dict()
        result = update_user("users", user_id, updates)
        if result:
            return {"message": "User updated successfully"}
        raise HTTPException(status_code=404, detail="User not found")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the user: {e}")
