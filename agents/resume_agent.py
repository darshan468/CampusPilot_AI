import fitz

from core.llm import llm


def analyze_resume(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    prompt = f"""
You are an ATS Resume Expert.

Analyze this resume.

Give:

1. Resume Score /100

2. Strengths

3. Weaknesses

4. Missing Skills

5. ATS Improvements

6. Suggestions

Resume

{text}
"""

    response = llm.invoke(prompt)

    return response.content