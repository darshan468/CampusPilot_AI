from database.database import DatabaseManager


class DatabaseService:
    """
    ==========================================================
    CampusPilot AI - Database Service
    ==========================================================
    Service Layer between Repository and Database
    ==========================================================
    """

    def __init__(self):
        self.db = DatabaseManager()

    # ==========================================================
    # Student
    # ==========================================================

    def get_student(self, student_id):
        return self.db.get_student(student_id)

    def save_student(self, student_data):
        return self.db.save_student(student_data)

    def update_student(self, student_data):
        return self.db.update_student(student_data)

    # ==========================================================
    # Study Planner
    # ==========================================================

    def save_study_plan(self, plan):
        return self.db.save_study_plan(plan)

    def get_study_plans(self, student_id=None):
        if hasattr(self.db, "get_study_plans"):
            return self.db.get_study_plans(student_id)

        return self.db.get_all_study_plans()

    def delete_study_plan(self, plan_id):
        if hasattr(self.db, "delete_study_plan"):
            return self.db.delete_study_plan(plan_id)

        return None

    # ==========================================================
    # Assignment
    # ==========================================================

    def save_assignment(self, assignment):
        return self.db.save_assignment(assignment)

    def get_assignments(self, student_id=None):
        if hasattr(self.db, "get_assignments"):
            return self.db.get_assignments(student_id)

        return self.db.get_all_assignments()

    def delete_assignment(self, assignment_id):
        if hasattr(self.db, "delete_assignment"):
            return self.db.delete_assignment(assignment_id)

        return None

    # ==========================================================
    # Timetable
    # ==========================================================

    def save_timetable(self, timetable):
        return self.db.save_timetable(timetable)

    def get_timetable(self):
        return self.db.get_timetable()

    def get_today_timetable(self):
        return self.db.get_today_timetable()

    def update_timetable(self, timetable_id, updated_data):
        return self.db.update_timetable(
            timetable_id,
            updated_data
        )

    def delete_timetable(self, timetable_id):
        return self.db.delete_timetable(
            timetable_id
        )

    def get_total_classes(self):
        return self.db.get_total_classes()

    # ==========================================================
    # Placement
    # ==========================================================

    def save_placement(self, placement):
        return self.db.save_placement(placement)

    def get_placements(self, student_id=None):
        return self.db.get_placements(student_id)

    def delete_placement(self, placement_id):
        if hasattr(self.db, "delete_placement"):
            return self.db.delete_placement(placement_id)

        return None

    # ==========================================================
    # Career
    # ==========================================================

    def save_career(self, career):
        return self.db.save_career(career)

    def get_careers(self):
        return self.db.get_careers()

    def get_latest_career(self):
        return self.db.get_latest_career()

    def delete_career(self, career_id):
        return self.db.delete_career(career_id)

    def get_total_career_reports(self):
        return self.db.get_total_career_reports()

    # ==========================================================
    # Events
    # ==========================================================

    def save_event(self, event):
        return self.db.save_event(event)

    def get_events(self):
        return self.db.get_events()

    def get_upcoming_events(self):
        return self.db.get_upcoming_events()

    def get_latest_event(self):
        return self.db.get_latest_event()

    def delete_event(self, event_id):
        return self.db.delete_event(event_id)

    def get_total_events(self):
        return self.db.get_total_events()

    # ==========================================================
    # Chat History
    # ==========================================================

    def save_chat(self, chat):
        return self.db.save_chat(chat)

    def get_chat_history(self):
        return self.db.get_chat_history()