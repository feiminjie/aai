from typing import Union
from pydantic import BaseModel


class Projects(BaseModel):
    project_name: str
    project_url: str
    remark: str