import datetime
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.person import Person


T = TypeVar("T", bound="Meeting")


@_attrs_define
class Meeting:
    """
    Attributes:
        location (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]):
        finish_time (Union[Unset, datetime.datetime]):
        subject (Union[Unset, str]):
        people (Union[Unset, List['Person']]):
        attached_files (Union[Unset, List[File]]):
    """

    location: Union[Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    finish_time: Union[Unset, datetime.datetime] = UNSET
    subject: Union[Unset, str] = UNSET
    people: Union[Unset, List["Person"]] = UNSET
    attached_files: Union[Unset, List[File]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        finish_time: Union[Unset, str] = UNSET
        if not isinstance(self.finish_time, Unset):
            finish_time = self.finish_time.isoformat()

        subject = self.subject

        people: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.people, Unset):
            people = []
            for people_item_data in self.people:
                people_item = people_item_data.to_dict()
                people.append(people_item)

        attached_files: Union[Unset, List[FileJsonType]] = UNSET
        if not isinstance(self.attached_files, Unset):
            attached_files = []
            for attached_files_item_data in self.attached_files:
                attached_files_item = attached_files_item_data.to_tuple()

                attached_files.append(attached_files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if finish_time is not UNSET:
            field_dict["finish_time"] = finish_time
        if subject is not UNSET:
            field_dict["subject"] = subject
        if people is not UNSET:
            field_dict["people"] = people
        if attached_files is not UNSET:
            field_dict["attached_files"] = attached_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person import Person

        d = src_dict.copy()
        location = d.pop("location", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _finish_time = d.pop("finish_time", UNSET)
        finish_time: Union[Unset, datetime.datetime]
        if isinstance(_finish_time, Unset):
            finish_time = UNSET
        else:
            finish_time = isoparse(_finish_time)

        subject = d.pop("subject", UNSET)

        people = []
        _people = d.pop("people", UNSET)
        for people_item_data in _people or []:
            people_item = Person.from_dict(people_item_data)

            people.append(people_item)

        attached_files = []
        _attached_files = d.pop("attached_files", UNSET)
        for attached_files_item_data in _attached_files or []:
            attached_files_item = File(payload=BytesIO(attached_files_item_data))

            attached_files.append(attached_files_item)

        meeting = cls(
            location=location,
            start_time=start_time,
            finish_time=finish_time,
            subject=subject,
            people=people,
            attached_files=attached_files,
        )

        meeting.additional_properties = d
        return meeting

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
