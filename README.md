# Project-PrivateTutor
The plan is to have 3 UI - frontEnd and a Server, to manage the whole things via API requests
![image](https://github.com/user-attachments/assets/0a72ce9e-4136-4b5a-9562-0ee74bc018be)

# 
___

#


# API

The **Student-Teacher Meeting Scheduler API** provides an interface for managing users (students and teachers), authenticating them, and scheduling meetings between them. This documentation outlines the available endpoints and how to use them.

---

## Table of Contents
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Overview](#api-overview)
- [Endpoints](#endpoints)
  - [User Endpoints](#user-endpoints)
  - [Teacher Endpoints](#teacher-endpoints)
  - [Student Endpoints](#student-endpoints)
  - [Meeting Endpoints](#meeting-endpoints)
- [Error Handling](#error-handling)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/student-teacher-api.git
   cd student-teacher-api
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file with the following keys:
   ```
   DB_USER=<your_db_user>
   DB_PASSWORD=<your_db_password>
   DB_CLUSTER=<your_cluster_url>
   DB_NAME=<your_db_name>
   ```

5. **Run the database migrations if necessary.**

---

## Running the Server

To run the server with auto-reload enabled:
```bash
uvicorn server.main:app --host 0.0.0.0 --port 8080 --reload
```

---

## API Overview

### User Management
- Register and authenticate users, returning a unique `user_id`.
- CRUD operations for user data.

### Teacher Management
- List all teachers or retrieve details by `teacher_id`.

### Student Management
- List all students or retrieve details by `student_id`.

### Meeting Management
- Schedule, manage, and delete meetings between students and teachers.

---

## Endpoints

### User Endpoints

| Method | Endpoint                 | Description                              |
|--------|--------------------------|------------------------------------------|
| `POST` | `/users`                 | Create a new user.                       |
| `POST` | `/users/authenticate`    | Authenticate a user and return `user_id`.|
| `GET`  | `/users/{username}`      | Retrieve user details by `username`.     |
| `GET`  | `/users/id/{user_id}`    | Retrieve user details by `user_id`.      |
| `PUT`  | `/users/{user_id}`       | Update user details.                     |
| `DELETE` | `/users/{user_id}`     | Delete a user.                           |

---

### Teacher Endpoints

| Method | Endpoint                 | Description                              |
|--------|--------------------------|------------------------------------------|
| `GET`  | `/teachers`              | List all teachers.                       |
| `GET`  | `/teachers/{id}`         | Retrieve teacher details by ID.          |
| `POST` | `/teachers`              | Create a new teacher.                    |
| `PUT`  | `/teachers/{id}`         | Update teacher details.                  |
| `DELETE` | `/teachers/{id}`       | Delete a teacher by ID.                  |

---

### Student Endpoints

| Method | Endpoint               | Description                              |
|--------|------------------------|------------------------------------------|
| `GET`  | `/students`            | List all students.                       |
| `GET`  | `/students/{id}`       | Retrieve student details by ID.          |
| `POST` | `/students`            | Create a new student.                    |
| `PUT`  | `/students/{id}`       | Update student details.                  |
| `DELETE` | `/students/{id}`     | Delete a student by ID.                  |

---

### Meeting Endpoints

| Method | Endpoint               | Description                              |
|--------|------------------------|------------------------------------------|
| `GET`  | `/meetings`            | List all meetings.                      |
| `GET`  | `/meetings/{id}`       | Retrieve meeting details by ID.         |
| `POST` | `/meetings`            | Create a new meeting.                   |
| `PUT`  | `/meetings/{id}`       | Update meeting details.                 |
| `DELETE`| `/meetings/{id}`      | Delete a meeting by ID.                 |

---

## Example Requests

### User Endpoints

**1. Register a New User**
```http
POST /users
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john.doe@example.com",
  "password": "securepassword",
  "roles": ["student"],
  "name": "John Doe"
}
```

**2. Authenticate a User**
```http
POST /users/authenticate
Content-Type: application/json

{
  "username": "john_doe",
  "password": "securepassword"
}
```

**3. Get User by ID**
```http
GET /users/id/64cbbd3e45a3a7f89098a12b
```

**4. Update a User**
```http
PUT /users/64cbbd3e45a3a7f89098a12b
Content-Type: application/json

{
  "about_section": "Updated about section"
}
```

### Meeting Endpoints

**1. Create a Meeting**
```http
POST /meetings
Content-Type: application/json

{
  "student_id": "64cbbd3e45a3a7f89098a12b",
  "teacher_id": "64cbbd3e45a3a7f89098b45c",
  "topic": "Math Tutoring",
  "scheduled_time": "2024-12-18T10:30:00"
}
```

**2. Get a Meeting by ID**
```http
GET /meetings/64cbbea945a3a7f89098c67d
```

---

## Error Handling

- **400 Bad Request:** Invalid input or missing fields.
- **401 Unauthorized:** Authentication failed.
- **404 Not Found:** Resource not found.
- **500 Internal Server Error:** Unexpected server-side issue.

---

Let me know if you need further adjustments or clarifications!