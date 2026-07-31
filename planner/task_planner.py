from typing import List, Dict


class TaskPlanner:
    """
    CampusPilot AI Task Planner

    Creates an execution plan
    from the agents selected by
    the Supervisor.
    """

    @staticmethod
    def create_plan(agents: List[str]) -> List[Dict]:

        plan = []

        for index, agent in enumerate(agents, start=1):

            plan.append(
                {
                    "step": index,
                    "agent": agent,
                    "status": "pending"
                }
            )

        return plan