import unittest
from fastapi.testclient import TestClient
from server.openapi_server.__main__ import app

client = TestClient(app)

class TestMeetingsEndpoints(unittest.TestCase):
    def setUp(self):
        """Setup for each test method to initialize a test meeting."""
        self.test_meeting_payload = {
            "location": "Conference Room 1",
            "start_time": "2024-12-15T10:00:00Z",
            "finish_time": "2024-12-15T11:00:00Z",
            "subject": "Project Discussion",
            # Each person might need to be a dictionary with more details
            "people": [
                {"name": "Person A", "role": "Attendee"},
                {"name": "Person B", "role": "Attendee"}
            ],
            # Each file might also need to be a dictionary specifying more than just a filename
            "attached_files": [
                {"filename": "file1.pdf", "filetype": "PDF"},
                {"filename": "file2.doc", "filetype": "Document"}
            ]
        }
        response = client.post("/meetings/", json=self.test_meeting_payload)
        if response.status_code != 200:
            print("Failed to create meeting:", response.json())
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """Clean up after each test by removing the test meeting."""
        client.delete(f"/meetings/{self.meeting_id}")

    def test_get_all_meetings(self):
        """Test GET /meetings/ endpoint to retrieve all meetings."""
        response = client.get("/meetings/")
        self.assertEqual(response.status_code, 200)
        meetings = response.json()
        self.assertIsInstance(meetings, list)
        self.assertTrue(any(meeting["location"] == self.test_meeting_payload["location"] for meeting in meetings))

    def test_create_meeting(self):
        """Test POST /meetings/ endpoint to create a new meeting."""
        new_meeting_payload = {
            "location": "Conference Room 2",
            "start_time": "2024-12-16T10:00:00Z",
            "finish_time": "2024-12-16T11:00:00Z",
            "subject": "Budget Review",
            "people": ["Person C", "Person D"],
            "attached_files": ["budget.xlsx"]
        }
        response = client.post("/meetings/", json=new_meeting_payload)
        self.assertEqual(response.status_code, 200)
        meeting_response = response.json()
        self.assertIn("id", meeting_response)
        self.assertEqual(meeting_response["message"], "Meeting created successfully")

    def test_update_meeting(self):
        """Test PUT /meetings/{id} endpoint to update a meeting."""
        update_payload = {
            "location": "Updated Location",
            "start_time": "2024-12-15T12:00:00Z",
            "finish_time": "2024-12-15T13:00:00Z",
            "subject": "Updated Discussion",
            "people": ["Person E", "Person F"],
            "attached_files": ["updated_file.pdf"]
        }
        response = client.put(f"/meetings/{self.meeting_id}", json=update_payload)
        self.assertEqual(response.status_code, 200)
        updated_response = response.json()
        self.assertEqual(updated_response["message"], "Meeting updated successfully")

    def test_delete_meeting(self):
        """Test DELETE /meetings/{id} endpoint to delete a meeting."""
        response = client.delete(f"/meetings/{self.meeting_id}")
        self.assertEqual(response.status_code, 200)
        delete_response = response.json()
        self.assertEqual(delete_response["message"], "Meeting deleted successfully")

    def test_get_meeting_by_id(self):
        """Test GET /meetings/{id} endpoint to retrieve a specific meeting by ID."""
        response = client.get(f"/meetings/{self.meeting_id}")
        self.assertEqual(response.status_code, 200)
        meeting = response.json()
        self.assertEqual(meeting["location"], self.test_meeting_payload["location"])
        self.assertEqual(meeting["subject"], self.test_meeting_payload["subject"])

if __name__ == '__main__':
    unittest.main()
