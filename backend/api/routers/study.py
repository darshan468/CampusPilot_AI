from fastapi import APIRouter

router = APIRouter(
    prefix="/study",
    tags=["Study"]
)


@router.get("/")
def study():

    return {"message": "Study API"}