from graph.pipeline import PipelineStage


class PlanningStage(PipelineStage):

    def __init__(self, supervisor):

        self.supervisor = supervisor

    def process(self, state):

        decision = self.supervisor.process(
            state["query"]
        )

        state["agents"] = decision.get(
            "agents",
            []
        )

        state["execution_plan"] = decision.get(
            "execution_plan",
            []
        )

        return state