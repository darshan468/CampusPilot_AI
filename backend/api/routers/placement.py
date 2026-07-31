from fastapi import APIRouter

router = APIRouter(
    prefix="/placement",
    tags=["Placement"]
)


@router.get("/")
def placement():

    return {"message": "Placement API"}