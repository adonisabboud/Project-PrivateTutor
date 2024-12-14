import streamlit as st
import datetime
import random

from server_requests import *  # Assuming this imports the functions like fetch_data and send_data


def main():
    # Try to get user ID if the user is logging in
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None

    st.title("Meeting Scheduler")

    # Check if the user wants to log in or create a new profile
    user_id_input = st.text_input("Enter Your ID (if you have one)", help="Enter your ID to log in to your existing profile.")
    login_button = st.button("Login")

    # Login action: Fetch the user profile by ID
    if login_button:
        user_profile = fetch_data(f"/users/{user_id_input}")
        if user_profile:
            st.session_state.user_id = user_id_input
            st.success(f"Welcome back! You are logged in with ID: {st.session_state.user_id}")
            st.write("You can now proceed to access your profile.")
        else:
            st.error("User ID not found. Please create a new profile.")

    # If no login, allow the user to create a new profile
    if not st.session_state.user_id:
        # Auto-generate user ID for new users
        st.session_state.user_id = str(random.randint(1000, 9999)) + str(int(datetime.datetime.now().timestamp()))

        # Create profile
        create_button = st.button("Create New Profile")
        if create_button:
            # Collect user details for profile creation
            user_name = st.text_input("Enter Your Name", help="Enter your full name.")
            profile_type = st.radio("Select Profile", ["Student", "Teacher"], key="profile_toggle")

            # Call create_user function to create a new profile
            if create_user(st.session_state.user_id, user_name, profile_type):
                st.success(f"New profile created! Your User ID is: {st.session_state.user_id}")
                st.warning("Please save your User ID. You'll need it next time to access your profile.")
                st.write("You are now registered as a new user. Please remember your ID for future logins.")

    # Display the user ID always at the top of the page
    st.write(f"### Your User ID: {st.session_state.user_id}")

    # Simple profile toggle at the top
    profile_type = st.radio("Select Your Profile", ["Student", "Teacher"], key="profile_toggle")

    # Change the color based on the profile selected
    if profile_type == "Student":
        st.markdown(
            """
            <style>
                .main {
                    background-color: #E0F7FA;  /* Light Cyan for Student */
                }
                .stButton>button {
                    background-color: #00BCD4;
                    color: white;
                    font-weight: bold;
                }
            </style>
            """, unsafe_allow_html=True
        )
    elif profile_type == "Teacher":
        st.markdown(
            """
            <style>
                .main {
                    background-color: #E8F5E9;  /* Light Green for Teacher */
                }
                .stButton>button {
                    background-color: #388E3C;
                    color: white;
                    font-weight: bold;
                }
            </style>
            """, unsafe_allow_html=True
        )

    # Handle different views for student or teacher profile
    if profile_type == "Student":
        student_menu = ["View Teachers", "Request a Meeting", "Manage Meetings"]
        choice = st.sidebar.selectbox("Select an Option", student_menu)

        if choice == "View Teachers":
            st.subheader("Browse Teachers")
            teachers = fetch_data("/teachers/")
            if teachers:
                for teacher in teachers:
                    st.write(f"**Name:** {teacher.get('name', 'N/A')}")
                    st.write(f"**Subjects:** {', '.join(teacher.get('subjects', []))}")
                    st.write(f"**Email:** {teacher.get('email', 'N/A')}")
                    teacher_id = teacher.get("id")
                    # Button to request a meeting
                    if st.button(f"Request Meeting with {teacher.get('name')}", key=teacher_id):
                        request_meeting_with_teacher(teacher_id)
                    st.write("---")
            else:
                st.error("Failed to load teachers data. Please try again later.")

        elif choice == "Request a Meeting":
            st.subheader("Request a Meeting with a Teacher")

            teachers = fetch_data("/teachers/")
            teacher_names = [teacher.get('name') for teacher in teachers]

            meeting_subject = st.text_input("Meeting Subject", help="Enter the subject of the meeting.")
            meeting_location = st.text_input("Meeting Location", help="Enter the meeting location.")

            # Split datetime input into separate date and time inputs
            start_date = st.date_input("Start Date", datetime.date.today())
            start_time = st.time_input("Start Time", datetime.time(9, 0))  # Default time 09:00 AM
            end_date = st.date_input("End Date", datetime.date.today())
            end_time = st.time_input("End Time", datetime.time(10, 0))  # Default time 10:00 AM

            selected_teacher = st.selectbox("Select a Teacher", teacher_names)
            attached_files = st.file_uploader("Upload Files (Optional)", accept_multiple_files=True)

            # Combine date and time for start and end times
            start_datetime = datetime.datetime.combine(start_date, start_time)
            end_datetime = datetime.datetime.combine(end_date, end_time)

            # Ensure that start time is before end time
            if start_datetime >= end_datetime:
                st.error("Start time must be before end time.")
            else:
                if st.button("Send Meeting Request"):
                    teacher = next((t for t in teachers if t.get('name') == selected_teacher), None)
                    if teacher:
                        files_metadata = [{"file_name": file.name, "file_type": file.type} for file in attached_files]

                        meeting_data = {
                            "location": meeting_location,
                            "start_time": start_datetime.isoformat(),
                            "finish_time": end_datetime.isoformat(),
                            "subject": meeting_subject,
                            "people": [{"name": teacher['name'], "role": "Teacher"}],
                            "attached_files": files_metadata,
                        }

                        result = send_data("/meetings/", meeting_data)
                        if result:
                            st.success("Your meeting request has been successfully sent!")
                        else:
                            st.error("Failed to send meeting request. Please try again later.")

        elif choice == "Manage Meetings":
            st.subheader("Your Meetings")

            meetings = fetch_data("/meetings/")
            student_name = st.text_input("Enter Your Name to Filter Meetings")

            if student_name and meetings:
                student_meetings = [
                    meeting for meeting in meetings if
                    any(p.get("name") == student_name for p in meeting.get("people", []))
                ]

                for meeting in student_meetings:
                    st.write(f"**Subject:** {meeting.get('subject', 'N/A')}")
                    st.write(f"**Location:** {meeting.get('location', 'N/A')}")
                    st.write(f"**Start Time:** {meeting.get('start_time', 'N/A')}")
                    st.write(f"**End Time:** {meeting.get('finish_time', 'N/A')}")
                    st.write("---")

                    if 'id' in meeting:
                        action = st.radio(f"Actions for {meeting.get('subject')}", ["Cancel"])
                        if action == "Cancel" and st.button(f"Cancel Meeting: {meeting.get('subject')}", key=meeting['id']):
                            update_result = send_data(f"/meetings/{meeting['id']}", {"status": "Canceled"}, method="PUT")
                            if update_result:
                                st.success(f"The meeting {meeting.get('subject')} has been canceled.")
                        else:
                            st.warning("Unable to perform action.")

    elif profile_type == "Teacher":
        teacher_menu = ["Manage Your Meetings", "View Students", "About Me"]
        choice = st.sidebar.selectbox("Select an Option", teacher_menu)

        if choice == "Manage Your Meetings":
            st.subheader("Your Meetings")

            meetings = fetch_data("/meetings/")
            teacher_name = st.text_input("Enter Your Name to Filter Meetings")

            if teacher_name and meetings:
                teacher_meetings = [
                    meeting for meeting in meetings if
                    any(p.get("name") == teacher_name for p in meeting.get("people", []))
                ]

                for meeting in teacher_meetings:
                    st.write(f"**Subject:** {meeting.get('subject', 'N/A')}")
                    st.write(f"**Location:** {meeting.get('location', 'N/A')}")
                    st.write(f"**Start Time:** {meeting.get('start_time', 'N/A')}")
                    st.write(f"**End Time:** {meeting.get('finish_time', 'N/A')}")
                    st.write("---")

                    if 'id' in meeting:
                        action = st.radio(f"Actions for {meeting.get('subject')}", ["Approve", "Deny", "Cancel"])
                        if action == "Cancel" and st.button(f"Cancel Meeting: {meeting.get('subject')}", key=meeting['id']):
                            update_result = send_data(f"/meetings/{meeting['id']}", {"status": "Canceled"}, method="PUT")
                            if update_result:
                                st.success(f"The meeting {meeting.get('subject')} has been canceled.")
                        elif action == "Approve" and st.button(f"Approve Meeting: {meeting.get('subject')}", key=meeting['id']):
                            update_result = send_data(f"/meetings/{meeting['id']}", {"status": "Approved"}, method="PUT")
                            if update_result:
                                st.success(f"The meeting {meeting.get('subject')} has been approved.")
                        elif action == "Deny" and st.button(f"Deny Meeting: {meeting.get('subject')}", key=meeting['id']):
                            update_result = send_data(f"/meetings/{meeting['id']}", {"status": "Denied"}, method="PUT")
                            if update_result:
                                st.success(f"The meeting {meeting.get('subject')} has been denied.")

        elif choice == "View Students":
            st.subheader("All Students")
            students = fetch_data("/students/")

            if students:
                for student in students:
                    st.write(f"**Name:** {student.get('name', 'N/A')}")
                    st.write(f"**Email:** {student.get('email', 'N/A')}")
                    st.write("---")

        elif choice == "About Me":
            st.subheader("Update Your Profile")
            about_me = st.text_area("About Me", "Write a brief description of yourself...")

            if st.button("Update Profile"):
                updated_profile_data = {
                    "name": user_name,
                    "id": st.session_state.user_id,
                    "profile_type": profile_type,
                    "about_me": about_me,
                }

                result = send_data("/update_profile/", updated_profile_data, method="PUT")
                if result:
                    st.success("Profile updated successfully!")
if __name__ == "__main__":
    main()
