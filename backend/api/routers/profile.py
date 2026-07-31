from fastapi import APIRouter

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/")
def profile():

    return {"message": "Profile API"}