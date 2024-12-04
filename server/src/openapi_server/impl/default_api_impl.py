from openapi_server.models.person import Person
from openapi_server.models.student import Student
from openapi_server.models.teacher import Teacher
from fastapi import HTTPException


# Simulated databases
PERSONS_DB = [
    Person(id=1, name="John Doe", email="john.doe@example.com", phone="1234567890"),
    Person(id=2, name="Jane Smith", email="jane.smith@example.com", phone="0987654321"),
]

STUDENTS_DB = [
    Student(id=1, name="Alice", email="alice@example.com", phone="1111111111",
            subjects_interested_in_learning=["Math", "Science"]),
    Student(id=2, name="Bob", email="bob@example.com", phone="2222222222",
            subjects_interested_in_learning=["History", "Literature"]),
]

TEACHERS_DB = []


class DefaultApiImpl:
    # Implement /persons
    async def persons_get(self):
        """Return the list of persons."""
        return PERSONS_DB

    # Implement /students
    async def students_get(self):
        """Return the list of students."""
        return STUDENTS_DB

    async def teachers_get(self):
        """Get a list of all teachers."""
        return TEACHERS_DB
    async def persons_delete(self, id: int):
        """Delete a person by ID."""
        global PERSONS_DB
        for person in PERSONS_DB:
            if person.id == id:
                PERSONS_DB.remove(person)
                return {"message": f"Person with id {id} deleted successfully"}
        raise HTTPException(status_code=404, detail="Person not found")


    async def students_delete(self, id: int):
        """Delete a student by ID."""
        global STUDENTS_DB
        for student in STUDENTS_DB:
            if student.id == id:
                STUDENTS_DB.remove(student)
                return {"message": f"Student with id {id} deleted successfully"}
        raise HTTPException(status_code=404, detail="Student not found")

    async def teachers_delete(self, id: int):
        """Delete a teacher by ID."""
        global TEACHERS_DB
        for teacher in TEACHERS_DB:
            if teacher.id == id:
                TEACHERS_DB.remove(teacher)
                return
        raise HTTPException(status_code=404, detail="Teacher not found")

    async def persons_post(self, person: Person):
        """Add a new person."""
        if not person.name or not person.email:
            raise HTTPException(status_code=400, detail="Name and Email are required.")
        global PERSONS_DB
        person.id = len(PERSONS_DB) + 1  # Simulate auto-increment ID
        PERSONS_DB.append(person)

    async def students_post(self, student: Student):
        """Add a new student."""
        if not student.name or not student.email:
            raise HTTPException(status_code=400, detail="Name and Email are required.")
        global STUDENTS_DB
        student.id = len(STUDENTS_DB) + 1  # Simulate auto-increment ID
        STUDENTS_DB.append(student)

    async def teachers_post(self, teacher: Teacher):
        """Add a new teacher."""
        if not teacher.name or not teacher.email:
            raise HTTPException(status_code=400, detail="Name and Email are required.")
        global TEACHERS_DB
        teacher.id = len(TEACHERS_DB) + 1  # Simulate auto-increment ID
        TEACHERS_DB.append(teacher)

    async def persons_put(self, person: Person):
        """Update an existing person's details."""
        global PERSONS_DB
        for existing_person in PERSONS_DB:
            if existing_person.id == person.id:
                # Update all fields in the Person model
                existing_person.name = person.name
                existing_person.email = person.email
                existing_person.phone = person.phone
                existing_person.about_section = person.about_section
                existing_person.available = person.available
                existing_person.rating = person.rating
                return
        raise HTTPException(status_code=404, detail="Person not found")

    async def students_put(self, student: Student):
        """Update an existing student's details."""
        global STUDENTS_DB
        for existing_student in STUDENTS_DB:
            if existing_student.id == student.id:
                # Update all fields in the Student model
                existing_student.name = student.name
                existing_student.email = student.email
                existing_student.phone = student.phone
                existing_student.about_section = student.about_section
                existing_student.available = student.available
                existing_student.rating = student.rating
                existing_student.subjects_interested_in_learning = student.subjects_interested_in_learning
                existing_student.meetings = student.meetings
                return {"message": f"Student with id {student.id} updated successfully"}
        raise HTTPException(status_code=404, detail="Student not found")
    async def teachers_put(self, teacher: Teacher):
        """Update an existing teacher's details."""
        global TEACHERS_DB
        for existing_teacher in TEACHERS_DB:
            if existing_teacher.id == teacher.id:
                # Update all fields in the Teacher model
                existing_teacher.name = teacher.name
                existing_teacher.email = teacher.email
                existing_teacher.phone = teacher.phone
                existing_teacher.about_section = teacher.about_section
                existing_teacher.available = teacher.available
                existing_teacher.rating = teacher.rating
                existing_teacher.subjects_to_teach = teacher.subjects_to_teach
                existing_teacher.hourly_rate = teacher.hourly_rate
                existing_teacher.meetings = teacher.meetings
                return {"message": f"Teacher with id {teacher.id} updated successfully"}
        raise HTTPException(status_code=404, detail="Teacher not found")

