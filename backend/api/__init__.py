from fastapi import FastAPI
from .v1 import *
from .v1.endpoint import add_project
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# 解决跨域问题
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1, prefix="/api")                      # 前缀


