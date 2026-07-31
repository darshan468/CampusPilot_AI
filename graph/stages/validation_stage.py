from graph.pipeline import PipelineStage


class ValidationStage(PipelineStage):

    def process(self, state):

        if not state.get("query"):

            state["error"] = "Empty query."

        return state