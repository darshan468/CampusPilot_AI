from fastapi import APIRouter

from graph.workflow import CampusPilotWorkflow

from backend.api.schemas.chat import ChatRequest

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

workflow = CampusPilotWorkflow()


@router.post("/")
def chat(request: ChatRequest):

    response = workflow.run(

        query=request.query,

        memory=request.memory
    )

    return {

        "success": True,

        "response": response
    }