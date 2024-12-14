import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"  # Replace with your server's base URL

# Helper function to fetch data from an endpoint
def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data from {endpoint}: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return []

# Helper function to send data to an endpoint
def send_data(endpoint, data, method="POST"):
    try:
        if method == "POST":
            response = requests.post(f"{BASE_URL}{endpoint}", json=data)
        elif method == "PUT":
            response = requests.put(f"{BASE_URL}{endpoint}", json=data)
        elif method == "DELETE":
            response = requests.delete(f"{BASE_URL}{endpoint}", json=data)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            st.error(f"Failed to send data to {endpoint}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Error sending data: {str(e)}")
        return None



def send_data(endpoint, data, method="POST"):
    try:
        if method == "POST":
            response = requests.post(f"{BASE_URL}{endpoint}", json=data)
        elif method == "PUT":
            response = requests.put(f"{BASE_URL}{endpoint}", json=data)
        elif method == "DELETE":
            response = requests.delete(f"{BASE_URL}{endpoint}", json=data)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            st.error(f"Failed to send data to {endpoint}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Error sending data: {str(e)}")
        return None


def create_user(user_id, user_name, profile_type):
    """Create a new user in the system if they don't exist."""
    # Sample data to create a new user in the system
    user_data = {
        "user_id": user_id,
        "user_name": user_name,
        "profile_type": profile_type,
        "about_me": "",  # Optional, you can let the user fill it later
    }
    # Sending new user data to the backend (Replace with actual API endpoint)
    result = send_data("/create_user/", user_data, method="POST")
    if result:
        return True
    else:
        return False


def request_meeting_with_teacher(teacher_id):
    # Fetch teacher info by ID to check availability
    teacher = fetch_data(f"/teachers/{teacher_id}")

    if teacher:
        st.write(f"### Request a Meeting with {teacher.get('name')}")
        available_times = teacher.get('available_times', [])  # Assuming availability is a list of time slots

        if available_times:
            selected_time = st.selectbox("Choose a time", available_times)
            meeting_subject = st.text_input("Meeting Subject", help="Enter the subject of the meeting.")
            meeting_location = st.text_input("Meeting Location", help="Enter the meeting location.")

            # Button to send the meeting request
            if st.button("Request Meeting"):
                meeting_data = {
                    "teacher_id": teacher_id,
                    "start_time": selected_time,
                    "subject": meeting_subject,
                    "location": meeting_location,
                    "student_id": st.session_state.user_id,
                }
                result = send_data("/meetings/", meeting_data)
                if result:
                    st.success("Meeting request successfully sent!")
                else:
                    st.error("Failed to send meeting request. Please try again.")
    else:
        st.error("Teacher data not found. Please try again.")