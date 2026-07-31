from agents.supervisor_agent import SupervisorAgent


class CampusCopilot:

    def __init__(self):
        self.supervisor = SupervisorAgent()

    def chat(self, query):

        return self.supervisor.process(query)