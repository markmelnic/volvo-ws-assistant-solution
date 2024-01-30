from . import *

router = APIRouter(tags=["Server"])


@router.get("/")
def default():
    return status.HTTP_418_IM_A_TEAPOT


@router.get("/ping")
def ping():
    return "pong"
