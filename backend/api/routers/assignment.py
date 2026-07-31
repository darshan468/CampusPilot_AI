from fastapi import APIRouter

router = APIRouter(
    prefix="/assignment",
    tags=["Assignment"]
)


@router.get("/")
def assignment():

    return {"message": "Assignment API"}