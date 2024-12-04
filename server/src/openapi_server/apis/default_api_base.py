# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt, StrictStr
from typing import Any, List
from openapi_server.models.meeting import Meeting
from openapi_server.models.person import Person
from openapi_server.models.student import Student
from openapi_server.models.teacher import Teacher


class BaseDefaultApi:
    subclasses: ClassVar[List] = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)

    async def auth_callback_google_get(
            self,
            code: StrictStr,
    ) -> None:
        """Handles the OAuth2 callback from Google and stores user information."""
        ...

    async def auth_login_google_get(
            self,
    ) -> None:
        """Redirects the user to Google&#39;s OAuth2 login page."""
        ...

    async def meetings_get(
            self,
    ) -> List[Meeting]:
        ...

    async def meetings_post(
            self,
            meeting: Meeting,
    ) -> None:
        """Schedule a meeting involving multiple participants."""
        ...

    async def meetings_schedule_google_calendar_post(
            self,
            meeting: Meeting,
    ) -> None:
        """Creates a meeting and adds it to the user&#39;s Google Calendar."""
        ...

    async def persons_get(
            self,
    ) -> List[Person]:
        ...

    async def students_delete(
            self,
            id: StrictInt,
    ) -> None:
        ...

    async def students_get(
            self,
    ) -> List[Student]:
        ...

    async def students_post(
            self,
            student: Student,
    ) -> None:
        ...

    async def students_put(
            self,
            student: Student,
    ) -> None:
        ...

    async def teachers_delete(
            self,
            id: StrictInt,
    ) -> None:
        ...

    async def teachers_get(
            self,
    ) -> List[Teacher]:
        ...

    async def teachers_post(
            self,
            teacher: Teacher,
    ) -> None:
        ...

    async def teachers_put(
            self,
            teacher: Teacher,
    ) -> None:
        ...
