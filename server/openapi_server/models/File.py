import datetime
from typing import Optional


class File:
    def __init__(self, file_name: str, file_type: str, file_path: Optional[str] = None,
                 file_content: Optional[bytes] = None, owner_id: Optional[int] = None,
                 upload_date: Optional[datetime.datetime] = None):
        """
        Initializes a new File object with metadata and content.

        :param file_name: The name of the file.
        :param file_type: The MIME type of the file.
        :param file_path: The path to the file on disk or in storage (optional).
        :param file_content: Binary content of the file (optional, for in-memory files).
        :param owner_id: The ID of the user who owns or uploaded the file (optional).
        :param upload_date: The date and time when the file was uploaded (optional, defaults to now).
        """
        self.file_name = file_name
        self.file_type = file_type
        self.file_path = file_path
        self.file_content = file_content
        self.owner_id = owner_id
        self.upload_date = upload_date if upload_date else datetime.datetime.now()

    def to_dict(self):
        """
        Serializes the File object to a dictionary.
        """
        return {
            'file_name': self.file_name,
            'file_type': self.file_type,
            'file_path': self.file_path,
            'file_content': self.file_content,  # Be cautious with large binary data
            'owner_id': self.owner_id,
            'upload_date': self.upload_date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        """
        Deserializes a dictionary into a File object.
        """
        return cls(
            file_name=data['file_name'],
            file_type=data['file_type'],
            file_path=data.get('file_path'),
            file_content=data.get('file_content'),
            owner_id=data.get('owner_id'),
            upload_date=datetime.datetime.fromisoformat(data['upload_date'])
        )

    def __str__(self):
        """
        String representation of the File object.
        """
        return f"File(name={self.file_name}, type={self.file_type}, owner={self.owner_id}, upload_date={self.upload_date})"
