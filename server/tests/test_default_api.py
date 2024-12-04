# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictInt, StrictStr  # noqa: F401
from typing import Any, List  # noqa: F401
from openapi_server.models.meeting import Meeting  # noqa: F401
from openapi_server.models.person import Person  # noqa: F401
from openapi_server.models.student import Student  # noqa: F401
from openapi_server.models.teacher import Teacher  # noqa: F401


def test_auth_callback_google_get(client: TestClient):
    """Test case for auth_callback_google_get

    Google OAuth2 Callback
    """
    params = [("code", 'code_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/auth/callback/google",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_auth_login_google_get(client: TestClient):
    """Test case for auth_login_google_get

    Login via Google
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/auth/login/google",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_meetings_get(client: TestClient):
    """Test case for meetings_get

    Get a list of all meetings
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/meetings",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_meetings_post(client: TestClient):
    """Test case for meetings_post

    Create a new meeting
    """
    meeting = {"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/meetings",
    #    headers=headers,
    #    json=meeting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_meetings_schedule_google_calendar_post(client: TestClient):
    """Test case for meetings_schedule_google_calendar_post

    Schedule a meeting in Google Calendar
    """
    meeting = {"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/meetings/schedule-google-calendar",
    #    headers=headers,
    #    json=meeting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_persons_get(client: TestClient):
    """Test case for persons_get

    Get a list of all persons
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/persons",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_students_delete(client: TestClient):
    """Test case for students_delete

    Delete a student by ID
    """
    params = [("id", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/students",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_students_get(client: TestClient):
    """Test case for students_get

    Get a list of all students
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/students",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_students_post(client: TestClient):
    """Test case for students_post

    Create a new student
    """
    student = {"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"subjects_interested_in_learning":["subjects_interested_in_learning","subjects_interested_in_learning"],"meetings":[{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]},{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]}],"id":0,"email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/students",
    #    headers=headers,
    #    json=student,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_students_put(client: TestClient):
    """Test case for students_put

    Update student details
    """
    student = {"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"subjects_interested_in_learning":["subjects_interested_in_learning","subjects_interested_in_learning"],"meetings":[{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]},{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]}],"id":0,"email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/students",
    #    headers=headers,
    #    json=student,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_teachers_delete(client: TestClient):
    """Test case for teachers_delete

    Delete a teacher by ID
    """
    params = [("id", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/teachers",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_teachers_get(client: TestClient):
    """Test case for teachers_get

    Get a list of all teachers
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/teachers",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_teachers_post(client: TestClient):
    """Test case for teachers_post

    Create a new teacher
    """
    teacher = {"about_section":"about_section","phone":"phone","hourly_rate":6.0274563,"name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"subjects_to_teach":["subjects_to_teach","subjects_to_teach"],"meetings":[{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]},{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]}],"id":0,"email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/teachers",
    #    headers=headers,
    #    json=teacher,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_teachers_put(client: TestClient):
    """Test case for teachers_put

    Update teacher details
    """
    teacher = {"about_section":"about_section","phone":"phone","hourly_rate":6.0274563,"name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"subjects_to_teach":["subjects_to_teach","subjects_to_teach"],"meetings":[{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]},{"start_time":"2000-01-23T04:56:07.000+00:00","subject":"subject","location":"location","people":[{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"},{"about_section":"about_section","phone":"phone","name":"name","available":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"rating":4.5,"id":0,"email":"email"}],"finish_time":"2000-01-23T04:56:07.000+00:00","attached_files":["",""]}],"id":0,"email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/teachers",
    #    headers=headers,
    #    json=teacher,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

