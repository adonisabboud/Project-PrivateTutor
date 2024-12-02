import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.meeting import Meeting  # noqa: E501
from openapi_server.models.person import Person  # noqa: E501
from openapi_server.models.student import Student  # noqa: E501
from openapi_server.models.teacher import Teacher  # noqa: E501
from openapi_server import util


def auth_callback_google_get(code):  # noqa: E501
    """Google OAuth2 Callback

    Handles the OAuth2 callback from Google and stores user information. # noqa: E501

    :param code: 
    :type code: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def auth_login_google_get():  # noqa: E501
    """Login via Google

    Redirects the user to Google&#39;s OAuth2 login page. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def meetings_get():  # noqa: E501
    """Get a list of all meetings

     # noqa: E501


    :rtype: Union[List[Meeting], Tuple[List[Meeting], int], Tuple[List[Meeting], int, Dict[str, str]]
    """
    return 'do some magic!'


def meetings_post(meeting):  # noqa: E501
    """Create a new meeting

    Schedule a meeting involving multiple participants. # noqa: E501

    :param meeting: 
    :type meeting: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        meeting = Meeting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def meetings_schedule_google_calendar_post(meeting):  # noqa: E501
    """Schedule a meeting in Google Calendar

    Creates a meeting and adds it to the user&#39;s Google Calendar. # noqa: E501

    :param meeting: 
    :type meeting: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        meeting = Meeting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def persons_get():  # noqa: E501
    """Get a list of all persons

     # noqa: E501


    :rtype: Union[List[Person], Tuple[List[Person], int], Tuple[List[Person], int, Dict[str, str]]
    """
    return 'do some magic!'


def students_delete(id):  # noqa: E501
    """Delete a student by ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def students_get():  # noqa: E501
    """Get a list of all students

     # noqa: E501


    :rtype: Union[List[Student], Tuple[List[Student], int], Tuple[List[Student], int, Dict[str, str]]
    """
    return 'do some magic!'


def students_post(student):  # noqa: E501
    """Create a new student

     # noqa: E501

    :param student: 
    :type student: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        student = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def students_put(student):  # noqa: E501
    """Update student details

     # noqa: E501

    :param student: 
    :type student: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        student = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def teachers_delete(id):  # noqa: E501
    """Delete a teacher by ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def teachers_get():  # noqa: E501
    """Get a list of all teachers

     # noqa: E501


    :rtype: Union[List[Teacher], Tuple[List[Teacher], int], Tuple[List[Teacher], int, Dict[str, str]]
    """
    return 'do some magic!'


def teachers_post(teacher):  # noqa: E501
    """Create a new teacher

     # noqa: E501

    :param teacher: 
    :type teacher: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        teacher = Teacher.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def teachers_put(teacher):  # noqa: E501
    """Update teacher details

     # noqa: E501

    :param teacher: 
    :type teacher: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        teacher = Teacher.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
