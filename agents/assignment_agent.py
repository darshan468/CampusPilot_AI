from core.llm import llm
from core.prompts import Prompts

from utils.datetime_utils import DateTimeUtils


class AssignmentAgent:

    def __init__(self, assignment_tool=None):
        self.assignment_tool = assignment_tool

    def generate_assignment_plan(
        self,
        subject,
        assignment_title,
        due_date,
        priority
    ):
        """
        Generates an AI assignment completion plan.
        """

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

Assignment:
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
3. Keep the last day for final review.
4. Mention the date for every task.
5. Suggest daily goals.
6. Motivate the student.
7. Return the response in Markdown.
"""

        try:

            assignment_plan = llm.generate(prompt)

            return assignment_plan

        except Exception as e:

            return f"""
## ❌ AI Service Error

CampusPilot AI couldn't generate the assignment plan.

Reason:

{str(e)}
"""

    def run(self, state):

        return self.generate_assignment_plan(
            subject=state.get("subject"),
            assignment_title=state.get("assignment_title"),
            due_date=state.get("due_date"),
            priority=state.get("priority"),
        )