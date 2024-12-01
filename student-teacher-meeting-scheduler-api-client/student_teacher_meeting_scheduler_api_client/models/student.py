import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting import Meeting


T = TypeVar("T", bound="Student")


@_attrs_define
class Student:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        phone (Union[Unset, str]):
        email (Union[Unset, str]):
        about_section (Union[Unset, str]):
        available (Union[Unset, List[datetime.datetime]]):
        rating (Union[Unset, float]): Average rating for the person, on a scale of 0 to 5. Example: 4.5.
        subjects_interested_in_learning (Union[Unset, List[str]]):
        meetings (Union[Unset, List['Meeting']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    about_section: Union[Unset, str] = UNSET
    available: Union[Unset, List[datetime.datetime]] = UNSET
    rating: Union[Unset, float] = UNSET
    subjects_interested_in_learning: Union[Unset, List[str]] = UNSET
    meetings: Union[Unset, List["Meeting"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        phone = self.phone

        email = self.email

        about_section = self.about_section

        available: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available, Unset):
            available = []
            for available_item_data in self.available:
                available_item = available_item_data.isoformat()
                available.append(available_item)

        rating = self.rating

        subjects_interested_in_learning: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subjects_interested_in_learning, Unset):
            subjects_interested_in_learning = self.subjects_interested_in_learning

        meetings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.meetings, Unset):
            meetings = []
            for meetings_item_data in self.meetings:
                meetings_item = meetings_item_data.to_dict()
                meetings.append(meetings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if about_section is not UNSET:
            field_dict["about_section"] = about_section
        if available is not UNSET:
            field_dict["available"] = available
        if rating is not UNSET:
            field_dict["rating"] = rating
        if subjects_interested_in_learning is not UNSET:
            field_dict["subjects_interested_in_learning"] = subjects_interested_in_learning
        if meetings is not UNSET:
            field_dict["meetings"] = meetings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meeting import Meeting

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        about_section = d.pop("about_section", UNSET)

        available = []
        _available = d.pop("available", UNSET)
        for available_item_data in _available or []:
            available_item = isoparse(available_item_data)

            available.append(available_item)

        rating = d.pop("rating", UNSET)

        subjects_interested_in_learning = cast(List[str], d.pop("subjects_interested_in_learning", UNSET))

        meetings = []
        _meetings = d.pop("meetings", UNSET)
        for meetings_item_data in _meetings or []:
            meetings_item = Meeting.from_dict(meetings_item_data)

            meetings.append(meetings_item)

        student = cls(
            id=id,
            name=name,
            phone=phone,
            email=email,
            about_section=about_section,
            available=available,
            rating=rating,
            subjects_interested_in_learning=subjects_interested_in_learning,
            meetings=meetings,
        )

        student.additional_properties = d
        return student

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
