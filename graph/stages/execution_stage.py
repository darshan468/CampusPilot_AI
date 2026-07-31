from graph.pipeline import PipelineStage


class ExecutionStage(PipelineStage):

    def __init__(self, engine):

        self.engine = engine

    def process(self, state):

        return self.engine.execute_plan(state)