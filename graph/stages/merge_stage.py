from graph.pipeline import PipelineStage

from agents.merger_agent import MergerAgent


class MergeStage(PipelineStage):

    def process(self, state):

        state["final_response"] = (
            MergerAgent.merge(
                state["responses"]
            )
        )

        return state