import json

from core.llm import llm


class ParserAgent:

    # =====================================================
    # Study Details Extraction
    # =====================================================

    @staticmethod
    def extract_study_details(query):

        prompt = f"""
You are an AI information extraction assistant.

Extract the following study details from the user's message.

Return ONLY valid JSON.

Fields:

subject
exam_date
daily_hours
difficulty

Rules:
- Return exam_date in YYYY-MM-DD format if possible.
- daily_hours should be a number.
- difficulty should be one of:
  Easy
  Medium
  Hard
- If any value is missing, return null.

Example:

User:
Create a study plan for Machine Learning.
My exam is on July 25.
I can study 3 hours daily.

Output:

{{
    "subject": "Machine Learning",
    "exam_date": "2026-07-25",
    "daily_hours": 3,
    "difficulty": "Medium"
}}

User:

{query}
"""

        try:

            response = llm.invoke(prompt)

            return json.loads(response.content)

        except Exception:

            return {
                "subject": None,
                "exam_date": None,
                "daily_hours": None,
                "difficulty": None
            }

    # =====================================================
    # Assignment Details Extraction
    # =====================================================

    @staticmethod
    def extract_assignment_details(query):

        prompt = f"""
You are an AI information extraction assistant.

Extract the following assignment details from the user's message.

Return ONLY valid JSON.

Fields:

subject
assignment_title
due_date
priority

Rules:
- Return due_date in YYYY-MM-DD format if possible.
- Priority should be one of:
  Low
  Medium
  High
- If any value is missing, return null.

Example:

User:
My DBMS assignment "Normalization" is due on July 20.
It is high priority.

Output:

{{
    "subject": "DBMS",
    "assignment_title": "Normalization",
    "due_date": "2026-07-20",
    "priority": "High"
}}

User:

{query}
"""

        try:

            response = llm.invoke(prompt)

            return json.loads(response.content)

        except Exception:

            return {
                "subject": None,
                "assignment_title": None,
                "due_date": None,
                "priority": None
            }