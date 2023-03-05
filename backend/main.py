import uvicorn
# from starlette.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles

from api import app

app.mount('/static', StaticFiles(directory='./static'), name='static')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, log_level="info")