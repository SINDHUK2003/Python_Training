from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional, Dict
from pydantic import BaseModel

app = FastAPI()

students = []


class Student(BaseModel):
    student_id: int
    name: str
    marks: Dict[str, int]


class UpdateMarks(BaseModel):
    marks: Dict[str, int]


class StudentGradeBook:

    def add_student(self, student: Student):
        for x in students:
            if x["student_id"] == student.student_id:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student already exists")
        students.append(student.dict())
        return student

    def get_student_by_name(self, name: str):
        for x in students:
            if x["name"].lower() == name.lower():
                return x
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )

    def update_marks(self, student_id: int, new_marks: Dict[str, int]):
        for x in students:
            if x["student_id"] == student_id:
                for sub, mark in new_marks.items():
                    if mark < 0:
                        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Marks cannot be negative")
                    x["marks"][sub] = mark
                return x
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    def delete_student(self, student_id: int):
        for x in students:
            if x["student_id"] == student_id:
                students.remove(x)
                return x
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    def class_average(self):
        if not students:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No students available")
        
        tot = 0
        cnt = 0
        for x in students:
            for mark in x["marks"].values():
                tot += mark
                cnt += 1

        return {"class_average": tot / cnt}

    def top_performers(self):
        if not students:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No students available")

        max_avg = -1
        toppers = []

        for x in students:
            avg = sum(x["marks"].values()) / len(x["marks"])
            if avg > max_avg:
                max_avg = avg
                toppers = [x]
            elif avg == max_avg:
                toppers.append(x)

        return {
            "top_performers": toppers,
            "average": max_avg
        }


gradebook = StudentGradeBook()


@app.get("/")
async def root():
    return {"message": "Student Grade Book API"}


@app.post("/students", status_code=status.HTTP_201_CREATED)
async def add_student(student: Student):
    return gradebook.add_student(student)


@app.get("/students/search")
async def get_student(name: Optional[str] = None):
    if not name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name parameter is required")
    return gradebook.get_student_by_name(name)


@app.put("/students/{student_id}")
async def update_student_marks(student_id: int = Path(..., gt=0), marks: UpdateMarks = None):
    if not marks:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Marks data required")
    return gradebook.update_marks(student_id, marks.marks)


@app.delete("/students/{student_id}")
async def delete_student(student_id: int = Path(..., gt=0)):
    deleted = gradebook.delete_student(student_id)
    return {
        "message": "Student deleted successfully",
        "student": deleted
    }


@app.get("/students/average")
async def class_average():
    return gradebook.class_average()


@app.get("/students/topper")
async def top_students():
    return gradebook.top_performers()
