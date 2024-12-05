# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, List
from typing_extensions import Annotated
from openapi_server.models.meetings_schedule_post_request import MeetingsSchedulePostRequest
from openapi_server.models.model_class import ModelClass
from openapi_server.models.schedule import Schedule
from openapi_server.models.student import Student
from openapi_server.models.teacher import Teacher


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def meetings_schedule_post(
        self,
        meetings_schedule_post_request: MeetingsSchedulePostRequest,
    ) -> None:
        ...


    async def students_register_post(
        self,
        student: Student,
    ) -> None:
        ...


    async def students_student_id_sessions_get(
        self,
        studentId: Annotated[StrictStr, Field(description="The ID of the student")],
    ) -> List[ModelClass]:
        ...


    async def teachers_add_post(
        self,
        teacher: Teacher,
    ) -> None:
        ...


    async def tutors_tutor_id_schedules_get(
        self,
        tutorId: Annotated[StrictStr, Field(description="The ID of the tutor")],
    ) -> Schedule:
        ...


    async def tutors_tutor_id_schedules_post(
        self,
        tutorId: Annotated[StrictStr, Field(description="The ID of the tutor")],
        schedule: Schedule,
    ) -> None:
        ...
