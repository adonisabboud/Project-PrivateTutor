# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, List  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.meetings_schedule_post_request import MeetingsSchedulePostRequest  # noqa: F401
from openapi_server.models.model_class import ModelClass  # noqa: F401
from openapi_server.models.schedule import Schedule  # noqa: F401
from openapi_server.models.student import Student  # noqa: F401
from openapi_server.models.teacher import Teacher  # noqa: F401


def test_meetings_schedule_post(client: TestClient):
    """Test case for meetings_schedule_post

    Schedule a meeting between a student and a teacher
    """
    meetings_schedule_post_request = openapi_server.MeetingsSchedulePostRequest()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/meetings/schedule",
    #    headers=headers,
    #    json=meetings_schedule_post_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_students_register_post(client: TestClient):
    """Test case for students_register_post

    Register a new student
    """
    student = {"phone":"phone","name":"name","id":"id","email":"email","available_times":["availableTimes","availableTimes"]}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/students/register",
    #    headers=headers,
    #    json=student,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_students_student_id_sessions_get(client: TestClient):
    """Test case for students_student_id_sessions_get

    View available tutoring sessions for a student
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/students/{studentId}/sessions".format(studentId='student_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_teachers_add_post(client: TestClient):
    """Test case for teachers_add_post

    Add a new teacher
    """
    teacher = {"courses":["courses","courses"],"phone":"phone","name":"name","id":"id","email":"email","available_times":["availableTimes","availableTimes"]}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/teachers/add",
    #    headers=headers,
    #    json=teacher,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tutors_tutor_id_schedules_get(client: TestClient):
    """Test case for tutors_tutor_id_schedules_get

    Get a tutor's schedule
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tutors/{tutorId}/schedules".format(tutorId='tutor_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tutors_tutor_id_schedules_post(client: TestClient):
    """Test case for tutors_tutor_id_schedules_post

    Create a new schedule for a tutor
    """
    schedule = {"date":"2000-01-23","sessions":[{"subject":"subject","start_time":"2000-01-23T04:56:07.000+00:00","session_id":"sessionId","end_time":"2000-01-23T04:56:07.000+00:00"},{"subject":"subject","start_time":"2000-01-23T04:56:07.000+00:00","session_id":"sessionId","end_time":"2000-01-23T04:56:07.000+00:00"}],"schedule_id":"scheduleId"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/tutors/{tutorId}/schedules".format(tutorId='tutor_id_example'),
    #    headers=headers,
    #    json=schedule,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

