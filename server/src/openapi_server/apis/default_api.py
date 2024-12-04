# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt, StrictStr
from typing import Any, List
from openapi_server.models.meeting import Meeting
from openapi_server.models.person import Person
from openapi_server.models.student import Student
from openapi_server.models.teacher import Teacher


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/auth/callback/google",
    responses={
        200: {"description": "Successful login."},
        400: {"description": "Failed to authenticate."},
    },
    tags=["default"],
    summary="Google OAuth2 Callback",
    response_model_by_alias=True,
)
async def auth_callback_google_get(
    code: StrictStr = Query(None, description="", alias="code"),
) -> None:
    """Handles the OAuth2 callback from Google and stores user information."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().auth_callback_google_get(code)


@router.get(
    "/auth/login/google",
    responses={
        302: {"description": "Redirect to Google login page."},
        400: {"description": "Failed to initiate Google login."},
    },
    tags=["default"],
    summary="Login via Google",
    response_model_by_alias=True,
)
async def auth_login_google_get(
) -> None:
    """Redirects the user to Google&#39;s OAuth2 login page."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().auth_login_google_get()


@router.get(
    "/meetings",
    responses={
        200: {"model": List[Meeting], "description": "A list of meetings"},
    },
    tags=["default"],
    summary="Get a list of all meetings",
    response_model_by_alias=True,
)
async def meetings_get(
) -> List[Meeting]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().meetings_get()


@router.post(
    "/meetings",
    responses={
        201: {"description": "Meeting created successfully."},
        400: {"description": "Invalid meeting details provided."},
    },
    tags=["default"],
    summary="Create a new meeting",
    response_model_by_alias=True,
)
async def meetings_post(
    meeting: Meeting = Body(None, description=""),
) -> None:
    """Schedule a meeting involving multiple participants."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().meetings_post(meeting)


@router.post(
    "/meetings/schedule-google-calendar",
    responses={
        200: {"description": "Meeting successfully scheduled in Google Calendar."},
        400: {"description": "Failed to create the meeting."},
        401: {"description": "Unauthorized, user not logged in."},
    },
    tags=["default"],
    summary="Schedule a meeting in Google Calendar",
    response_model_by_alias=True,
)
async def meetings_schedule_google_calendar_post(
    meeting: Meeting = Body(None, description=""),
) -> None:
    """Creates a meeting and adds it to the user&#39;s Google Calendar."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().meetings_schedule_google_calendar_post(meeting)


@router.get(
    "/persons",
    responses={
        200: {"model": List[Person], "description": "A list of persons"},
    },
    tags=["default"],
    summary="Get a list of all persons",
    response_model_by_alias=True,
)
async def persons_get(
) -> List[Person]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().persons_get()


@router.delete(
    "/students",
    responses={
        200: {"description": "Student deleted successfully"},
        404: {"description": "Student not found"},
    },
    tags=["default"],
    summary="Delete a student by ID",
    response_model_by_alias=True,
)
async def students_delete(
    id: StrictInt = Query(None, description="", alias="id"),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().students_delete(id)


@router.get(
    "/students",
    responses={
        200: {"model": List[Student], "description": "A list of students"},
    },
    tags=["default"],
    summary="Get a list of all students",
    response_model_by_alias=True,
)
async def students_get(
) -> List[Student]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().students_get()


@router.post(
    "/students",
    responses={
        201: {"description": "Student created successfully"},
    },
    tags=["default"],
    summary="Create a new student",
    response_model_by_alias=True,
)
async def students_post(
    student: Student = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().students_post(student)


@router.put(
    "/students",
    responses={
        200: {"description": "Student updated successfully."},
        404: {"description": "Student not found."},
    },
    tags=["default"],
    summary="Update student details",
    response_model_by_alias=True,
)
async def students_put(
    student: Student = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().students_put(student)


@router.delete(
    "/teachers",
    responses={
        200: {"description": "Teacher deleted successfully"},
        404: {"description": "Teacher not found"},
    },
    tags=["default"],
    summary="Delete a teacher by ID",
    response_model_by_alias=True,
)
async def teachers_delete(
    id: StrictInt = Query(None, description="", alias="id"),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().teachers_delete(id)


@router.get(
    "/teachers",
    responses={
        200: {"model": List[Teacher], "description": "A list of teachers"},
    },
    tags=["default"],
    summary="Get a list of all teachers",
    response_model_by_alias=True,
)
async def teachers_get(
) -> List[Teacher]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().teachers_get()


@router.post(
    "/teachers",
    responses={
        201: {"description": "Teacher created successfully"},
    },
    tags=["default"],
    summary="Create a new teacher",
    response_model_by_alias=True,
)
async def teachers_post(
    teacher: Teacher = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().teachers_post(teacher)


@router.put(
    "/teachers",
    responses={
        200: {"description": "Teacher updated successfully."},
        404: {"description": "Teacher not found."},
    },
    tags=["default"],
    summary="Update teacher details",
    response_model_by_alias=True,
)
async def teachers_put(
    teacher: Teacher = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().teachers_put(teacher)
