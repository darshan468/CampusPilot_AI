from core.prompts import Prompts
from utils.datetime_utils import DateTimeUtils


class AssignmentTool:
    """
    ==========================================================
    CampusPilot AI - Assignment Tool
    ==========================================================

    Responsibilities
    ----------------
    • Generate AI assignment plans
    • Save assignment plans
    """

    def __init__(self, repository, llm):

        self.repository = repository
        self.llm = llm

    def generate_assignment_plan(
        self,
        subject,
        assignment_title,
        due_date,
        priority
    ):

        today = DateTimeUtils.get_today()

        days_left = DateTimeUtils.days_remaining(due_date)

        if days_left <= 0:

            return (
                "❌ The due date must be after today's date.\n\n"
                "Please choose a future due date."
            )

        prompt = f"""
{Prompts.ASSIGNMENT}

Subject:
{subject}

Assignment Title:
{assignment_title}

Today's Date:
{DateTimeUtils.format_date(today)}

Due Date:
{DateTimeUtils.format_date(due_date)}

Days Remaining:
{days_left}

Priority:
{priority}

Instructions:

1. Divide the assignment into daily tasks.
2. Allocate work evenly.
3. Keep the final day for review.
4. Mention the date for every task.
5. Suggest achievable daily goals.
6. Motivate the student.
7. Return the response in Markdown.
"""

        plan = self.llm.generate(prompt)

        try:

            self.repository.save_assignment({

                "subject": subject,

                "assignment_title": assignment_title,

                "due_date": due_date,

                "priority": priority,

                "ai_plan": plan

            })

        except Exception:

            # Ignore database save failures
            pass

        return plan

    def process(self, state):

        return self.generate_assignment_plan(

            subject=state.get("subject"),

            assignment_title=state.get("assignment_title"),

            due_date=state.get("due_date"),

            priority=state.get("priority")

        )