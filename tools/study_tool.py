from core.prompts import Prompts
from utils.datetime_utils import DateTimeUtils


class StudyTool:
    """
    ==========================================================
    CampusPilot AI - Study Tool
    ==========================================================

    Responsibilities
    ----------------
    • Generate AI study plans
    • Save study plans
    """

    def __init__(self, repository, llm):

        self.repository = repository
        self.llm = llm

    def generate_plan(
        self,
        subject,
        exam_date,
        daily_hours,
        difficulty
    ):

        today = DateTimeUtils.get_today()

        days_left = DateTimeUtils.days_remaining(exam_date)

        if days_left <= 0:

            return (
                "❌ The exam date must be after today's date.\n\n"
                "Please choose a future date."
            )

        prompt = f"""
{Prompts.STUDY}

Subject:
{subject}

Today's Date:
{DateTimeUtils.format_date(today)}

Exam Date:
{DateTimeUtils.format_date(exam_date)}

Days Remaining:
{days_left}

Daily Study Time:
{daily_hours}

Difficulty:
{difficulty}

Instructions:

1. Create a daily study schedule.
2. Divide the syllabus evenly.
3. Allocate revision time.
4. Keep the final day for revision.
5. Mention the date for every task.
6. Motivate the student.
7. Return the response in Markdown.
"""

        plan = self.llm.generate(prompt)

        try:

            self.repository.save_plan({

                "subject": subject,

                "exam_date": exam_date,

                "daily_hours": daily_hours,

                "difficulty": difficulty,

                "plan": plan

            })

        except Exception:

            # Saving failure shouldn't stop the response
            pass

        return plan

    def process(self, state):

        return self.generate_plan(

            subject=state.get("subject"),

            exam_date=state.get("exam_date"),

            daily_hours=state.get("daily_hours"),

            difficulty=state.get("difficulty")

        )