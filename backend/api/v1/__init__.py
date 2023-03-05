from fastapi import APIRouter
from .endpoint import addproj


v1 = APIRouter(prefix="/v1")

v1.include_router(addproj)



