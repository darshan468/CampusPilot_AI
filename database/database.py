from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import (
    Base,
    Student,
    StudyPlan,
    Assignment,
    Timetable,
    Placement,
    Event,
    Career,
    ChatHistory
)

print("Loading:", __file__)

DATABASE_URL = "sqlite:///database/campuspilot.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


from database.models import Student

class DatabaseManager:
    
    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def get_session(self):
        return SessionLocal()

    def save_student(self, student_data):
        db = self.get_session()

        try:
            student = db.query(Student).first()

            if student:
                for key, value in student_data.items():
                    setattr(student, key, value)
            else:
                student = Student(**student_data)
                db.add(student)

            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    # =====================================================
    # Student
    # =====================================================

    def get_student(self, student_id=None):
    
        db = self.get_session()

        try:

            if student_id:
                return (
                    db.query(Student)
                    .filter(Student.id == student_id)
                    .first()
                )

            return db.query(Student).first()

        finally:

            db.close()

    # =====================================================
    # Study Plans
    # =====================================================

    def save_study_plan(self, study_data):

        db = self.get_session()

        try:
            plan = StudyPlan(**study_data)
            db.add(plan)
            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    def get_all_study_plans(self):

        db = self.get_session()

        try:
            return db.query(StudyPlan).all()

        finally:
            db.close()

    def get_total_study_plans(self):

        db = self.get_session()

        try:
            return db.query(StudyPlan).count()

        finally:
            db.close()

    # =====================================================
    # Assignments
    # =====================================================

    def save_assignment(self, assignment_data):

        db = self.get_session()

        try:

            assignment = Assignment(**assignment_data)

            db.add(assignment)

            db.commit()

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_all_assignments(self):

        db = self.get_session()

        try:

            return db.query(Assignment).all()

        finally:

            db.close()

    def get_total_assignments(self):

        db = self.get_session()

        try:

            return db.query(Assignment).count()

        finally:

            db.close()

    def get_pending_assignments(self):

        db = self.get_session()

        try:

            return (
                db.query(Assignment)
                .filter(Assignment.status == "Pending")
                .count()
            )

        finally:

            db.close()

    def get_completed_assignments(self):

        db = self.get_session()

        try:

            return (
                db.query(Assignment)
                .filter(Assignment.status == "Completed")
                .count()
            )

        finally:

            db.close()

    # =====================================================
    # Timetable
    # =====================================================

    def save_timetable(self, timetable_data):

        db = self.get_session()

        try:

            timetable = Timetable(**timetable_data)

            db.add(timetable)

            db.commit()

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_timetable(self):

        db = self.get_session()

        try:

            return (
                db.query(Timetable)
                .order_by(
                    Timetable.day,
                    Timetable.start_time
                )
                .all()
            )

        finally:

            db.close()

    def get_today_timetable(self, day):

        db = self.get_session()

        try:

            return (
                db.query(Timetable)
                .filter(Timetable.day == day)
                .order_by(Timetable.start_time)
                .all()
            )

        finally:

            db.close()

    def update_timetable(self, timetable_id, updated_data):

        db = self.get_session()

        try:

            timetable = (
                db.query(Timetable)
                .filter(Timetable.id == timetable_id)
                .first()
            )

            if timetable:

                for key, value in updated_data.items():
                    setattr(timetable, key, value)

                db.commit()

                return True

            return False

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def delete_timetable(self, timetable_id):

        db = self.get_session()

        try:

            timetable = (
                db.query(Timetable)
                .filter(Timetable.id == timetable_id)
                .first()
            )

            if timetable:

                db.delete(timetable)

                db.commit()

                return True

            return False

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_total_classes(self):

        db = self.get_session()

        try:

            return db.query(Timetable).count()

        finally:

            db.close()

    # =====================================================
    # Placements
    # =====================================================

    def save_placement(self, placement_data):

        db = self.get_session()

        try:

            placement = Placement(**placement_data)

            db.add(placement)

            db.commit()

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_placements(self):

        db = self.get_session()

        try:

            return db.query(Placement).all()

        finally:

            db.close()

    # =====================================================
    # Events
    # =====================================================

    def save_event(self, event_data):

        db = self.get_session()

        try:

            event = Event(**event_data)

            db.add(event)

            db.commit()

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_events(self):

        db = self.get_session()

        try:

            return db.query(Event).all()

        finally:

            db.close()
            
            
    # =====================================================
    # Career Guidance
    # =====================================================

    def save_career(self, career_data):

        db = self.get_session()

        try:

            career = Career(**career_data)

            db.add(career)

            db.commit()

            db.refresh(career)

            return career

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_careers(self):

        db = self.get_session()

        try:

            return (
                db.query(Career)
                .order_by(Career.created_at.desc())
                .all()
            )

        finally:

            db.close()

    def get_latest_career(self):

        db = self.get_session()

        try:

            return (
                db.query(Career)
                .order_by(Career.created_at.desc())
                .first()
            )

        finally:

            db.close()

    def get_total_career_reports(self):

        db = self.get_session()

        try:

            return db.query(Career).count()

        finally:

            db.close()

    def delete_career(self, career_id):

        db = self.get_session()

        try:

            career = (
                db.query(Career)
                .filter(Career.id == career_id)
                .first()
            )

            if career:

                db.delete(career)

                db.commit()

                return True

            return False

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    # =====================================================
    # Chat History
    # =====================================================

    def save_chat(self, user_message, ai_response):

        db = self.get_session()

        try:

            chat = ChatHistory(
                user_message=user_message,
                ai_response=ai_response
            )

            db.add(chat)

            db.commit()

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    def get_chat_history(self):

        db = self.get_session()

        try:

            return (
                db.query(ChatHistory)
                .order_by(ChatHistory.created_at.desc())
                .all()
            )

        finally:

            db.close()
            
    # =====================================================
    # Upcoming Events
    # =====================================================

    def get_upcoming_events(self):

        db = self.get_session()

        try:

            from datetime import date

            return (
                db.query(Event)
                .filter(Event.event_date >= date.today())
                .order_by(Event.event_date.asc())
                .all()
            )

        finally:

            db.close()

    # =====================================================
    # Latest Event
    # =====================================================

    def get_latest_event(self):

        db = self.get_session()

        try:

            return (
                db.query(Event)
                .order_by(Event.created_at.desc())
                .first()
            )

        finally:

            db.close()

    # =====================================================
    # Delete Event
    # =====================================================

    def delete_event(self, event_id):

        db = self.get_session()

        try:

            event = (
                db.query(Event)
                .filter(Event.id == event_id)
                .first()
            )

            if event:

                db.delete(event)
                db.commit()

                return True

            return False

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    # =====================================================
    # Total Events
    # =====================================================

    def get_total_events(self):

        db = self.get_session()

        try:

            return db.query(Event).count()

        finally:

            db.close()
            
            
# =====================================================
# Global Database Manager Instance
# =====================================================

db_manager = DatabaseManager()