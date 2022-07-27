class Student:
    """Student data class"""

    def __init__(
        self, name, student_id, age, subjects, grade, average_score, attendance=0
    ):
        """
        :param name: str
        :param student_id: int
        :param age: int
        :param subjects: list
        :param grade: string
        :param average_score: float
        :param attendance: int
        """
        self.name = name
        self.id = student_id
        self.age = age
        self.subjects = subjects
        self.grade = grade
        self.average_score = average_score
        self.attendance = attendance
