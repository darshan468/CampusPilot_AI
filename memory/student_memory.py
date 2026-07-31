from database.database import db_manager


class StudentMemory:

    @staticmethod
    def get_profile():

        return db_manager.get_student()

    @staticmethod
    def get_name():

        student = db_manager.get_student()

        if student:
            return student.name

        return "Student"

    @staticmethod
    def get_department():

        student = db_manager.get_student()

        if student:
            return student.department

        return ""

    @staticmethod
    def get_year():

        student = db_manager.get_student()

        if student:
            return student.year

        return ""

    @staticmethod
    def get_semester():

        student = db_manager.get_student()

        if student:
            return student.semester

        return ""

    @staticmethod
    def get_career_goal():

        student = db_manager.get_student()

        if student:
            return student.career_goal

        return ""

    @staticmethod
    def get_learning_style():

        student = db_manager.get_student()

        if student:
            return student.learning_style

        return ""

    @staticmethod
    def get_study_time():

        student = db_manager.get_student()

        if student:
            return student.preferred_study_time

        return ""