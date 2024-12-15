from server_requests import *
import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def handle_meeting_actions(meeting_id, action):
    """
    Handle meeting actions like Cancel or Approve.

    Args:
        meeting_id (str): The ID of the meeting.
        action (str): The action to perform (e.g., "Approve", "Cancel").

    Returns:
        None
    """
    try:
        status = "Approved" if action == "Approve" else "Canceled"
        if send_data(f"/meetings/{meeting_id}", {"status": status}, method="PUT"):
            logger.info(f"Meeting {action}d: {meeting_id}")
            st.success(f"Meeting {action}d successfully.")
        else:
            logger.error(f"Failed to {action} meeting: {meeting_id}")
            st.error(f"Failed to {action} the meeting.")
    except Exception as e:
        logger.exception(f"Error performing action '{action}' for meeting {meeting_id}")
        st.error(f"An error occurred while trying to {action} the meeting. Please try again.")

def teacher_view():
    """Teacher Dashboard."""
    logger.info("Loading Teacher Dashboard.")
    st.subheader("Teacher Dashboard")
    options = ["Manage Meetings", "Edit Availability", "Edit Profile"]
    choice = st.sidebar.radio("Menu", options)

    if choice == "Manage Meetings":
        st.subheader("Your Meetings")
        try:
            teacher_meetings = get_my_meetings(st.session_state.user_id)
            if teacher_meetings:
                for meeting in teacher_meetings:
                    st.write(f"**Subject:** {meeting.get('topic', 'N/A')}")
                    st.write(f"**Student:** {meeting.get('student_name', 'N/A')}")
                    st.write(f"**Scheduled Time:** {meeting.get('scheduled_time', 'N/A')}")
                    action = st.radio(f"Actions for {meeting.get('topic')}", ["Approve", "Cancel"], key=meeting.get('id'))
                    if st.button(f"{action} Meeting: {meeting.get('topic')}", key=f"{action}_{meeting['id']}"):
                        handle_meeting_actions(meeting.get('id'), action)
                    st.write("---")
            else:
                logger.info("No meetings found for teacher.")
                st.info("No meetings found.")
        except Exception as e:
            logger.exception("Error loading meetings for teacher.")
            st.error("Failed to load meetings. Please try again later.")

    elif choice == "Edit Availability":
        st.subheader("Edit Your Availability")
        availability = st.text_area("Enter your availability (e.g., Monday 9-12 AM)")
        if st.button("Save Availability"):
            try:
                if send_data(f"/users/{st.session_state.user_id}/availability", {"availability": availability}, method="PUT"):
                    logger.info(f"Availability updated for user {st.session_state.user_id}")
                    st.success("Availability updated successfully!")
                else:
                    logger.error(f"Failed to update availability for user {st.session_state.user_id}")
                    st.error("Failed to update availability. Please try again.")
            except Exception as e:
                logger.exception("Error updating availability.")
                st.error("An error occurred while updating availability. Please try again later.")

    elif choice == "Edit Profile":
        st.subheader("Edit Your Profile")
        about_section = st.text_area("About Me", placeholder="Write about yourself...")
        if st.button("Update Profile"):
            try:
                if send_data(f"/users/{st.session_state.user_id}", {"about_section": about_section}, method="PUT"):
                    logger.info(f"Profile updated for user {st.session_state.user_id}")
                    st.success("Profile updated successfully!")
                else:
                    logger.error(f"Failed to update profile for user {st.session_state.user_id}")
                    st.error("Failed to update profile. Please try again.")
            except Exception as e:
                logger.exception("Error updating profile.")
                st.error("An error occurred while updating your profile. Please try again later.")

def student_view():
    """Student Dashboard."""
    logger.info("Loading Student Dashboard.")
    st.subheader("Student Dashboard")
    options = ["Available Teachers", "My Meetings", "Edit Profile"]
    choice = st.sidebar.radio("Menu", options)

    if choice == "Available Teachers":
        st.subheader("Available Teachers")
        try:
            teachers = fetch_data("/teachers/")
            if teachers:
                for teacher in teachers:
                    st.write(f"**Name:** {teacher.get('name', 'N/A')}")
                    st.write(f"**Subjects:** {', '.join(teacher.get('subjects', []))}")
                    if st.button(f"Request Meeting with {teacher.get('name')}", key=teacher.get("id")):
                        logger.info(f"Requesting meeting with teacher {teacher.get('id')}")
                        request_meeting_with_teacher(teacher.get("id"))
                    st.write("---")
            else:
                logger.info("No teachers found.")
                st.info("No teachers found.")
        except Exception as e:
            logger.exception("Error fetching teachers.")
            st.error("Failed to load teacher data. Please try again later.")

    elif choice == "My Meetings":
        st.subheader("Your Meetings")
        try:
            student_meetings = get_my_meetings(st.session_state.user_id)
            if student_meetings:
                for meeting in student_meetings:
                    st.write(f"**Subject:** {meeting.get('topic', 'N/A')}")
                    st.write(f"**Teacher:** {meeting.get('teacher_name', 'N/A')}")
                    st.write(f"**Scheduled Time:** {meeting.get('scheduled_time', 'N/A')}")
                    if st.button(f"Cancel Meeting: {meeting.get('topic')}", key=meeting.get('id')):
                        handle_meeting_actions(meeting.get('id'), "Cancel")
                    st.write("---")
            else:
                logger.info("No meetings found for student.")
                st.info("No meetings found.")
        except Exception as e:
            logger.exception("Error fetching meetings for student.")
            st.error("Failed to load meetings. Please try again later.")

    elif choice == "Edit Profile":
        st.subheader("Edit Your Profile")
        about_section = st.text_area("About Me", placeholder="Write about yourself...")
        if st.button("Update Profile"):
            try:
                if send_data(f"/users/{st.session_state.user_id}", {"about_section": about_section}, method="PUT"):
                    logger.info(f"Profile updated for user {st.session_state.user_id}")
                    st.success("Profile updated successfully!")
                else:
                    logger.error(f"Failed to update profile for user {st.session_state.user_id}")
                    st.error("Failed to update profile. Please try again.")
            except Exception as e:
                logger.exception("Error updating profile.")
                st.error("An error occurred while updating your profile. Please try again later.")
