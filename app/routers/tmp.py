from fastapi import APIRouter

router = APIRouter(
    tags=["TMP"],
    prefix="/hello",
)


@router.get("/world")
def index():
    return {"Hello": "World"}