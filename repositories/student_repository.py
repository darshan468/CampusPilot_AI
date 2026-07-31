class StudentRepository:
    """
    ==========================================================
    CampusPilot AI - Student Repository
    ==========================================================

    Responsibilities
    ----------------
    • Manage student database operations
    • Act as an abstraction layer between the
      service layer and the database
    """

    def __init__(self, database):
        self.database = database

    # ==========================================================
    # Student Operations
    # ==========================================================

    def get_student(self):

        try:
            return self.database.get_student()

        except Exception as e:
            raise RuntimeError(
                f"Failed to fetch student: {e}"
            )

    def save_student(self, student_data):

        try:
            return self.database.save_student(student_data)

        except Exception as e:
            raise RuntimeError(
                f"Failed to save student: {e}"
            )

    def update_student(self, student_data):

        try:
            return self.database.update_student(student_data)

        except Exception as e:
            raise RuntimeError(
                f"Failed to update student: {e}"
            )