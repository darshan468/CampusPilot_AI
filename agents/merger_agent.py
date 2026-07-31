from datetime import datetime


class MergerAgent:
    """
    ==========================================================
    CampusPilot AI - Merger Agent
    ==========================================================

    Responsibilities
    ----------------
    • Merge responses from multiple agents
    • Remove duplicate responses
    • Ignore empty responses
    • Format final Markdown response
    """

    @staticmethod
    def merge(responses):

        if not responses:
            return (
                "🤖 Sorry, I couldn't generate a response."
            )

        # ------------------------------------------
        # Remove empty responses
        # ------------------------------------------

        cleaned = [
            response.strip()
            for response in responses
            if response and response.strip()
        ]

        # ------------------------------------------
        # Remove duplicate responses
        # ------------------------------------------

        unique = []

        for response in cleaned:

            if response not in unique:
                unique.append(response)

        if not unique:

            return (
                "🤖 Sorry, I couldn't generate a response."
            )

        # ------------------------------------------
        # Single Agent Response
        # ------------------------------------------

        if len(unique) == 1:
            return unique[0]

        # ------------------------------------------
        # Multi-Agent Response
        # ------------------------------------------

        timestamp = datetime.now().strftime("%d %b %Y • %I:%M %p")

        final = "# 🎓 CampusPilot AI\n\n"

        final += (
            f"*Generated on {timestamp}*\n\n"
        )

        for index, response in enumerate(unique, start=1):

            final += (
                f"## Response {index}\n\n"
            )

            final += response.strip()

            final += "\n\n---\n\n"

        return final.rstrip("-\n ")