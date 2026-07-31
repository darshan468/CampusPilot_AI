class AssignmentRepository:
    """
    CampusPilot AI - Assignment Repository
    """

    def __init__(self, database):
        self.database = database

    def save_assignment(self, assignment):
        try:
            return self.database.save_assignment(assignment)
        except Exception as e:
            raise RuntimeError(f"Failed to save assignment: {e}")

    def get_assignments(self):
        try:
            return self.database.get_assignments()
        except Exception as e:
            raise RuntimeError(f"Failed to fetch assignments: {e}")

    def delete_assignment(self, assignment_id):
        try:
            return self.database.delete_assignment(assignment_id)
        except Exception as e:
            raise RuntimeError(f"Failed to delete assignment: {e}")