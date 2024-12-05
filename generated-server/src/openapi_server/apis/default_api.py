# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from default_api_base import BaseDefaultApi
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
from pydantic import Field, StrictStr
from typing import Any, List
from typing_extensions import Annotated
from openapi_server.models.meetings_schedule_post_request import MeetingsSchedulePostRequest
from openapi_server.models.model_class import ModelClass
from openapi_server.models.schedule import Schedule
from openapi_server.models.student import Student
from openapi_server.models.teacher import Teacher


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/meetings/schedule",
    responses={
        201: {"description": "Meeting scheduled successfully"},
        400: {"description": "Error in data format"},
    },
    tags=["default"],
    summary="Schedule a meeting between a student and a teacher",
    response_model_by_alias=True,
)
async def meetings_schedule_post(
    meetings_schedule_post_request: MeetingsSchedulePostRequest = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().meetings_schedule_post(meetings_schedule_post_request)


@router.post(
    "/students/register",
    responses={
        201: {"description": "Student registered successfully"},
        400: {"description": "Error in data format"},
    },
    tags=["default"],
    summary="Register a new student",
    response_model_by_alias=True,
)
async def students_register_post(
    student: Student = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().students_register_post(student)


@router.get(
    "/students/{studentId}/sessions",
    responses={
        200: {"model": List[ModelClass], "description": "Successfully retrieved available sessions"},
        404: {"description": "No sessions found"},
    },
    tags=["default"],
    summary="View available tutoring sessions for a student",
    response_model_by_alias=True,
)
async def students_student_id_sessions_get(
    studentId: Annotated[StrictStr, Field(description="The ID of the student")] = Path(..., description="The ID of the student"),
) -> List[ModelClass]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().students_student_id_sessions_get(studentId)


@router.post(
    "/teachers/add",
    responses={
        201: {"description": "Teacher added successfully"},
        400: {"description": "Error in data format"},
    },
    tags=["default"],
    summary="Add a new teacher",
    response_model_by_alias=True,
)
async def teachers_add_post(
    teacher: Teacher = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().teachers_add_post(teacher)


@router.get(
    "/tutors/{tutorId}/schedules",
    responses={
        200: {"model": Schedule, "description": "Successfully retrieved the schedule"},
        404: {"description": "Schedule not found"},
    },
    tags=["default"],
    summary="Get a tutor&#39;s schedule",
    response_model_by_alias=True,
)
async def tutors_tutor_id_schedules_get(
    tutorId: Annotated[StrictStr, Field(description="The ID of the tutor")] = Path(..., description="The ID of the tutor"),
) -> Schedule:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().tutors_tutor_id_schedules_get(tutorId)


@router.post(
    "/tutors/{tutorId}/schedules",
    responses={
        201: {"description": "Schedule created successfully"},
        400: {"description": "Error in data format"},
    },
    tags=["default"],
    summary="Create a new schedule for a tutor",
    response_model_by_alias=True,
)
async def tutors_tutor_id_schedules_post(
    tutorId: Annotated[StrictStr, Field(description="The ID of the tutor")] = Path(..., description="The ID of the tutor"),
    schedule: Schedule = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().tutors_tutor_id_schedules_post(tutorId, schedule)
