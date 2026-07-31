from typing import List

from graph.state import AgentState


class PipelineStage:

    def process(self, state: AgentState) -> AgentState:
        return state


class Pipeline:

    def __init__(self):

        self.stages: List[PipelineStage] = []

    def add_stage(self, stage: PipelineStage):

        self.stages.append(stage)

    def execute(self, state: AgentState):

        for stage in self.stages:

            state = stage.process(state)

            if state.get("error"):

                break

        return state