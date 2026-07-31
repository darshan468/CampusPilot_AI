class StudyRepository:
    """
    CampusPilot AI - Study Repository
    """

    def __init__(self, database):
        self.database = database

    def save_plan(self, plan):
        try:
            return self.database.save_study_plan(plan)
        except Exception as e:
            raise RuntimeError(f"Failed to save study plan: {e}")

    def get_plans(self):
        try:
            return self.database.get_study_plans()
        except Exception as e:
            raise RuntimeError(f"Failed to fetch study plans: {e}")

    def delete_plan(self, plan_id):
        try:
            return self.database.delete_study_plan(plan_id)
        except Exception as e:
            raise RuntimeError(f"Failed to delete study plan: {e}")