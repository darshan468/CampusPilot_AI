from core.llm import llm
from core.prompts import Prompts

from utils.datetime_utils import DateTimeUtils
from database.database import db_manager


class StudyAgent:

    def __init__(self, study_tool=None):
        self.study_tool = study_tool

    def generate_study_plan(
        self,
        subject,
        exam_date,
        daily_hours,
        difficulty
    ):

        # -----------------------------
        # Validate Input
        # -----------------------------
        if not subject:
            return "❌ Subject is required."

        if not exam_date:
            return "❌ Exam date is required."

        if not daily_hours:
            return "❌ Daily study hours are required."

        if not difficulty:
            return "❌ Difficulty level is required."

        # -----------------------------
        # Date Validation
        # -----------------------------
        today = DateTimeUtils.get_today()

        days_left = DateTimeUtils.days_remaining(exam_date)

        if days_left <= 0:

            return (
                "❌ The selected exam date must be after today's date.\n\n"
                "Please choose a future exam date."
            )

        # -----------------------------
        # AI Prompt
        # -----------------------------
        prompt = f"""
{Prompts.STUDY_PLANNER}

Student Details

Subject:
{subject}

Today's Date:
{DateTimeUtils.format_date(today)}

Exam Date:
{DateTimeUtils.format_date(exam_date)}

Days Remaining:
{days_left}

Daily Study Time:
{daily_hours} Hours

Difficulty:
{difficulty}

Instructions:

1. Start from today's date.
2. Never generate past dates.
3. Create exactly {days_left} study days.
4. Divide the syllabus evenly.
5. Reserve the final day for revision.
6. Mention the calendar date for every day.
7. Include:
   • Topics
   • Practice Questions
   • Revision
   • Daily Goal
   • Motivation
8. Format the output using Markdown.
"""

        # -----------------------------
        # Generate AI Response
        # -----------------------------
        try:

            study_plan = llm.generate(prompt)

        except Exception as e:

            return f"""
## ❌ CampusPilot AI Error

Unable to generate the study plan.

Reason:

{str(e)}
"""

        # -----------------------------
        # Save to Database
        # -----------------------------
        try:

            db_manager.save_study_plan(
                {
                    "subject": subject,
                    "exam_date": exam_date,
                    "daily_hours": daily_hours,
                    "difficulty": difficulty,
                    "plan": study_plan
                }
            )

        except Exception as e:

            print("Database Error:", e)

        # -----------------------------
        # Final Response
        # -----------------------------
        return f"""
# 📚 Personalized Study Plan

### ✅ Study Plan Created Successfully

**Subject:** {subject}

**Exam Date:** {DateTimeUtils.format_date(exam_date)}

**Days Remaining:** {days_left}

**Daily Study Time:** {daily_hours} Hours

**Difficulty:** {difficulty}

---

{study_plan}

---

✅ Your study plan has been saved successfully in CampusPilot AI.
"""

    def run(self, state):

        return self.generate_study_plan(
            subject=state.get("subject"),
            exam_date=state.get("exam_date"),
            daily_hours=state.get("daily_hours"),
            difficulty=state.get("difficulty"),
        )