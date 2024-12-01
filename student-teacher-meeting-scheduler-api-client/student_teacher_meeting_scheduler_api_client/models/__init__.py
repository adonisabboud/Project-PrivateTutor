"""Contains all the data models used in inputs/outputs"""

from .meeting import Meeting
from .person import Person
from .student import Student
from .teacher import Teacher

__all__ = (
    "Meeting",
    "Person",
    "Student",
    "Teacher",
)
