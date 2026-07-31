from datetime import datetime

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# =====================================================
# Student Profile
# =====================================================

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20))

    college = Column(String(150))
    department = Column(String(100))
    year = Column(String(30))
    semester = Column(String(20))

    career_goal = Column(String(100))
    preferred_study_time = Column(String(50))
    learning_style = Column(String(50))

    profile_image = Column(String(255))


# =====================================================
# Study Plans
# =====================================================

class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)

    subject = Column(String(100), nullable=False)
    exam_date = Column(Date)

    daily_hours = Column(String(20))
    difficulty = Column(String(30))

    plan = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# =====================================================
# Assignments
# =====================================================

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)

    subject = Column(String(100), nullable=False)
    assignment_title = Column(String(200), nullable=False)

    due_date = Column(Date)

    priority = Column(String(20))

    status = Column(
        String(20),
        default="Pending",
        nullable=False
    )

    ai_plan = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# =====================================================
# Timetable
# =====================================================

class Timetable(Base):
    __tablename__ = "timetable"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(String(20), nullable=False)
    subject = Column(String(100), nullable=False)
    faculty = Column(String(100))

    start_time = Column(String(20), nullable=False)
    end_time = Column(String(20), nullable=False)

    room = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# =====================================================
# Placement
# =====================================================

class Placement(Base):
    __tablename__ = "placements"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)

    interview_date = Column(String(30))
    notes = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# =====================================================
# Career Guidance
# =====================================================

class Career(Base):
    __tablename__ = "career"

    id = Column(Integer, primary_key=True, index=True)

    target_role = Column(String(100), nullable=False)
    current_skills = Column(Text, nullable=False)

    experience = Column(String(50))
    career_goal = Column(String(200))

    roadmap = Column(Text)
    recommendations = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# =====================================================
# Events
# =====================================================

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(150), nullable=False)

    event_type = Column(String(50), nullable=False)

    event_date = Column(Date, nullable=False)

    event_time = Column(String(20))

    venue = Column(String(150))

    organizer = Column(String(100))

    description = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


# =====================================================
# Chat History
# =====================================================

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )