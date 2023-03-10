from fastapi import APIRouter
from .endpoint import addproj, addInter, addField


v1 = APIRouter(prefix="/v1")

v1.include_router(addproj)
v1.include_router(addInter)
v1.include_router(addField)



